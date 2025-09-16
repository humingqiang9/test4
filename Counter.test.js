import React from 'react';
import { render, screen, fireEvent } from '@testing-library/react';
import Counter from './Counter';

// Mock the useState hook to control state in tests
jest.mock('react', () => ({
  ...jest.requireActual('react'),
  useState: jest.fn(),
}));

describe('Counter Component', () => {
  let setCountMock;

  beforeEach(() => {
    setCountMock = jest.fn();
    // Mock useState to return a specific value and our setter mock
    React.useState.mockImplementation((initialValue) => [initialValue, setCountMock]);
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  test('renders with initial count', () => {
    React.useState.mockImplementation(() => [5, setCountMock]);
    
    render(<Counter initialCount={5} />);
    
    expect(screen.getByText('Counter: 5')).toBeInTheDocument();
  });

  test('increment button increases count', () => {
    React.useState.mockImplementation(() => [0, setCountMock]);
    
    render(<Counter />);
    
    const incrementButton = screen.getByText('+');
    fireEvent.click(incrementButton);
    
    expect(setCountMock).toHaveBeenCalledWith(1);
  });

  test('decrement button decreases count', () => {
    React.useState.mockImplementation(() => [0, setCountMock]);
    
    render(<Counter />);
    
    const decrementButton = screen.getByText('-');
    fireEvent.click(decrementButton);
    
    expect(setCountMock).toHaveBeenCalledWith(-1);
  });

  test('reset button sets count back to initial value', () => {
    const initialCount = 10;
    React.useState.mockImplementation(() => [5, setCountMock]);
    
    render(<Counter initialCount={initialCount} />);
    
    const resetButton = screen.getByText('Reset');
    fireEvent.click(resetButton);
    
    expect(setCountMock).toHaveBeenCalledWith(initialCount);
  });
});