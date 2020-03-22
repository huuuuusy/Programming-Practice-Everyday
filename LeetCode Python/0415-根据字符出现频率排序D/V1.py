""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    巧妙的思路，用字典容易想，但是将字典元素用lambda函数按顺序排序不好想
    最后res += v*k也很巧妙
    需要再理解一下l的转换公式，参考：https://www.runoob.com/python/python-func-sorted.html
结果：
    执行用时 : 60 ms, 在所有 Python3 提交中击败了91.7%的用户
    内存消耗 : 13.6 MB, 在所有 Python3 提交中击败了88.89%的用户
"""
def get_keys(d, value):
    return [k for k,v in d.items() if v == value]
    
class Solution:
    def frequencySort(self, s):
        res = ''
        map = {}
        for i in s :
            if i not in map:
                map[i] = 1
            else :
                map[i] += 1
        # 将字典的元素按照key进行反向排序
        l = sorted(map.items(), key=lambda x: x[1], reverse=True)
        for v , k in l:
            res += v*k
        return res

if __name__ == "__main__":
    s = "tree"
    answer = Solution().frequencySort(s)
    print(answer)