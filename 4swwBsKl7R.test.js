import React from 'react';
import { render, screen } from '@testing-library/react';
import WelcomeComponent from './WelcomeComponent';

describe('WelcomeComponent', () => {
  test('renders welcome message', () => {
    render(<WelcomeComponent />);
    
    // Check if the main heading is in the document
    const headingElement = screen.getByText(/Welcome to Our Application!/i);
    expect(headingElement).toBeInTheDocument();
    
    // Check if the paragraph text is in the document
    const paragraphElement = screen.getByText(/We're glad to have you here. Enjoy your stay!/i);
    expect(paragraphElement).toBeInTheDocument();
  });
  
  test('renders with correct styling', () => {
    render(<WelcomeComponent />);
    
    // Check if the component container exists
    const containerElement = screen.getByText(/Welcome to Our Application!/i).parentElement;
    expect(containerElement).toBeInTheDocument();
    
    // Check if the container has the expected styles
    expect(containerElement).toHaveStyle('text-align: center');
    expect(containerElement).toHaveStyle('padding: 20px');
    expect(containerElement).toHaveStyle('background-color: #f0f8ff');
    expect(containerElement).toHaveStyle('border-radius: 8px');
  });
});