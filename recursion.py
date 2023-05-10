# Part I: Fibonacci Sequence
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Part II: Euclid's GCD Algorithm
def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

# Part III: String Comparison
def compareTo(s1, s2):
    if len(s1) == 0 and len(s2) == 0:
        return 0
    elif len(s1) == 0:
        return -1
    elif len(s2) == 0:
        return 1
    else:
        if s1[0] == s2[0]:
            return compareTo(s1[1:], s2[1:])
        else:
            return ord(s1[0]) - ord(s2[0])

# Test the functions
print(fibonacci(5))  # Output: 5
print(gcd(56, 98))  # Output: 14
print(compareTo("apple", "apple"))  # Output: 0
print(compareTo("apple", "banana")) # Output: -1
print(compareTo("banana", "apple")) # Output: 1
