def first_word(text: str) -> str:
    words = text.split()
    return words[0]

# For testing. 
txt = str(input("Enter a sentence: "))
print(first_word(txt))
