# Coding Challenges
 In this repository, you will find solutions to three different coding challenges.

# Prerequisites
Use Python to write down the solutions.

# Challenge 1: Converting 12-hour time to 24-hour time
Converting a 12-hour time like "8:30 am" or "8:30 pm" to 24-hour time (like "0830" or "2030") sounds straightforward, doesn't it? Let's put your skills to the test and see how you tackle it.

# Task
You are required to define a function that takes an hour (always in the range of 1 to 12, inclusive), a minute (always in the range of 0 to 59, inclusive), and a period (either "am" or "pm") as input. Your task is to return a four-digit string that encodes that time in 24-hour format.

# Notes
By convention, noon is 12:00 pm, and midnight is 12:00 am.
On the 12-hour clock, there is no 0 hour, and time just after midnight is denoted as, for example, 12:15 am. On the 24-hour clock, this translates to 0015.
# Challenge 2: Two numbers are positive
Your challenge here is to write a function that takes three integers - a, b, and c - as arguments. The function should return True if exactly two out of the three integers are positive numbers (greater than zero), and False otherwise.

Examples
(2, 4, -3) => True
(-4, 6, 8) => True
(4, -6, 9) => True
(-4, 6, 0) => False
(4, 6, 10) => False
(-14, -3, -4) => False
# Challenge 3: Consonant value
In this challenge, you'll be working with strings. Given a lowercase string that consists of alphabetic characters only (no spaces), your task is to return the highest value of consonant substrings. Consonants are any letters of the alphabet except "aeiou". Each consonant has a specific value associated with it (a = 1, b = 2, c = 3, ..., z = 26).

Examples
For the word "zodiacs", solve("zodiacs") = 26
For the word "strength", solve("strength") = 57
In the word "zodiacs," the vowels are "o" and "i". After removing them, we get "z d cs". The consonant substrings are "z," "d," and "cs," with values z = 26, d = 4, and cs = 3 + 19 = 22. The highest value is 26.

For the word "strength," the consonant substrings are "str" and "ngth," with values "str" = 19 + 20 + 18 = 57 and "ngth" = 14 + 7 + 20 + 8 = 49. The highest value is 57.

