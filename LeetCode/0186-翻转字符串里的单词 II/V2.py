""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    先用"".join(s)将s变为string
    再用.split()将s变为单词列表
    [::-1]表示将列表中的单词反转
    外层用" ".join()将反转后的列表变为字符串
    最外层list()将字符串按字符转为列表
注意：
    s[:]而不是s,因为要在原地址进行操作
结果：
    执行用时 : 272 ms, 在所有 Python3 提交中击败了57.4%的用户
    内存消耗 : 17.5 MB, 在所有 Python3 提交中击败了100%的用户
"""

class Solution:
    def reverseWords(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        s[:] = list(" ".join("".join(s).split()[::-1]))
        return s


if __name__ == "__main__":
    s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    answer = Solution().reverseWords(s)
    print(answer)