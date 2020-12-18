""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： python == 3.7.3
"""

"""
思路:
    防御式编程：
        正常思路是中间部分只要出现3个0即可种花，两边需要特殊讨论
        防御式思想是将两边各补一个0,这样两边的情况和中间相同，无需单独讨论；对于所有情况，只要出现连续的3个0即可种花
结果：
    执行用时 : 196 ms, 在所有 Python3 提交中击败了81.87%的用户
    内存消耗 : 13.9 MB, 在所有 Python3 提交中击败了10.67%的用户
"""

class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        new_flowers = [0]+flowerbed+[0]
        for i in range(1, len(new_flowers)-1): # i的范围是真正种花的范围，需要去掉头尾的补零
            if new_flowers[i-1] == new_flowers[i] == new_flowers[i+1] == 0:
                new_flowers[i] = 1 # 在此处栽花
                n -= 1
        return n <= 0 # 表示可以栽完花

if __name__ == "__main__":
    flowerbed = [1,0,0,0,1]
    n = 1
    answer = Solution().canPlaceFlowers(flowerbed, n)
    print(answer)