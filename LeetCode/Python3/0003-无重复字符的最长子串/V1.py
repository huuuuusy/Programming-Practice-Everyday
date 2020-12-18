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
    def lengthOfLongestSubstring(self, s):
        from collections import defaultdict
        lookup = defaultdict(int) # lookup以字典的形式存储每次滑动窗口中元素的个数
        start = 0 # 滑窗起点
        end = 0 # 滑窗终点
        max_len = 0 # 滑窗最大长度
        counter = 0 # 是否需要移动start的flag
        while end < len(s):
            if lookup[s[end]] > 0: # 如果当前窗口结尾的元素已经在字典中出现，将flag变为true
                counter += 1 
            lookup[s[end]] += 1 # 窗口向后移动
            end += 1
            while counter > 0: # 当flag为true时，此时需要移动窗口的起点
                if lookup[s[start]] > 1: # 向后移动窗口的起点，当当前窗口起点已经在字典中出现时，flag变为False
                    counter -= 1
                lookup[s[start]] -= 1 # 向后移动起点
                start += 1
            max_len = max(max_len, end - start)
        return max_len



if __name__ == "__main__":
    s = "abcabcbb"
    answer = Solution().lengthOfLongestSubstring(s)
    print(answer)
