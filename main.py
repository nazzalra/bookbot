file_path = "books/frankenstein.txt"
with open(file_path) as file:
    contents = file.read()
    print(contents)


def word_count(text):
    return len(text.split())

def count_letters(text):
    text = text.lower()
    count_letters = {}
    for letter in text:
        if is_alphabet(letter):
            if letter in count_letters:
                count_letters[letter] += 1
            else:
                count_letters[letter] = 1
    return count_letters

def is_alphabet(letter):
    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    return letter in alphabet

print(f"--- Begin report of {file_path} ---")
print(f"{word_count(contents)} words found in the document")

cl = count_letters(contents)
cl_list = list(cl.items())
cl_list.sort(key=lambda x:x[1], reverse=True)

for item in cl_list:
    print(f"The '{item[0]}' character was found {item[1]} times")

print("--- End Report ---")
