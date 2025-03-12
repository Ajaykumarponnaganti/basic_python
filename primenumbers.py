# Function to check if a number is prime

def is_prime(num):
    if num < 2:
        return False  
    for i in range(2, int(num ** 0.5) + 1): 
        if num % i == 0:
            return False
    return True  

def find_primes(start, end):
    print(f"Prime numbers between {start} and {end} are:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")  
    print()  

start = int(input("Enter the start number: "))
end = int(input("Enter the end number: "))

find_primes(start, end)
