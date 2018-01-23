my_list = [-45, 1, 4, -4, 34, 3]
# Write code to create a new list with just the positive numbers
positive = [x for x in my_list if x >= 0]
# New list with all the numbers doubled
double = [x * 2 for x in my_list]
# New list with all the positive numbers doubled
double_positive = [x * 2 for x in my_list if x >= 0]

words = ['hello', 'world', 'python', 'kittens']
# Make new list of all strings in uppercase.
uppercase = [w.upper() for w in words]

languages = ['JS', 'C#', 'Java', 'visual Basic.NET']
# todo make new list of all strings longer than 3 letters
longer_than_three_letters = [w for w in words if len(w) > 3]
# todo make new list of all strings longer than 3 letters converted
# to uppercase ['JAVA', 'VISUAL MASIC.NET']
longer_than_three_letters_upper = [w.upper() for w in words if len(w) > 3]
lowercase_languages = [l.lower() for l in languages]
print(lowercase_languages)
