print("------Programming Languages------")

languages = []

for i in range(5):
    lang = input("Enter a programming language: ")
    languages.append(lang)

search = input("Enter a language to search: ")

if search in languages:
    print(search, "is available in the list")
elif search not in languages:
    print(search, "is not available in the list")

# Membership operators with strings
text = "Python Programming"

print("Python" in text)
print("Java" not in text)