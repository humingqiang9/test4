import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import Counter from './Counter';

describe('Counter Component', () => {
  test('renders with initial count', () => {
    render(<Counter initialCount={5} />);
    expect(screen.getByText('Counter: 5')).toBeInTheDocument();
  });

  test('increments count when increment button is clicked', () => {
    render(<Counter />);
    const incrementButton = screen.getByText('Increment');
    const counterDisplay = screen.getByText('Counter: 0');
    
    fireEvent.click(incrementButton);
    expect(counterDisplay).toHaveTextContent('Counter: 1');
    
    fireEvent.click(incrementButton);
    expect(counterDisplay).toHaveTextContent('Counter: 2');
  });

  test('decrements count when decrement button is clicked', () => {
    render(<Counter />);
    const decrementButton = screen.getByText('Decrement');
    const counterDisplay = screen.getByText('Counter: 0');
    
    fireEvent.click(decrementButton);
    expect(counterDisplay).toHaveTextContent('Counter: -1');
  });

  test('resets count when reset button is clicked', () => {
    render(<Counter initialCount={3} />);
    const incrementButton = screen.getByText('Increment');
    const resetButton = screen.getByText('Reset');
    const counterDisplay = screen.getByText('Counter: 3');
    
    // Increment first
    fireEvent.click(incrementButton);
    fireEvent.click(incrementButton);
    expect(counterDisplay).toHaveTextContent('Counter: 5');
    
    // Then reset
    fireEvent.click(resetButton);
    expect(counterDisplay).toHaveTextContent('Counter: 3');
  });
});