import React from 'react';
import PropTypes from 'prop-types';
import './Box.css';

const Box = ({ children, variant = 'primary', size = 'md', className = '', ...props }) => {
  const classes = [
    'box',
    `box--${variant}`,
    `box--${size}`,
    className,
  ]
    .filter(Boolean)
    .join(' ');

  return (
    <div className={classes} {...props}>
      {children}
    </div>
  );
};

Box.propTypes = {
  children: PropTypes.node,
  variant: PropTypes.oneOf(['primary', 'muted', 'inverted']),
  size: PropTypes.oneOf(['sm', 'md', 'lg']),
  className: PropTypes.string,
};

export default Box;


