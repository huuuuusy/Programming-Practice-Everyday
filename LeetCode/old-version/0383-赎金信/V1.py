""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.39
工具： python == 3.7.3
"""

"""
思路:
    直接求解
结果：
    执行用时 : 48 ms, 在所有 Python3 提交中击败了98.50%的用户
    内存消耗 : 13.9 MB, 在所有 Python3 提交中击败了5.17%的用户
"""
class Solution:
    def canConstruct(self, ransomNote, magazine):
        for num in set(ransomNote):
            if magazine.count(num) < ransomNote.count(num):
                return False
        return True


if __name__ == "__main__":
    ransomNote = "bg"
    magazine = "efjbdfbdgfjhhaiigfhbaejahgfbbgbjagbddfgdiaigdadhcfcj"
    answer = Solution().canConstruct(ransomNote, magazine)
    print(answer)