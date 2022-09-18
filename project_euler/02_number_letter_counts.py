# Problem 17: Number letter counts

# If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

# If all the numbers from 1 to given limit inclusive were written out in words, how many letters would be used?

# Note: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

numbers = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
def count_letters(x: str, arr: str)-> int:
    sum = 0
    for i in range(len(arr)):
        if x == arr[i]:
            sum += 1
    return sum


count_letters('a', ['a', 'kf'])