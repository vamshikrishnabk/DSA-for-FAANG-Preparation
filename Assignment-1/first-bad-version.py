# You are a product manager and currently leading a team to develop a new product. Unfortunately, 
# the latest version of your product fails the quality check. Since each version is developed based on the previous version, 
# all the versions after a bad version are also bad. Suppose you have n version and you want to find out the first bad one, 
# which causes all the following ones to be bad. Also, talk about the time complexity of your code.
# Test Cases:
# Input: [0,0,0,1,1,1,1,1,1]
# Output: 3
# Explanation: 0 indicates a good version and 1 indicates a bad version. So, the index of the first 1 is at 3. Thus, the output is 3



# Time Complexity - O(n)
# def checkBadVersion(arr):
#     for i in range(len(arr)):
#         if arr[i] == 1:
#             return i


#Time Complexity - O(logn)
def checkBadVersion(arr):
    left=0
    right=len(arr)-1
    while(left <= right):
        mid=left + (right-left)//2
        if arr[mid] == 1:
            if mid !=0:
                if arr[mid-1] == 0:
                    return mid
                else:
                    right=mid-1
            else:
                return mid
        else:
            left=mid+1
    return -1

## Driver code
arr=[0,0,0,1,1,1,1,1,1]

## function calling
result=checkBadVersion(arr)
print(result)


