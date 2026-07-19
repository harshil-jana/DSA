# Pattern-1: Rectangular Star Pattern

# *****
# *****
# *****
# *****
# *****

# def pattern1(n):
#     for i in range(1,n+1):   #Outer loop for number of rows
#         print("*****")

# pattern1(5)


# ------------------------------

# Pattern-2: Right-Angled Triangle Pattern

# *
# **
# ***
# ****
# *****


# def pattern2(n):
#     for i in range(1,n+1): #Outer loop for number of rows
#         print("*" * i )

# pattern2(5)


# ------------------------------

# Pattern - 3: Right-Angled Number Pyramid

# 1
# 12
# 123
# 1234
# 12345

# class Solution:
#     def pattern3(self, n):    
#         for i in range(1,n+1):    #Outer loop for number of rows
#             for j in range(1,i+1):  #Inner Loop : The series of numbers to printed 
#                 print(j,end = "")  #end = "" for getting the iteration output in a single line
#             print("")             #Go to new line

# sol = Solution()
# sol.pattern3(5)


# ------------------------------

# Pattern - 4: Right-Angled Number Pyramid - II

# 1
# 22
# 333
# 4444
# 55555

# class Solution:
#     def pattern4(self, n):
#         for i in range(1,n+1):   #Outer loop for number of rows
#             for j in range(1,i+1):  #Inner Loop : Number of times "i" should be printed
#                 print(i ,end = "")  #end = "" for getting the iteration output in a single line
#             print("")    #Go to new line

# sol = Solution()
# sol.pattern4(5)



# ------------------------------

# Pattern-5: Inverted Right Pyramid

# *****
# ****
# ***
# **
# *

# class Solution:
#     def pattern5(self, n):
#         for i in range(1,n+1):   #Outer loop for number of rows
#             print("*" * (n-i+1))   #Reversing = Logic

# sol = Solution()
# sol.pattern5(5)



# ------------------------------

# Pattern - 6: Inverted Numbered Right Pyramid

# 12345
# 1234
# 123
# 12
# 1

# class Solution:
#     def pattern6(self, n):
#         for i in range(n,0,-1):   #Outer loop for number of rows
#             for j in range(1,i+1):
#                 print(j, end = "")   #Reversing = Logic
#             print("")

# sol = Solution()
# sol.pattern6(5)



# ------------------------------

# Pattern - 7: Star Pyramid

#     *    
#    ***   
#   *****
#  *******
# *********

# class Solution:
#     def pattern7(self, n):
#         for i in range(0,n):   #Outer loop for number of rows
#             print(" " * (n-i-1), end = "")
#             print("*" * (2*i+1), end="")
#             print("")
           

# sol = Solution()
# sol.pattern7(5)


# ------------------------------

# Pattern - 8: Inverted Star Pyramid

# *********
#  *******
#   *****
#    ***
#     *

# class Solution:
#     def pattern8(self, n):
#         for i in range(n,0,-1):   #Outer loop for number of rows
#             print(" " * (n-i), end = "")
#             print("*" * (2*i-1), end="")
#             print("")
           

# sol = Solution()
# sol.pattern8(5)


# ------------------------------

# Pattern - 9: Diamond Star Pattern

#     *    
#    ***   
#   *****
#  *******
# *********
# *********
#  *******
#   *****
#    ***
#     *

# class Solution:
#     def pattern9(self, n):
#         for i in range(0,n):   #Outer loop for number of rows
#             print(" " * (n-i-1), end = "")
#             print("*" * (2*i+1), end="")
#             print("")

#         for i in range(n,0,-1):
#             print(" " * (n-i), end="" )
#             print("*" * (2*i-1), end="")
#             print("")
           

# sol = Solution()
# sol.pattern9(4)


# ------------------------------

# Pattern - 10: Half Diamond Star Pattern

# *
# **
# ***
# ****
# *****
# ****
# ***
# **
# *

# class Solution:
#     def pattern10(self, n):
#         for i in range(1,n+1):
#             print("*" * i)
#         for i in range(n-1,0,-1):
#             print("*" * i)
           

# sol = Solution()
# sol.pattern10(4)


#---------------------------
# Single Loop


# class Solution:
#     def pattern10(self, n):
#         for i in range(0,2*n-1):
#             if i<n:
#                 print("*" * (i+1))
#             else:
#                 print("*" * (2*n-i-1))

           

# sol = Solution()
# sol.pattern10(4)


# ------------------------------

# Pattern - 11: Binary Number Triangle Pattern

# 1
# 01
# 101
# 0101
# 10101

# class Solution:
#     def pattern11(self, n):
#         for i in range(0,n+1):
#             if i % 2 == 0:
#                 start = 1
#             else:
#                 start = 0

#             for j in range(i+1):
#                 print(start, end="")
#                 start = 1- start
#             print("")
# sol = Solution()
# sol.pattern11(4)


# ------------------------------

# Pattern - 12: Number Crown Pattern

# 1      1
# 12    21
# 123  321
# 12344321

class Solution:
    def pattern12(self, n):
        for i in range(1,n+1):
            for j in range(1,i+1):  #Left Half
                print(j, end="")
                
            print(" " * (2*(n-i)), end="")    #Spaces

            for j in range(i,0,-1):
                print(j, end="")

            print("")

sol = Solution()
sol.pattern12(5)