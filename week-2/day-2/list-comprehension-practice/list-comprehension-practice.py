# [Expression for item in iterable if condition]
# 1.
nums = [1, 2, 3, 4, 5]
doubled_nums = [num * 2 for num in nums]
print(doubled_nums)

# 2.
nums = [1, 2, 3, 4, 5]
even_nums = [num for num in nums if num % 2 == 0]
print(even_nums)

# 3.
words = ["cat", "dog", "elephant", "ox"]
words_len = [len(word) for word in words]
print(words_len)

# 4.
squared = [x ** 2 for x in range(1, 11)]
print(squared)

# 5
words = ["cat", "dog", "elephant", "ox"]
long_words = [word for word in words if len(word) > 3]
print(long_words)

# 6.
s = "Hello World"
upper_case = [char.upper() for char in s]
print(upper_case)

# 7.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
div_3 = [num for num in nums if num % 3 == 0]
print(div_3)

# 8.
s = "Hello World"
vowels = ('a', 'e', 'i', 'o', 'u')
vowel_check = [char for char in s.lower() if char in vowels]
print(vowel_check)

# 9.
list_of_tuples = [(x, x ** 2) for x in range(1, 6)]
print(list_of_tuples)

# 10.
nums = [-4, -2, 0, 3, 7]
no_negatives = [0 if num < 0 else num for num in nums]
print(no_negatives)
