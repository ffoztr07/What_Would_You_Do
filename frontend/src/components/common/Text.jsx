import React from 'react';
import PropTypes from 'prop-types';
import './Text.css';

const Text = ({
  children,
  as = 'span',
  variant = 'primary',
  size = 'medium',
  weight = 'regular',
  align = 'left',
  truncate = false,
  noWrap = false,
  italic = false,
  underline = false,
  strikethrough = false,
  className = '',
  ...props
}) => {
  const baseClass = 'text';
  const variantClass = `text--${variant}`;
  const sizeClass = `text--${size}`;
  const weightClass = `text--${weight}`;
  const alignClass = `text--align-${align}`;
  const truncateClass = truncate ? 'text--truncate' : '';
  const nowrapClass = noWrap ? 'text--nowrap' : '';
  const italicClass = italic ? 'text--italic' : '';
  const underlineClass = underline ? 'text--underline' : '';
  const strikeClass = strikethrough ? 'text--strike' : '';

  const classes = [
    baseClass,
    variantClass,
    sizeClass,
    weightClass,
    alignClass,
    truncateClass,
    nowrapClass,
    italicClass,
    underlineClass,
    strikeClass,
    className,
  ]
    .filter(Boolean)
    .join(' ');

  const Component = as;

  return (
    <Component className={classes} {...props}>
      {children}
    </Component>
  );
};

Text.propTypes = {
  children: PropTypes.node.isRequired,
  as: PropTypes.oneOf([
    'span',
    'p',
    'small',
    'strong',
    'em',
    'label',
    'h1',
    'h2',
    'h3',
    'h4',
    'h5',
    'h6',
  ]),
  variant: PropTypes.oneOf([
    'primary',
    'secondary',
    'muted',
    'success',
    'warning',
    'danger',
    'inverted',
  ]),
  size: PropTypes.oneOf(['small', 'medium', 'large']),
  weight: PropTypes.oneOf(['regular', 'medium', 'semibold', 'bold']),
  align: PropTypes.oneOf(['left', 'center', 'right', 'justify']),
  truncate: PropTypes.bool,
  noWrap: PropTypes.bool,
  italic: PropTypes.bool,
  underline: PropTypes.bool,
  strikethrough: PropTypes.bool,
  className: PropTypes.string,
};

export default Text;


