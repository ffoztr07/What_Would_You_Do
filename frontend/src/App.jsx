import { useState, useEffect } from 'react'
import './App.css'
import { Button } from './components/common';
import { Input } from './components/common';
import { Text } from './components/common';
import { Box } from './components/common';
import { Rating } from './components/common';
import Container from './components/layout/Container.jsx';
import Stack from './components/layout/Stack.jsx';

function App() {
  const [questionText, setQuestionText] = useState('');
  const [correctVersionOfAnswer, setCorrectVersionOfAnswer] = useState('');
  const [ratingOfAnswer, setRatingOfAnswer] = useState(0);
  const [userAnswer, setUserAnswer] = useState('');
  const [isSubmitted, setIsSubmitted] = useState(false);
  const [isLoading, setIsLoading] = useState(false);
  const [isMobile, setIsMobile] = useState(false);

  // Responsive breakpoint detection
  useEffect(() => {
    const checkMobile = () => {
      setIsMobile(window.innerWidth <= 768);
    };
    
    checkMobile();
    window.addEventListener('resize', checkMobile);
    
    return () => window.removeEventListener('resize', checkMobile);
  }, []);

  const getQuestion = async () => {
    try {
      const res = await fetch('/api/get_question');
      const data = await res.json();
      setQuestionText(data?.message ?? 'No message');
    } catch (err) {
      setQuestionText('Failed to reach backend');
    }
  }

  const submitAnswer = async () => {
    if (isLoading) return; // Prevent multiple submissions
    
    setIsLoading(true);
    try {
      const res = await fetch('/api/submit_answer', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ answer: userAnswer, question: questionText }),
      });
      const data = await res.json();
      setCorrectVersionOfAnswer(data?.corrected_answer ?? 'No corrected answer');
      setRatingOfAnswer(data?.rating ?? 0);
      setIsSubmitted(true);
    } catch (err) {
      setCorrectVersionOfAnswer('Failed to reach backend');
      setIsSubmitted(true);
    } finally {
      setIsLoading(false);
    }
  }

  const handleInputChange = (e) => {
    setUserAnswer(e.target.value);
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      if (!isSubmitted && !isLoading && userAnswer.trim()) {
        submitAnswer();
      }
    }
  };

  const submitButton = () => {
    submitAnswer();
  }

  const handleGetNewQuestion = () => {
    setQuestionText('');
    getQuestion();
    setCorrectVersionOfAnswer('');
    setRatingOfAnswer(0);
    setUserAnswer('');
    setIsSubmitted(false);
    setIsLoading(false);
  };

  useEffect(() => {
    getQuestion();
  }, []);
  
  return (
    <Container size={isMobile ? "sm" : "md"}>
      <Stack gap={isMobile ? 48 : 72} align="center">
       
        <Text
          variant="primary"
          size={isMobile ? "small" : "medium"}
          weight="bold"
          align="center"
          style={{ 
            maxWidth: isMobile ? '100%' : '600px', 
            textAlign: 'center', 
            margin: '0 auto',
            padding: isMobile ? '0 16px' : '0'
          }}
        >
          {questionText}
        </Text>
        
        <Stack direction="column" gap={isMobile ? 24 : 36} align="center" style={{ width: '100%' }}>
          <Input
            type="textarea"
            size={isMobile ? "small" : "medium"}
            placeholder='Enter your answer'
            value={userAnswer}
            onChange={handleInputChange}
            onKeyDown={handleKeyDown}
            disabled={isSubmitted || isLoading}
            style={{ 
              width: isMobile ? '100%' : '400px', 
              minHeight: isMobile ? '100px' : '120px', 
              textAlign: 'left',
              maxWidth: '100%'
            }}
          />
          
          <Box 
            size="sm" 
            variant="muted" 
            style={{ 
              width: isMobile ? '100%' : '400px', 
              textAlign: 'center',
              maxWidth: '100%'
            }}
          >
            <Text 
              variant="muted" 
              size={isMobile ? "xs" : "small"} 
              align="center"
              style={{ lineHeight: '1.4' }}
            >
              Please note that your responses may be used to improve our AI systems and for commercial purposes.
              We respect your privacy and handle all data securely.
            </Text>
          </Box>
          
          <Button 
            size={isMobile ? "large" : "medium"} 
            onClick={submitButton}
            loading={isLoading}
            disabled={isSubmitted || isLoading || !userAnswer.trim()}
            style={{ width: isMobile ? '100%' : 'auto' }}
          >
            {isLoading ? 'Submitting...' : 'Submit'}
          </Button>
          
        </Stack>

        {isSubmitted && (
          <Stack direction="column" gap={isMobile ? 16 : 24} align="center" style={{ width: '100%' }}>
            <Box 
              size="sm" 
              variant="primary" 
              style={{ 
                width: isMobile ? '100%' : '480px', 
                textAlign: 'center',
                maxWidth: '100%'
              }}
            >
              <Text 
                as="div" 
                weight="medium"
                size={isMobile ? "small" : "medium"}
              >
                {correctVersionOfAnswer || 'Corrected Version Of Answer'}
              </Text>
            </Box>
            <Rating size={isMobile ? "md" : "lg"} value={ratingOfAnswer} readOnly={true} />
            <Button 
              variant="secondary" 
              size={isMobile ? "large" : "large"} 
              onClick={handleGetNewQuestion}
              style={{ width: isMobile ? '100%' : 'auto' }}
            >
              Get New Question
            </Button>
          </Stack>
        )}
      </Stack>
    </Container>
  )
}

export default App
