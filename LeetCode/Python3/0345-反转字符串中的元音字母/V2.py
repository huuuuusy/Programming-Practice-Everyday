""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    对撞指针，只需要一轮循环即可完成替换
结果：
    执行用时 : 92 ms, 在所有 Python3 提交中击败了56.07%的用户
    内存消耗 : 14.8 MB, 在所有 Python3 提交中击败了16.46%的用户
"""

class Solution:
    def reverseVowels(self, s):
        vowels_list = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        i, j = 0, len(s)-1
        ss = list(s)
        while i < j:
            if ss[i] not in vowels_list:
                i += 1
                continue
            if ss[j] not in vowels_list:
                j -= 1
                continue
            if i < j: 
                ss[i], ss[j] = ss[j], ss[i]
            i += 1
            j -= 1
        d = ''
        return d.join(ss)

        
if __name__ == "__main__":
    s = "hello"
    answer = Solution().reverseVowels(s)
    print(answer)