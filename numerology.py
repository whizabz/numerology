# Program to calculate the sum of the characters of a name for numerology

import re

# Define the CHALDEAN dictionary
CHALDEAN_DICT = {
      'a': 1,
      'b': 2,
      'c': 3,
      'd': 4,
      'e': 5,
      'f': 8,
      'g': 3,
      'h': 5,
      'i': 1,
      'j': 1,
      'k': 2,
      'l': 3,
      'm': 4,
      'n': 5,
      'o': 7,
      'p': 8,
      'q': 1,
      'r': 2,
      's': 3,
      't': 4,
      'u': 6,
      'v': 6,
      'w': 6,
      'x': 5,
      'y': 1,
      'z': 7
}

# Define the PYTHAGOREAN dictionary
PYTHAGOREAN_DICT = {
      'a': 1,
      'b': 2,
      'c': 3,
      'd': 4,
      'e': 5,
      'f': 6,
      'g': 7,
      'h': 8,
      'i': 9,
      'j': 1,
      'k': 2,
      'l': 3,
      'm': 4,
      'n': 5,
      'o': 6,
      'p': 7,
      'q': 8,
      'r': 9,
      's': 1,
      't': 2,
      'u': 3,
      'v': 4,
      'w': 5,
      'x': 6,
      'y': 7,
      'z': 8
    };

# Function to get sum of digits 
def getSum(n):
    
    sum = 0
    while (n != 0):
       
        sum = sum + (n % 10)
        n = n//10
       
    return sum

# Count number of digits in a number
def countDigit(n):
    count = 0
    while n != 0:
        n //= 10
        count += 1
    return count

# Open file with names
f = open("names.txt", "r")

# For each name
for x in f:
    # Remove "\n" line endings because we're in Windows
    name=re.sub("\n", "", x)
    
    # Set the character sum
    char_sum=0
    
    # Calculate character sum based on dictionary
    for character in list(name):
        char_sum = char_sum + CHALDEAN_DICT[character.lower()] 
    
    # Set the digit sum
    digit_sum=char_sum

    # Calculate digit sum till we have just 1 digit
    while countDigit(digit_sum) > 1:
        digit_sum=getSum(digit_sum)
    
    # Print names with 6 as the digit sum
    if digit_sum == 6:
        print(name)
    
    # Print name, character sum and digit sum
    # print(name, char_sum, digit_sum)

# Close file
f.close()