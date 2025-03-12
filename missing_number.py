def find_missing_number(arr, n):
    full_set = set(range(1, n + 1))   
    arr_set = set(arr)  
    missing_number = full_set - arr_set  
    return missing_number.pop() 

n = int(input("Enter the total number of elements (n): "))
arr = list(map(int, input(f"Enter {n-1} numbers separated by space: ").split()))

missing_number = find_missing_number(arr, n)
print(f"The missing number is: {missing_number}")

