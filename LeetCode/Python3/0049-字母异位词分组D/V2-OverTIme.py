""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    在V1的基础上加了字典对输入进行长度分类，在每一类里循环判断
    速度比V1快一些，但仍然超时
结果：
    第100个测试用例超时
"""

from collections import Counter
class Solution:
    def groupAnagrams(self, strs):
        res = []
        if len(strs) == 0:
            return res
        if len(strs) == 1:
            return [strs]
        d = {}
        for s in strs:
            d[len(s)] = d.get(len(s),[]) + [s]
        for key, value in d.items():
            res_part = [[value[0]]]
            if len(value) > 1:
                for item in value[1:]:
                    for i in range(len(res_part)):
                        add = False
                        if Counter(res_part[i][0]) == Counter(item):
                            res_part[i].append(item)
                            add = True
                            break
                    if add == False:
                        res_part.append([item])
            res.extend(res_part)
        return res



if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat",'apple']
    answer = Solution().groupAnagrams(strs)
    print(answer)
