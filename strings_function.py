name = "sumit"

print(len(name))

print(name.endswith("mit"))
print(name.startswith("su"))
print(name.capitalize())
print(name.find("it"))
print(name.replace("s","t"))
print(name.upper())        # Converts all characters to uppercase
print(name.lower())        # Converts all characters to lowercase
print(name.title())        # Converts the first character of each word to uppercase
print(name.isalpha())      # Checks if all characters in the string are alphabetic
print(name.isdigit())      # Checks if all characters in the string are digits
print(name.islower())      # Checks if all characters are lowercase
print(name.isupper())      # Checks if all characters are uppercase
print(name.strip())        # Removes any leading/trailing whitespace
print(name.center(10))     # Centers the string within a field of width 10
print(name.count("i"))     # Counts occurrences of substring "i"
print(name.index("u"))     # Returns the index of first occurrence of "u"
