def x(sen: str ) -> str: 

    return "".join(map(str.capitalize, sen.split()))

# For testing.

txt = str(input("Enter a sentence: "))
print(x(txt))