from sqlmodel import Session, select
from models import Question, engine, create_db_and_tables

def seed_questions():
    # First, create the database tables
    create_db_and_tables()
    
    with Session(engine) as session:
        try:
            # Sample questions with specific IDs
            questions = [
                # Social Situations
                "You're at a restaurant and receive the wrong order. The waiter seems very busy. What do you do?",
                "A stranger sits next to you on a long flight and won't stop talking. How do you handle this?",
                "You're at a party where you don't know anyone except the host, who is busy with other guests. What's your strategy?",
                "Your neighbor's dog keeps barking at 3 AM. How do you address this situation?",
                # Workplace Scenarios
                "You realize you've been CC'd on an email by mistake that contains sensitive information. What do you do?",
                "During a meeting, your colleague takes credit for your idea. How do you respond?",
                "You notice a coworker consistently arrives late but your boss hasn't said anything. What's your approach?",
                "The office coffee machine is broken and everyone is grumpy. How do you lighten the mood?",
                # Unexpected Situations
                "You're in an elevator that gets stuck between floors with three strangers. What do you do?",
                "While walking, you witness someone drop their wallet without noticing. What's your reaction?",
                "You're at a grocery store and realize you forgot your wallet at the checkout. How do you handle this?",
                "A tourist approaches you asking for directions to a place you've never heard of. What do you do?",
                # Digital Age Dilemmas
                "You accidentally send a text message complaining about someone TO that person. How do you fix this?",
                "Your friend posts an embarrassing photo of you on social media. What's your response?",
                "You see false information being shared online by someone you know. Do you intervene?",
                "Your phone dies during an important video call. How do you handle the situation?",
                # Travel & Transportation
                "Your train is delayed for 2 hours with no explanation. What do you do?",
                "You're lost in a foreign country where you don't speak the language. How do you find your way?",
                "The person next to you on the bus is eating something that smells terrible. What's your reaction?",
                "You accidentally get on the wrong bus and end up in an unfamiliar neighborhood. What do you do?",
                # Moral & Ethical Choices
                "You find a USB drive in a public place. What do you do with it?",
                "A cashier gives you too much change. How do you handle this?",
                "You see someone cheating on a test. What's your response?",
                "Your friend asks you to lie to their boss about why they missed work. What do you do?",
                # New Questions
                "You overhear a private conversation in a public place. Do you mention it to anyone?",
                "A friend borrows your favorite book and returns it damaged. How do you react?",
                "You witness a minor car accident. Do you get involved?",
                "You receive a gift you don't like from a close friend. How do you respond?",
                "Your roommate never does their share of the chores. What do you do?",
                "You are running late for an important meeting and someone asks you for directions. What do you do?",
                "You are asked to donate to a cause you don't support. How do you handle it?",
                "You are at a buffet and someone cuts in line. What do you do?",
                "You are given credit for something you didn't do at work. How do you handle it?",
                "You find a hair in your food at a friend's dinner party. What do you do?",
                "You are asked to cover for a coworker who is frequently absent. How do you respond?",
                "You are at a movie and someone is talking loudly behind you. What do you do?",
                "You are invited to an event you don't want to attend. How do you decline?",
                "You are asked a personal question in a group setting. How do you respond?",
                "You see someone shoplifting. What do you do?",
                "You are offered a job with a higher salary but less job satisfaction. What do you choose?",
                "You are at a friend's house and accidentally break something valuable. What do you do?",
                "You are asked to give a speech with little notice. How do you prepare?",
                "You are in a group project and one member isn't contributing. How do you handle it?",
                "You are at a wedding and don't know anyone at your table. How do you start a conversation?",
                "You are asked to review a friend's work and it's not good. How do you give feedback?",
                "You are at a concert and someone blocks your view. What do you do?",
                "You are in a rush and someone asks for your help. How do you respond?",
                "You are at a family gathering and a sensitive topic comes up. What do you do?",
                "You are at a restaurant and your food is undercooked. How do you handle it?",
                "You are at a gym and someone is not wiping down equipment. What do you do?",
                "You are at a hotel and your room is not clean. How do you address it?",
                "You are at a store and the cashier is rude. How do you respond?",
                "You are at a friend's house and they serve food you dislike. What do you do?",
                "You are at a meeting and someone interrupts you repeatedly. How do you handle it?",
                "You are at a park and see someone littering. What do you do?",
                "You are at a party and someone is clearly uncomfortable. What do you do?",
                "You are at a library and someone is being noisy. How do you respond?",
                "You are at a doctor's office and your appointment is delayed. What do you do?",
                "You are at a public pool and see unsafe behavior. What do you do?",
                "You are at a friend's wedding and your ex is there. How do you handle it?",
                "You are at a job interview and asked an illegal question. How do you respond?",
                "You are at a networking event and don't know anyone. How do you start a conversation?",
                "You are at a restaurant and your card is declined. What do you do?",
                "You are at a store and see a parent struggling with a child. Do you offer help?",
                "You are at a friend's house and they ask you to remove your shoes. What do you do?",
                "You are at a public event and someone faints. What do you do?",
                "You are at a bus stop and someone asks for money. How do you respond?",
                "You are at a hotel and the fire alarm goes off. What do you do?",
                "You are at a conference and lose your name badge. What do you do?",
                "You are at a restaurant and the tip is automatically added. Do you say anything?",
                "You are at a friend's house and their pet makes a mess. What do you do?",
                "You are at a store and someone asks you to watch their bag. What do you do?",
                "You are at a public restroom and there is no toilet paper. What do you do?",
                "You are at a party and someone spills a drink on you. How do you react?",
                "You are at a meeting and forget your notes. What do you do?",
                "You are at a restaurant and your order is taking too long. What do you do?",
                "You are at a friend's house and they start an argument. How do you handle it?",
                "You are at a store and the price is wrong at checkout. What do you do?",
                "You are at a public place and someone is taking photos without permission. What do you do?",
                "You are at a gym and someone is using equipment incorrectly. What do you do?",
                "You are at a hotel and your reservation is missing. What do you do?",
                "You are at a restaurant and see a bug in your food. What do you do?",
                "You are at a friend's house and they ask you to help move furniture. What do you do?",
                "You are at a store and someone cuts in line. How do you respond?",
                "You are at a public event and someone is being disruptive. What do you do?",
                "You are at a meeting and someone takes credit for your work. How do you handle it?",
                "You are at a party and someone is clearly intoxicated. What do you do?",
                "You are at a restaurant and your server is new and struggling. How do you respond?",
                "You are at a friend's house and they ask you to stay longer than planned. What do you do?",
                "You are at a store and the cashier gives you the wrong change. What do you do?",
                "You are at a public place and someone is talking loudly on the phone. What do you do?",
                "You are at a gym and someone is monopolizing equipment. What do you do?",
                "You are at a hotel and the room next door is noisy. What do you do?",
                "You are at a restaurant and your food is too spicy. What do you do?",
                "You are at a friend's house and they ask you to watch their pet. What do you do?",
                "You are at a store and someone asks for your opinion on a product. What do you do?",
                "You are at a public event and lose your wallet. What do you do?",
                "You are at a meeting and someone is dominating the conversation. What do you do?",
                "You are at a party and someone is making offensive jokes. What do you do?",
                "You are at a restaurant and your food is cold. What do you do?",
                "You are at a friend's house and they ask you to help cook. What do you do?",
                "You are at a store and see a child alone. What do you do?",
                "You are at a public place and someone is smoking where it's not allowed. What do you do?",
                "You are at a gym and someone asks to work in with you. What do you do?",
                "You are at a hotel and the amenities are not as advertised. What do you do?",
                "You are at a restaurant and your table is not ready. What do you do?",
                "You are at a friend's house and they ask you to help clean up. What do you do?",
                "You are at a store and someone is shoplifting. What do you do?",
                "You are at a public event and someone is lost. What do you do?",
                "You are at a meeting and someone is late. What do you do?",
                "You are at a party and someone is being rude. What do you do?",
                "You are at a restaurant and your drink is wrong. What do you do?",
                "You are at a friend's house and they ask you to stay for dinner. What do you do?",
                "You are at a store and the line is very long. What do you do?",
                "You are at a public place and someone is asking for donations. What do you do?",
                "You are at a gym and someone is not following the rules. What do you do?",
                "You are at a hotel and the staff is unhelpful. What do you do?",
                "You are at a restaurant and your reservation is lost. What do you do?",
                "You are at a friend's house and they ask you to help with a project. What do you do?",
            ]

            # Add questions to database
            added_count = 0
            for i, q_text in enumerate(questions):
                # Check if question with this text already exists
                existing = session.exec(select(Question).where(Question.text == q_text)).first()
                if not existing:
                    new_question = Question(text=q_text)
                    session.add(new_question)
                    added_count += 1
            
            session.commit()
            if added_count > 0:
                print(f"Successfully added {added_count} new questions to the database!")
            else:
                print("All questions already exist in the database.")
        except Exception as e:
            print(f"An error occurred: {e}")
            session.rollback()

if __name__ == "__main__":
    seed_questions() 