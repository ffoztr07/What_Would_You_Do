import React from 'react';
import PropTypes from 'prop-types';
import './Stack.css';

const Stack = ({
  children,
  direction = 'column',
  gap = 12,
  align = 'stretch',
  justify = 'flex-start',
  wrap = false,
  className = '',
  ...props
}) => {
  const style = {
    '--stack-gap': typeof gap === 'number' ? `${gap}px` : gap,
  };

  const classes = [
    'stack',
    `stack--${direction}`,
    `stack--align-${align}`,
    `stack--justify-${justify}`,
    wrap ? 'stack--wrap' : '',
    className,
  ]
    .filter(Boolean)
    .join(' ');

  return (
    <div className={classes} style={style} {...props}>
      {children}
    </div>
  );
};

Stack.propTypes = {
  children: PropTypes.node,
  direction: PropTypes.oneOf(['row', 'column']),
  gap: PropTypes.oneOfType([PropTypes.number, PropTypes.string]),
  align: PropTypes.oneOf(['stretch', 'flex-start', 'center', 'flex-end', 'baseline']),
  justify: PropTypes.oneOf(['flex-start', 'center', 'flex-end', 'space-between', 'space-around', 'space-evenly']),
  wrap: PropTypes.bool,
  className: PropTypes.string,
};

export default Stack;


