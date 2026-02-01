import React from 'react';
import { Link } from 'react-router-dom';

export const Header: React.FC = () => {
  return (
    <header className="bg-white shadow-md">
      <div className="container mx-auto px-4 py-3 flex items-center justify-between">
        <Link to="/" className="flex items-center gap-3">
          <img 
            src="/assets/image1.png" 
            alt="NICE Academy Logo" 
            className="h-20 w-auto object-contain"
            onError={(e) => {
              // Fallback if image fails or isn't the right one
              e.currentTarget.style.display = 'none';
              e.currentTarget.parentElement?.classList.add('text-blue-600', 'font-bold', 'text-3xl');
              if (e.currentTarget.parentElement) e.currentTarget.parentElement.innerText = 'NICE ACADEMY';
            }}
          />
          <span className="text-2xl font-bold text-gray-800 hidden md:block">
            NICE ACADEMY
          </span>
        </Link>
        <nav>
          <ul className="flex gap-6 items-center">
            <li>
              <Link to="/" className="text-gray-600 hover:text-blue-600 font-medium">
                Home
              </Link>
            </li>
            <li>
              <a href="#services" className="text-gray-600 hover:text-blue-600 font-medium">
                Services
              </a>
            </li>
            <li>
              <a href="#contact" className="text-gray-600 hover:text-blue-600 font-medium">
                Contact
              </a>
            </li>
          </ul>
        </nav>
      </div>
    </header>
  );
};
