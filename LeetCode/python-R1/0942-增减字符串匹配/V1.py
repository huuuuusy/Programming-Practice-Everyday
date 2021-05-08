""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37.1
工具： python == 3.7.3
"""

"""
思路:
    list＋str转换类型法
结果：
    执行用时 : 104 ms, 在所有 Python3 提交中击败了76.94%的用户
    内存消耗 : 15.2 MB, 在所有 Python3 提交中击败了5.54%的用户
"""

class Solution:
    def diStringMatch(self, S):
        target = [i for i in range(len(S)+1)]
        res = []
        for s in list(S):
            # 如果是增加，则从target选出目前最小的元素
            if s == 'I':
                res.append(target[0])
                target.pop(0)
            # 如果是减小，则从target选出目前最大的元素
            else:
                res.append(target[-1])
                target.pop()
        # 将仅剩的元素添加到末尾
        res.append(target[0])
        return res


if __name__ == "__main__":
    S = "DDI"
    answer = Solution().diStringMatch(S)
    print(answer)


