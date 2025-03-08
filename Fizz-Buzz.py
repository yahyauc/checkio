def checkio(num: int) -> str:
    if num % 3 == 0 and num % 5 ==0:
        return "Fizz Buzz"
    elif num % 3 != 0 and num % 5 ==0:
        return "Buzz"
    elif num % 3 == 0 and num % 5 !=0:
        return "Fizz"
    else:
        return str(num)
    
# For testing.
num = int(input("Enter a number : "))
print(checkio(num))