# ----------------- Factorials - Recursive and Iterative

# def iterative_factorial(n):
#     fact = 1
#     for i in range(2, n+1):
#         fact *= i
#     return fact
# print(iterative_factorial(5))

# def recursive_factorial(n):
#     if n == 1:
#         return n
#     else:
#         temp = recursive_factorial(n-1)
#         return temp * n
# print(recursive_factorial(5))

# ----------------- Permutations - Recursive

# def permute(string, pocket=""):
#     if len(string) == 0:
#         print(pocket)
#     else:
#         for i in range(len(string)):
#             letter = string[i]
#             front = string[0:i]
#             back = string[i+1:]
#             together = front + back
#             permute(together, letter+pocket)

# print(permute("ABC", ""))

# ----------------- Permutations - Iterative

# from math import factorial
# def permutations (str):
#     for p in range(factorial(len(str))):
#         print(''.join(str))
#         i = len(str) - 1
#         while i > 0 and str[i -1] > str[i]:
#             i -= 1
#         str[i:] = reversed(str[i:])
#         if i > 0:
#             q = i 
#             while str[i - 1] > str[q]:
#                 q += 1
#             temp = str[i - 1]
#             str[i - 1] = str[q]
#             str[q] = temp

# s = 'abc'
# s = list(s)
# permutations(s)

# ----------------- N-Queens - Recursive

# def n_queens(n):
#     board = [-1] * n
#     return n_queens_helper(board, 0)
# print(n_queens(4))

# Linear search

# def search(arr, target):
#     for i in range(len(arr)):

#         if arr [i] == target:
#             return i
        
# arr = [2,5,8,9,10,16,22]
# target = 10

# print(search(arr, target))

# ----------------------- Iterative Binary search

# def binary_itr(arr, start, end, target):
#     while start <= end:
#         mid = (start + end) // 2
#         if arr[mid] < target:
#             start = mid + 1
#         elif arr[mid] > target:
#             end = mid - 1
#         else:
#             return mid
#     return -1
#     # return start

# arr = [2,5,8,10,16,22,25]
# target = 10

# result = binary_itr(arr, 0, len(arr)-1, target)

# if result != -1:
#     print("Element is present at index %d" % result)
# else:
#     print("Element is not present in array")

# --------------------- Recursive Binary search

# def binary_recur(arr, start, end, target):
#     if end >= start:
#         mid = start + end - 1 // 2

#         if arr[mid] < target:
#             binary_recur(arr, mid +1,end,target)

#         elif arr[mid] > target:
#             binary_recur(arr, start, mid -1, target)
#         else:
#             return mid
#     else:
#         return -1
#     # return start

# arr = [2,5,8,10,16,22,25]
# target = 10

# result = binary_recur(arr, 0, len(arr) -1, target)

# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in array")
    
# def binary_recur(arr, start, end, target):
#     if end >= start:
#         mid = (start + end) // 2  # Corrected parentheses here

#         if arr[mid] < target:
#             return binary_recur(arr, mid + 1, end, target)  # Return the result of the recursive call

#         elif arr[mid] > target:
#             return binary_recur(arr, start, mid - 1, target)  # Return the result of the recursive call
#         else:
#             return mid
#     else:
#         return -1

# arr = [2, 5, 8, 10, 16, 22, 25]
# target = 10

# result = binary_recur(arr, 0, len(arr) - 1, target)

# if result != -1:
#     print("Element is present at index", str(result))
# else:
#     print("Element is not present in the array")
