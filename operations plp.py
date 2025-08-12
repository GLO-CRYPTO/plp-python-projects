

x = 40
y = 12
# Addition
sum_result = x + y
print("Sum:", sum_result)

# Subtraction
diff_result = x - y
print("Difference:", diff_result)

# Multiplication
mul_result = x * 3
print("Multiplication Result:", mul_result)

# Division
div_result = x / y
print("Division Result:", div_result)

# Modulus
mod_result = x % y
print("Modulus Result:", mod_result)

# Floor Division
floor_result = x // 5
print("Floor Division Result:", floor_result)

# Exponentiation
exp_result = y ** 2
print("Exponentiation Result:", exp_result)

x = 85
y = 75
 
# Equal to
print("Is x equal to y?", x == y)  # False

# Greater than
print("Is x greater than y?", x > y)  # True

# Greater than
print("Is x greater than y?", x > y)  # True
 
# Less than
print("Is x less than y?", x < y)  # False
 
# Greater than or equal to
print("Is x greater than or equal to y?", x >= y)  # True
 
# Less than or equal to
print("Is x less than or equal to y?", x <= y)  # False


# Logical Operators Example
topics_covered = 5
required_topics = 8
certification_eligibility = 10
 
# Using and
print("Eligible for certification?", topics_covered >= required_topics and topics_covered >= certification_eligibility)  # False
 
# Using or
print("Can appear for a retest?", topics_covered >= required_topics or topics_covered >= certification_eligibility)  # False
 
# Using not
print("Not eligible for certification?", not(topics_covered >= certification_eligibility))  # True


#bitwise example
code = 12  # 0b1100
key = 5    # 0b0101

encrypted = (code ^ key) << 1
print(encrypted)


encrypted = 18
key = 5

# Step 1: Reverse the left shift
temp = encrypted >> 1  # 18 >> 1 → 9

# Step 2: Reverse the XOR
code = temp ^ key  # 9 ^ 5 → 12

print("Decrypted code:", code)  # Output: 12


# Bitwise Operators Example
a = 12  # Binary: 1100
b = 5   # Binary: 0101
# Bitwise AND
print("a & b:", a & b)  # 4 (0100)

# Bitwise OR
print("a | b:", a | b)  # 13 (1101)
 
# Bitwise XOR
print("a ^ b:", a ^ b)  # 9 (1001)
 
# Bitwise NOT
print("~a:", ~a)  # -13 (Inverts bits and adds 1 in two's complement)
 
# Left shift
print("a << 2:", a << 2)  # 48 (110000)
 
# Right shift
print("a >> 2:", a >> 2)  # 3 (0011)

a = 10  # Assigns 10 to a
print("a:", a)  
 
a += 5  # a = a + 5
print("a += 5:", a)  
 
a -= 3  # a = a - 3
print("a -= 3:", a)  
 
a *= 2  # a = a * 2
print("a *= 2:", a)  
 
a /= 4  # a = a / 4
print("a /= 4:", a)  
 
a %= 3  # a = a % 3
print("a %= 3:", a)  
 
a **= 2  # a = a ** 2
print("a **= 2:", a)  
 
a //= 2  # a = a // 2
print("a //= 2:", a)

# Identity Operators Example
a = [10, 20, 30]
b = a
c = [10, 20, 30]
 
# Using is
print("a is b:", a is b)  # True (Same memory location)
print("a is c:", a is c)  # False (Different memory locations)
 
# Using is not
print("a is not c:", a is not c)  # True
print("b is not a:", b is not a)  # False

# Membership Operators Example
topics = ["Python", "Java", "C++", "SQL"]
 
# Using in
print("Python in topics:", "Python" in topics)  # True
print("HTML in topics:", "HTML" in topics)      # False
 
# Using not in
print("Ruby not in topics:", "Ruby" not in topics)  # True
print("Java not in topics:", "Java" not in topics)  # False

# Operator Precedence Example
result = 5 + 3 * 2 ** 2 - 4 / 2
print("Result:", result) 

x = 40
y = 3
 
# Addition
sum_result = x + y
print("Sum:", sum_result)
 
# Subtraction
diff_result = x - y
print("Difference:", diff_result)
 
# Multiplication
mul_result = x * 3
print("Multiplication Result:", mul_result)
 
# Division
div_result = x / y
print("Division Result:", div_result)
 
# Modulus
mod_result = x % y
print("Modulus Result:", mod_result)
 
# Floor Division
floor_result = x // 5
print("Floor Division Result:", floor_result)

x = 12
y = 6

# Equal to
print(x == y)  # False

# Not equal to
print(x != y)  # True

# Greater than
print(x > y)   # True


# Less than
print(x < y)   # False

# Greater than or equal to
print(x >= 10) # True

# Less than or equal to
print(y <= 4)  # False
#identity operators
a = 7
b = 7
print(a == b)  # True (same value)
print(a is b)  # True (Python reuses small integers in memory)

c = 1000
d = 1000
print(c == d)  # True (same value)
print(c is d)  # True
#hierachy of operators
print(6 + 3 * 2 ** 2)  # 18 (Parentheses > ** > * > +)

