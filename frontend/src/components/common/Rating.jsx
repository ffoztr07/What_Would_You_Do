import React from 'react';
import PropTypes from 'prop-types';
import './Rating.css';

const Star = ({ filled, onClick, readOnly }) => (
  <button
    type="button"
    className={`rating__star ${filled ? 'rating__star--filled' : ''} ${readOnly ? 'rating__star--readonly' : ''}`}
    onClick={onClick}
    disabled={readOnly}
    aria-label={filled ? 'filled star' : 'empty star'}
  >
    ★
  </button>
);

Star.propTypes = {
  filled: PropTypes.bool,
  onClick: PropTypes.func,
  readOnly: PropTypes.bool,
};

const Rating = ({ value = 0, max = 5, onChange, size = 'md', className = '', readOnly = false }) => {
  return (
    <div className={[`rating rating--${size}`, className].filter(Boolean).join(' ')}>
      {Array.from({ length: max }).map((_, index) => {
        const starIndex = index + 1;
        return (
          <Star
            key={index}
            filled={starIndex <= value}
            onClick={() => !readOnly && onChange && onChange(starIndex)}
            readOnly={readOnly}
          />
        );
      })}
    </div>
  );
};

Rating.propTypes = {
  value: PropTypes.number,
  max: PropTypes.number,
  onChange: PropTypes.func,
  size: PropTypes.oneOf(['sm', 'md', 'lg']),
  className: PropTypes.string,
  readOnly: PropTypes.bool,
};

export default Rating;


