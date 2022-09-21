# Given a positive integer num, write a program that returns True if num is a perfect
# square else return False. Do not use built-in functions like sqrt. Also, talk about the time
# complexity of your code.
# Test Cases:
# Input: 16
# Output: True
# Input: 14
# Output: False



# time complexity - O(logn)
# function definition
def perfectSquare(n):
    l=1
    r=n
    while(l<=r):
        mid=l + (r-l)//2
        if mid * mid == n:
            return True
        elif mid * mid < n:
            l=mid+1
        else:
            r=mid-1
    return False
    
## Driver code
n=16

# function calling
result=perfectSquare(n)
print(result)



