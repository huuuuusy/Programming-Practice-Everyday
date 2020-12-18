""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路：
    递归（不熟，参看别人的解答）
    countAndSay(n)处理的是countAndSay(n-1)的结果，思路如下：
    def countAndSay(n)
        如果n=1，返回字符串'1'
        得到countAndSay(n-1)的字符串：
            从字符串的第一位开始处理，辅助一个计数值count_num：表示重复的字符数，以及num：前一位的字符 
                如果当前位与前一位一样，那么count_num加一；
                如果当前位于前一位不一样，那么需要把前面的字符输出，即追加 count_num+num的字符串；
            最后，为了保证最后一位的信息也添加进去，增加了一步：strs+= count_num + char的操作
        最后，返回字符串strs即可。
结果：
    执行用时 : 48 ms, 在所有 Python3 提交中击败了96.50%的用户
    内存消耗 : 13 MB, 在所有 Python3 提交中击败了96.91%的用户
"""

class Solution:
    def countAndSay(self, n):
        if n == 1:
            return '1'
        # count_num负责记录重复的字符数
        count_num = 0
        # num负责记录前一位字符
        num = ''
        strs = ''
        for char in self.countAndSay(n-1):
            # 如果当前字符和前一位字符不一样
            if char != num:
                # 保存对前一个数字的统计结果（在结果中添加count_num和num)
                if count_num > 0:
                    strs += str(count_num) + num
                # 将count_num置1，因为开始重新计数（对当前数字）
                count_num = 1
                # 将当前数字传给num
                num = char
            else:
            # 当前字符和前一个字符相同，则直接将计数器加一
                count_num += 1
        # 确保最后一位也被添加进去
        strs += str(count_num) + char
        return strs

if __name__ == "__main__":
    n = 5
    answer = Solution().countAndSay(n)
    print(answer)
