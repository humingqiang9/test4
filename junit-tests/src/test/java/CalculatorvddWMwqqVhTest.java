import org.junit.jupiter.api.Test;
import org.junit.jupiter.api.DisplayName;
import static org.junit.jupiter.api.Assertions.*;

public class CalculatorvddWMwqqVhTest {

    @Test
    @DisplayName("Test addition of two positive numbers")
    public void testAddTwoPositiveNumbers() {
        Calculator calculator = new Calculator();
        assertEquals(5, calculator.add(2, 3), "2 + 3 should equal 5");
    }

    @Test
    @DisplayName("Test addition with zero")
    public void testAddWithZero() {
        Calculator calculator = new Calculator();
        assertEquals(7, calculator.add(7, 0), "7 + 0 should equal 7");
        assertEquals(7, calculator.add(0, 7), "0 + 7 should equal 7");
    }

    @Test
    @DisplayName("Test addition of negative numbers")
    public void testAddNegativeNumbers() {
        Calculator calculator = new Calculator();
        assertEquals(-5, calculator.add(-2, -3), "-2 + -3 should equal -5");
        assertEquals(2, calculator.add(5, -3), "5 + -3 should equal 2");
    }

    @Test
    @DisplayName("Test addition of floating point numbers")
    public void testAddFloatingPointNumbers() {
        Calculator calculator = new Calculator();
        assertEquals(5.5, calculator.add(2.2, 3.3), 0.01, "2.2 + 3.3 should equal 5.5");
    }
}