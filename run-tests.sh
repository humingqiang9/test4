#!/bin/bash

echo "Compiling Calculator class..."
javac -d bin src/main/java/Calculator.java

echo "Compiling test class..."
javac -d bin -cp "lib/*:bin" src/test/java/CalculatorTest2k3xyCrVCu.java

echo "Running tests..."
java -jar lib/junit-console.jar --class-path=bin --select-class=CalculatorTest2k3xyCrVCu