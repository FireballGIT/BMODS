import math
from collections import Counter

def fact(n):
    """Calculates the factorial of a non-negative integer n (n!)."""
    # Use math.factorial for a reliable built-in solution
    if not isinstance(n, int) or n < 0:
        raise ValueError("Factorial is only defined for non-negative integers.")
    return math.factorial(n)
  
def convert(value, from_unit):
    """Converts common units (temp and length)."""
    # Standardize input to lowercase for reliable comparisons
    unit = from_unit.lower()

    if unit == "farenheit":
        # Missing assignment to a return variable
        result = (value - 32) * 5 / 9
        return result, "Celsius"
    elif unit == "celcius":
        # Missing assignment and return
        result = (value * 9 / 5) + 32
        return result, "Fahrenheit"
    elif unit == "centimeters":
        # Missing assignment and return
        result = value / 2.54
        return result, "Inches"
    elif unit == "inches":
        # Missing assignment and return
        result = value * 2.54
        return result, "Centimeters"
    else:
        # Handle invalid input gracefully
        return None, "Error: Unknown unit type"

# --- New Statistics Functions ---

def mean(data_list):
    """Calculates the average (mean) of a list of numbers."""
    if not data_list:
        return 0
    # Sum all items and divide by the count of items
    return sum(data_list) / len(data_list)

def median(data_list):
    """Calculates the middle value (median) of a list of numbers."""
    if not data_list:
        return 0
    # The list must be sorted first
    sorted_list = sorted(data_list)
    n = len(sorted_list)
    mid_index = n // 2

    # If the list length is even, average the two middle numbers
    if n % 2 == 0:
        return (sorted_list[mid_index - 1] + sorted_list[mid_index]) / 2
    # If the list length is odd, return the exact middle number
    else:
        return sorted_list[mid_index]

def mode(data_list):
    """Finds the most frequently occurring value(s) in a list."""
    if not data_list:
        return []
    # Counter helps count frequency of items efficiently
    counts = Counter(data_list)
    if not counts:
        return []

    # Find the highest frequency count
    max_count = max(counts.values())
    
    # Return all items that match the highest frequency
    return [item for item, count in counts.items() if count == max_count]

def standard_deviation(data_list):
    """Calculates the standard deviation of a sample list of numbers."""
    if len(data_list) < 2:
        return 0.0

    avg = mean(data_list)
    # Calculate the variance (average of squared differences from the mean)
    variance = sum([(x - avg) ** 2 for x in data_list]) / (len(data_list) - 1)
    # Standard deviation is the square root of the variance
    return math.sqrt(variance)
