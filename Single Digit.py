# Function to repeatedly sum digits until a single digit is obtained
def digital_root(num):
    while num >= 10: 
        sum_of_digits = 0
        while num > 0:
            sum_of_digits += num % 10 
            num //= 10  
        num = sum_of_digits  
    return num

number = int(input("Enter a number: "))

result = digital_root(number)
print(f"The single-digit sum is: {result}")
