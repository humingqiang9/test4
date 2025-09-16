# JUnit Calculator Test

This project contains a simple Calculator class and a JUnit test for its add method.

## Files

- `src/main/java/Calculator.java` - The Calculator class with an add method
- `src/test/java/CalculatorTest2k3xyCrVCu.java` - JUnit test for the Calculator's add method

## Dependencies

All required JUnit 5 jars are in the `lib` directory.

## How to Compile

```bash
# Compile the Calculator class
javac -d bin src/main/java/Calculator.java

# Compile the test class
javac -d bin -cp "lib/*:bin" src/test/java/CalculatorTest2k3xyCrVCu.java
```

## How to Run Tests

```bash
java -jar lib/junit-console.jar --class-path=bin --select-class=CalculatorTest2k3xyCrVCu
```

The test should pass successfully.