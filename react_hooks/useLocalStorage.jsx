import { useState, useEffect } from 'react';

/**
 * Custom hook for managing browser localStorage.
 * @param {string} key - The localStorage key.
 * @param {*} initialValue - The initial value to use if the key is not present in localStorage.
 * @returns {Array} A stateful value and a function to update it, similar to useState.
 */
const useLocalStorage = (key, initialValue) => {
  // Get the initial value from localStorage or use the provided initial value
  const [storedValue, setStoredValue] = useState(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch (error) {
      console.error(`Error reading localStorage key "${key}":`, error);
      return initialValue;
    }
  });

  // Update localStorage when the state changes
  const setValue = (value) => {
    try {
      // Allow value to be a function so we have the same API as useState
      const valueToStore =
        value instanceof Function ? value(storedValue) : value;
      setStoredValue(valueToStore);
      window.localStorage.setItem(key, JSON.stringify(valueToStore));
    } catch (error) {
      console.error(`Error setting localStorage key "${key}":`, error);
    }
  };

  return [storedValue, setValue];
};

export default useLocalStorage;