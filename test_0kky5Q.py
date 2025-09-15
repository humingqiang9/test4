import pytest

def reverse_string(s):
    """Function to reverse a string."""
    return s[::-1]

def test_reverse_string():
    """Test case for reversing a string."""
    # Test with a regular string
    assert reverse_string("hello") == "olleh"
    
    # Test with an empty string
    assert reverse_string("") == ""
    
    # Test with a single character
    assert reverse_string("a") == "a"
    
    # Test with a palindrome
    assert reverse_string("racecar") == "racecar"
    
    # Test with spaces and punctuation
    assert reverse_string("hello, world!") == "!dlrow ,olleh"

def test_reverse_string_with_numbers():
    """Test case for reversing strings with numbers."""
    assert reverse_string("12345") == "54321"
    assert reverse_string("abc123") == "321cba"

if __name__ == "__main__":
    pytest.main([__file__])