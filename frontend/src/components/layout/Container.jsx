import React from 'react';
import PropTypes from 'prop-types';
import './Container.css';

const Container = ({ children, size = 'md', centered = true, className = '', ...props }) => {
  const baseClass = 'container';
  const sizeClass = `container--${size}`;
  const centeredClass = centered ? 'container--centered' : '';

  const classes = [baseClass, sizeClass, centeredClass, className]
    .filter(Boolean)
    .join(' ');

  return (
    <div className={classes} {...props}>
      {children}
    </div>
  );
};

Container.propTypes = {
  children: PropTypes.node,
  size: PropTypes.oneOf(['sm', 'md', 'lg', 'xl']),
  centered: PropTypes.bool,
  className: PropTypes.string,
};

export default Container;


