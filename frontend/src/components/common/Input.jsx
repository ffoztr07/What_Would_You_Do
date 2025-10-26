import React from 'react';
import PropTypes from 'prop-types';
import './Input.css';

const Input = ({
  type = 'text',
  variant = 'primary',
  size = 'medium',
  disabled = false,
  fullWidth = false,
  placeholder = '',
  value = '',
  onChange,
  onFocus,
  onBlur,
  onKeyDown,
  className = '',
  label,
  error,
  required = false,
  style = {},
  ...props
}) => {
  const baseClass = 'input';
  const variantClass = `input--${variant}`;
  const sizeClass = `input--${size}`;
  const widthClass = fullWidth ? 'input--full-width' : '';
  const disabledClass = disabled ? 'input--disabled' : '';
  const errorClass = error ? 'input--error' : '';

  // Check if this should be a textarea based on minHeight or type
  const isTextarea = type === 'textarea' || (style && style.minHeight);

  const inputClasses = [
    baseClass,
    variantClass,
    sizeClass,
    widthClass,
    disabledClass,
    errorClass,
    isTextarea ? 'input--textarea' : '',
    className
  ].filter(Boolean).join(' ');

  const handleChange = (e) => {
    if (!disabled && onChange) {
      onChange(e);
    }
  };

  const handleFocus = (e) => {
    if (!disabled && onFocus) {
      onFocus(e);
    }
  };

  const handleBlur = (e) => {
    if (!disabled && onBlur) {
      onBlur(e);
    }
  };

  const handleKeyDown = (e) => {
    if (!disabled && onKeyDown) {
      onKeyDown(e);
    }
  };

  return (
    <div className="input-wrapper">
      {label && (
        <label className="input__label">
          {label}
          {required && <span className="input__required">*</span>}
        </label>
      )}
      {isTextarea ? (
        <textarea
          className={inputClasses}
          disabled={disabled}
          placeholder={placeholder}
          value={value}
          onChange={handleChange}
          onFocus={handleFocus}
          onBlur={handleBlur}
          onKeyDown={handleKeyDown}
          required={required}
          style={style}
          {...props}
        />
      ) : (
        <input
          type={type}
          className={inputClasses}
          disabled={disabled}
          placeholder={placeholder}
          value={value}
          onChange={handleChange}
          onFocus={handleFocus}
          onBlur={handleBlur}
          onKeyDown={handleKeyDown}
          required={required}
          style={style}
          {...props}
        />
      )}
      {error && (
        <div className="input__error-message">
          {error}
        </div>
      )}
    </div>
  );
};

Input.propTypes = {
  type: PropTypes.oneOf(['text', 'email', 'password', 'number', 'tel', 'url', 'search', 'textarea']),
  variant: PropTypes.oneOf(['primary', 'secondary', 'outline', 'ghost']),
  size: PropTypes.oneOf(['small', 'medium', 'large']),
  disabled: PropTypes.bool,
  fullWidth: PropTypes.bool,
  placeholder: PropTypes.string,
  value: PropTypes.string,
  onChange: PropTypes.func,
  onFocus: PropTypes.func,
  onBlur: PropTypes.func,
  onKeyDown: PropTypes.func,
  className: PropTypes.string,
  label: PropTypes.string,
  error: PropTypes.string,
  required: PropTypes.bool,
  style: PropTypes.object,
};

export default Input;
