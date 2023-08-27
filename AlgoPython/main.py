# https://www.youtube.com/watch?v=fW_OS3LGB9Q

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

# --------------------- Bubble sort

# def bubble_optimized(A):
#     iterations = 0
#     for i in range(len(A)):
#         for j in range(len(A)-i-1):
#             iterations += 1
#             if A[j] > A[j+1]:
#                 A[j], A[j+1] = A[j+1], A[j]
#     return A, iterations

# A = [9,8,7,6,5,4,3,2,1]
# print(bubble_optimized(A))

# --------------------- Bubble sort - unoptimized

# def swap(A, i, j):
#     temp = A[i]
#     A[i] = A[j]
#     A[j] = temp

# def bubble_sort_un_op(A):
#     iterations = 0
#     for i in A:
#         for j in range(len(A)-1):
#             iterations += 1
#             if A[j] > A[j+1]:
#                 swap(A, j, j+1)
#     return A, iterations

# A = [9,8,7,6,5,4,3,2,1]
# print(bubble_sort_un_op(A))

# --------------------- Insertion sort

# def insert_sort(A):
#     for j in range(1, len(A)):
#         key = A[j]
#         i = j - 1
#         while i >= 0 and A[i] > key:
#             A[i+1] = A[i]
#             i -= 1
#         A[i+1] = key
#     return A

# A = [9,8,7,6,5,4,3,2,1]
# print(insert_sort(A))

# --------------------- Linked List (linked by nodes)

# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None

# class LinkedList:

#     def traversal(self):
#         first = self.head
#         while first:
#             print(first.data)
#             first = first.next

#     def insert_new_head(self, new_data):
#         new_node = Node(new_data)
#         new_node.next = self.head
#         self.head = new_node

#     def search(self, x):
#         temp = self.head
#         while temp is not None:
#             if temp.data == x:
#                 return True
#             temp = temp.next
#         return False
    
#     def delete_node(self, data):
#         temp = self.head
#         while temp is not None:
#             if temp.data == data:
#                 break
#             prev = temp
#             temp = temp.next
#         prev.next = temp.next

#     def delete_tail(self):
#         temp = self.head
#         while temp.next.next is not None:
#             temp = temp.next
#         temp.next = None

# family = LinkedList()
# family.head = Node("Bob")
# wife = Node("Amy")
# first_kid = Node("Max")
# second_kid = Node("Jenny")

# family.head.next = wife
# wife.next = first_kid
# first_kid.next = second_kid

# # family.traversal()
# family.insert_new_head("Dave")
# family.delete_node("Bob")
# family.delete_tail()
# family.traversal()
# # print(family.search("Bob"))

# --------------------- Hash Table ( associative array, hash function, key/value pairs, collision, chaining) just talked about in video @53 mins
# practice with the Robin-Karp algorithm

# some problems are complet, so solve them in smaller bits (divide and conquer method)
# recursion can work, but may over utilize memory, so you may need to save into Data Structure: stack, queue, Priority Queue...
# consider Breadth First Search (BFS) and Branch and Bound method for fuction optimization

# --------------------- Merge Sort

# example 1 - brute force

# A = [-5,-23,5,0,23,-6,23,67]
# C = []

# while A:
#     minimum = A[0]
#     for x in A:
#         if x < minimum:
#             minimum = x
#     C.append(minimum)
#     A.remove(minimum)

# print(C)

# example 2 - merge sort (2 halves need to be sorted for this to work)

# def merging(left, right):
#     C = []
#     while min(len(left), len(right)) > 0:
#         if left[0] > right[0]:
#             insert = right.pop(0)
#             C.append(insert)
#         elif left[0] < right[0]:
#             insert = left.pop(0)
#             C.append(insert)
#     if len(left) > 0:
#         for i in left:
#             C.append(i)
#     if len(right) > 0:
#         for i in right:
#             C.append(i)
#     return C

# left = [2,5,6,10]
# right = [3,4,12,20]

# print(merging(left, right))

# example 3 - sort recursively top down method

# def sortArray(A):
#     if len(A) <= 1:
#         return A
#     middle = len(A) // 2
#     left = sortArray(A[:middle])
#     right = sortArray(A[middle:])
#     merged = []
#     while left and right:
#         if left[0] < right[0]:
#             merged.append(left.pop(0))
#         else:
#             merged.append(right.pop(0))
#     merged.extend(right if right else left)
#     return merged

# print (sortArray([2,5,-6,10,3,4,-12,20]))

# example 4 - sort recursively bottom up method

# class Solution(object):
#     def sortArray(self, nums):
#         #iterative merge sort using sorted
#         mid = len(nums)//2
#         left = nums[:mid]
#         right = nums[mid:]
#         C = []
#         while min(len(left), len(right)) > 0:
#             if left[0] > right[0]:
#                 insert = right.pop(0)
#                 C.append(insert)
#             elif left[0] < right[0]:
#                 insert = left.pop(0)
#                 C.append(insert)
#         if len(left) > 0:
#             for i in left:
#                 C.append(i)
#         if len(right) > 0:
#             for i in right:
#                 C.append(i)
#         return C
    
# matrix multiplecation (m = rows, n = columns)
# nieve method = O(n^3) (numPy optimezed software package)
# 2X2 matrix "X"
# X = [[1,2],
#     [2,3]]
# # 2X2 matrix "Y"
# Y = [[2,3],
#     [3,4]]
# # 2X2 matrix of "0", which added to our answer, gives the answer
# result = [[0,0],
#         [0,0]]

# # iterate through rows of X
# for i in range(len(X)):
#     # iterate through columns of Y
#     for j in range(len(Y[0])):
#         # iterate through rows of Y
#         for k in range(len(Y)):
#             result[i][j] += X[i][k] * Y[k][j]

# for end in result:
#     print(end)

# Iteration
# import numpy as np

# x = np.array([[1,2],[2,3]])
# y = np.array([[2,3],[3,4]])

# def strassen_iter(x,y):

#     # Splitting the matrices into quadrants.  See graphic
#     a,b,c,d = x[0,0], x[0,1], x[1,0], x[1,1]
#     e,f,g,h = y[0,0], y[0,1], y[1,0], y[1,1]

#     # Computing the 7 products
#     p1 = a * (f-h)
#     p2 = (a+b) * h
#     p3 = (c+d) * e
#     p4 = d * (g-e)
#     p5 = (a+d) * (e+h)
#     p6 = (b-d) * (g+h)
#     p7 = (a-c) * (e+f)

#     # Computing the values of the 4 quadrants of the final matrix c
#     c1 = p5 + p4 - p2 + p6
#     c2 = p1 + p2
#     c3 = p3 + p4
#     c4 = p1 + p5 - p3 - p7

#     return np.array([[c1,c2],[c3,c4]])

# print(strassen_iter(x,y))

#  lesson 4
# --------------------- Assign Mice to Holes (Greedy Algorithm)
# def assignHole(mice, holes):
#     # Base - num of mice and holes are equal
#     if len(mice) != len(holes):
#         return "Number of mice and holes not the same"
#     # Sort the lists
#     mice.sort()
#     holes.sort()
#     #  Finding max difference between mice and holes
#     max_diff = 0
#     for i in range(len(mice)):
#         if max_diff < abs(mice[i] - holes[i]):
#             max_diff = abs(mice[i] - holes[i])
#     return max_diff
# mice = [4,-4,2]
# holes = [4,0,5]
# #  the required answer is returned from the function
# min_time = assignHole(mice, holes)
# print("The last mouse gets into the hole in time:", min_time)


# --------------------- Kids with Greatest Candies (Greedy Algorithm)

# --------------------- Fractional knapsack (Greedy Algorithm) - Bounded Knapsack Problem
# weight = [30,50,10,70,40]
# value = [150,100,90,140,120]
# capacity = 150

# def fractional_knapsack(value, weight, capacity):
#     items = list(range(len(value)))
#     print("Items:", items)
#     ratio = [v//w for v,w in zip(value, weight)]
#     print("Ratios:", ratio)
#     srt_ratios = sorted(ratio, reverse=True)
#     print("Sorted Ratios:", srt_ratios)
#     items.sort(key=lambda i: ratio[i], reverse=True)
#     # print("Sorted Items:", items)

#     max_value = 0
#     fractions = [0] * len(value)
#     print(fractions)
#     for i in items:
#         if weight[i] <= capacity:
#             fractions[i] = 1
#             max_value += value[i]
#             capacity -= weight[i]
#         else:
#             fractions[i] = capacity // weight[i]
#             max_value += value[i] * capacity // weight[i]
            
#     return max_value
# print(fractional_knapsack(value, weight, capacity))

#  @1:31:50
