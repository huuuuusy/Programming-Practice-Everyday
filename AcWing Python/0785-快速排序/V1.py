""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

def quick_sort(nums, left, right):
    if left >= right:
        return -1
    i = left
    j = right
    mid = nums[(left + right) >> 1]
    while i < j:
        while nums[i] < mid:
            i += 1
        while nums[j] > mid:
            j -= 1 
        if i < j:
            nums[i], nums[j] = nums[j], nums[i]
    quick_sort(nums, left, j)
    quick_sort(nums, j+1, right)
    return nums       
        

if __name__ == "__main__":
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(input())
    answer = quick_sort(nums, 0, n-1)
    for i in range(n):
        print(answer[i])      