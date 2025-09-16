// Function to generate Fibonacci sequence up to n terms
function fibonacci(n) {
  if (n <= 0) {
    console.log("Please enter a positive integer");
    return;
  }
  
  if (n === 1) {
    console.log([0]);
    return;
  }
  
  if (n === 2) {
    console.log([0, 1]);
    return;
  }
  
  let fibSequence = [0, 1];
  
  for (let i = 2; i < n; i++) {
    fibSequence[i] = fibSequence[i - 1] + fibSequence[i - 2];
  }
  
  console.log(fibSequence);
  return fibSequence;
}

// Example usage:
// fibonacci(10);