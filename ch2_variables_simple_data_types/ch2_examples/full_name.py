# p.21 example 1: using variables in strings
# example 1 output: ada lovelace
# this is the first example of a formatted string, or f-string.
# f-strings let you put the value of Python expressions 
# into a string by using the syntax f"{var_name}".
# f-strings allow you to make dynamic strings.

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)

# p.21 example 2: f-string with a method
# example 1 output: Hello, Ada Lovelace
first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(f"Hello, {full_name.title()}!")