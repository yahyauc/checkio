def number_length(value: int) -> int:
    text = str(value)
    lenght = len(text)
    return lenght

# For testing.
num = int(input("Enter a number : "))
print(number_length(num))
