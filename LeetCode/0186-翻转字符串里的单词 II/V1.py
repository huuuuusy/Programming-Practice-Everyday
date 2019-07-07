""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    先用index记录分隔符的位置
    然后在原数组基础上添加翻转后的单词
    最后把前面的字符串删除
结果：
    执行用时 : 2744 ms, 在所有 Python3 提交中击败了7.14%的用户
    内存消耗 : 17.7 MB, 在所有 Python3 提交中击败了100%的用户
"""

class Solution:
    def reverseWords(self, s):
        """
        Do not return anything, modify s in-place instead.
        """
        # index负责存储空白字符的位置
        index = [-1]
        for i in range(len(s)):
            if s[i] == " ":
                index.append(i)
        # 在原数组后面添加前一个单词
        for i in range(len(index)-1):
            s.append(" ")
            left = index[-(i+2)]
            right = index[-(i+1)]
            for j in range(left+1, right):
                s.append(s[j])
        # 最后推出前面的原数组
        for i in range(index[-1]+1):
            s.pop(0)
        return s


if __name__ == "__main__":
    s = ["t","h","e"," ","s","k","y"," ","i","s"," ","b","l","u","e"]
    answer = Solution().reverseWords(s)
    print(answer)