""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    最大的难度是如何理解题意
    奇数位和偶数位上的所有字符分别一致，就是一组，
    如abcde、cdabe，两者奇数位上均是a/c/e，偶数位上都是b/d，最后都能通过有限次的交换得到对方
结果：
    执行用时 : 68 ms, 在所有 Python3 提交中击败了61.4%的用户
    内存消耗 : 13.9 MB, 在所有 Python3 提交中击败了5.40%的用户
"""

class Solution:
    def numSpecialEquivGroups(self, A):
        res = set()
        for sub in A:
            new_sub = "".join(sorted(sub[::2]) + sorted(sub[1::2]))
            res.add(new_sub)
        return len(res)

if __name__ == "__main__":
    A = ["abc","acb","bac","bca","cab","cba"]
    answer = Solution().numSpecialEquivGroups(A)
    print(answer)