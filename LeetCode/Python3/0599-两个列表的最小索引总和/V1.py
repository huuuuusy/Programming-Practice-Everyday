""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    用字典，注意本题的写法简洁巧妙
结果：
    执行用时 : 348 ms, 在所有 Python3 提交中击败了22.45%的用户
    内存消耗 : 14 MB, 在所有 Python3 提交中击败了5.52%的用户
"""

class Solution:
    def findRestaurant(self, list1, list2):
        # 用字典保存set(list1)与set(list2)的交集元素的下标和
        d = {x: list1.index(x)+list2.index(x) for x in set(list1) & set(list2)}
        # 返回d中下标值最小的键
        return [x for x in d if d[x] == min(d.values())]

if __name__ == "__main__":
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    answer = Solution().findRestaurant(list1, list2)
    print(answer)