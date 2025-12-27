import math
from collections import Counter

def fact(n):
    if not isinstance(n, int) or n < 0:
        raise ValueError("Factorial is only defined for non-negative integers.")
    return math.factorial(n)

def convert(value, from_unit):
    unit = from_unit.lower()

    if unit == "farenheit":
        return (value - 32) * 5 / 9, "Celsius"
    elif unit == "celcius":
        return (value * 9 / 5) + 32, "Fahrenheit"
    elif unit == "centimeters":
        return value / 2.54, "Inches"
    elif unit == "inches":
        return value * 2.54, "Centimeters"
    else:
        return None, "Error: Unknown unit type"

def mean(data):
    return sum(data) / len(data) if data else 0

def median(data):
    if not data:
        return 0
    s = sorted(data)
    n = len(s)
    mid = n // 2
    return (s[mid - 1] + s[mid]) / 2 if n % 2 == 0 else s[mid]

def mode(data):
    if not data:
        return []
    c = Counter(data)
    m = max(c.values())
    return [k for k,v in c.items() if v == m]

def standard_deviation(data):
    if len(data) < 2:
        return 0.0
    avg = mean(data)
    var = sum((x - avg) ** 2 for x in data) / (len(data) - 1)
    return math.sqrt(var)
