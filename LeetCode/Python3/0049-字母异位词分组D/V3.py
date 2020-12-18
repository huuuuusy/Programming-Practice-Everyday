""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    用长度为26的矩阵存储每个字母出现的次数
    将每个单词转化为一串数字编码
    构建字典，key是数字编码，value是单词列表
    最后输出字典的value
结果：
    执行用时 : 160 ms, 在所有 Python3 提交中击败了51.85%的用户
    内存消耗 : 18 MB, 在所有 Python3 提交中击败了5.13%的用户
"""

import collections
class Solution:
    def groupAnagrams(self, strs):
        ans = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                # 用ord()得到ASCII码，然后判断字母在字母表的位置
                count[ord(c) - ord('a')] += 1
            ans[tuple(count)].append(s)
        return list(ans.values())



if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat",'apple']
    answer = Solution().groupAnagrams(strs)
    print(answer)
