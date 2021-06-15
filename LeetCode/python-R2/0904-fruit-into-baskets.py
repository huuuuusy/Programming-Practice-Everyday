"""
在一排树中，第 i 棵树产生 tree[i] 型的水果。
你可以从你选择的任何树开始，然后重复执行以下步骤：

把这棵树上的水果放进你的篮子里。如果你做不到，就停下来。
移动到当前树右侧的下一棵树。如果右边没有树，就停下来。
请注意，在选择一颗树后，你没有任何选择：你必须执行步骤 1，然后执行步骤 2，然后返回步骤 1，然后执行步骤 2，依此类推，直至停止。

你有两个篮子，每个篮子可以携带任何数量的水果，但你希望每个篮子只携带一种类型的水果。

用这个程序你能收集的水果树的最大总量是多少？


示例 1：
输入：[1,2,1]
输出：3
解释：我们可以收集 [1,2,1]。

示例 2：
输入：[0,1,2,2]
输出：3
解释：我们可以收集 [1,2,2]
如果我们从第一棵树开始，我们将只能收集到 [0, 1]。

示例 3：
输入：[1,2,3,2,2]
输出：4
解释：我们可以收集 [2,3,2,2]
如果我们从第一棵树开始，我们将只能收集到 [1, 2]。

示例 4：
输入：[3,3,3,1,2,1,1,2,3,3,4]
输出：5
解释：我们可以收集 [1,2,1,1,2]
如果我们从第一棵树或第八棵树开始，我们将只能收集到 4 棵水果树。
 
提示：
1 <= tree.length <= 40000
0 <= tree[i] < tree.length

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fruit-into-baskets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def totalFruit(self, tree):
        res = 0
        if len(set(tree)) <= 2:
            return len(tree)
        for i in range(1, len(tree)-1):
            left, right = i-1, i+1
            check_list = tree[i-1:i+2]
            
            if len(set(check_list)) == 3:
                # 当当前元素左右元素均不同时，结果是2
                res = max(res, 2)
            else:
                # 否则向左右检查
                while left > 0 and tree[left-1] in check_list:
                    left -= 1
                while right < len(tree)-1 and tree[right+1] in check_list:
                    right += 1 
                res = max(res, right-left+1)
            # print(check_list, left, right, tree[left: right+1])

        return res

if __name__ == '__main__':
    tree = [0]
    answer = Solution().totalFruit(tree)
    print(answer)