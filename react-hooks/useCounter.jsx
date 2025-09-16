import { useState, useEffect } from 'react';

/**
 * A custom React hook that manages a counter state.
 * @param {number} initialCount - The initial value for the counter.
 * @returns {object} An object containing the current count and functions to increment, decrement, and reset the counter.
 */
const useCounter = (initialCount = 0) => {
  const [count, setCount] = useState(initialCount);

  const increment = () => setCount((c) => c + 1);
  const decrement = () => setCount((c) => c - 1);
  const reset = () => setCount(initialCount);

  return { count, increment, decrement, reset };
};

export default useCounter;