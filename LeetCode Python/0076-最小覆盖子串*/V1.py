""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.39
工具： python == 3.7.3
"""

"""
思路：
    滑动窗口
参考：
    https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/solution/hua-dong-chuang-kou-by-powcai/
结果：
    执行用时 : 48 ms, 在所有 Python3 提交中击败了91.03%的用户
    内存消耗 : 13.3 MB, 在所有 Python3 提交中击败了47.28%的用户
"""

class Solution:
    def minWindow(self, s, t):
        from collections import defaultdict
        lookup = defaultdict(int) # 存储当前需要检索的字母个数
        for alp in t: # 先将t中的字母存入lookup；t中的字母初始个数是1,则其他字母初始个数为0
            lookup[alp] += 1
        start = 0 # 滑动窗口的起始
        end = 0
        min_len = float('inf') 
        counter = len(t) # counter用来统计t中的字母是否都在窗口中，若都在，则counter=0
        res = ""
        while end < len(s):
            if lookup[s[end]] > 0: # 如果lookup中s[end]的值大于0,说明是t中的字母，此时窗口中包含t中的一个字母，所以counter可以减一
                counter -= 1
            lookup[s[end]] -= 1 # 将lookup中当前字母的个数减一，lookup中存储的是该字母有几个出现在窗口中，和初始值的差值表示出现的个数
            end += 1
            while counter == 0: # 此时表明t中所有字母均在窗口中
                if min_len > end - start: # 更新min_len
                    min_len = end - start
                    res = s[start:end] # 更新res
                if lookup[s[start]] == 0:
                    counter += 1
                lookup[s[start]] += 1 # 移动窗口起点
                start += 1
        return res
            


if __name__ == "__main__":
    s = "ADOBECODEBANC"
    t = "ABC"
    answer = Solution().minWindow(s, t)
    print(answer)
