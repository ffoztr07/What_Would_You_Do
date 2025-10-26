import React from 'react';
import './Header.css';

const Header = ({ title = 'Alpha Mini', subtitle = 'AI Learning Assistant' }) => {
  return (
    <header className="app-header">
      <div className="header-content">
        <div className="header-logo">
          <div className="logo-icon">α</div>
          <div className="logo-text">
            <h1 className="app-title">{title}</h1>
            <p className="app-subtitle">{subtitle}</p>
          </div>
        </div>
        <div className="header-actions">
          <button className="header-button" aria-label="Settings">
            ⚙️
          </button>
        </div>
      </div>
    </header>
  );
};

export default Header;
