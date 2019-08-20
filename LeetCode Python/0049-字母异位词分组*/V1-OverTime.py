""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    用Counter+双循环去判断每一个单词是否有异位词
    若存在，则将结果添加到异位词后面
结果：
    第97个测试用例超时
"""

from collections import Counter
class Solution:
    def groupAnagrams(self, strs):
        res = []
        if len(strs) == 0:
            return res
        res.append([strs[0]])
        if len(strs) == 1:
            return res
        for s in strs[1:]:
            for i in range(len(res)):
                add = False
                if Counter(res[i][0]) == Counter(s):
                    res[i].append(s)
                    add = True
                    break
            if add == False:
                res.append([s])
        return res



if __name__ == "__main__":
    strs = ["1","1","1"]
    answer = Solution().groupAnagrams(strs)
    print(answer)
