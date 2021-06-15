#模板
def binarySearch(nums, target):
    # 左右都闭合的区间 [l, r]
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (left + right) >> 1
        if nums[mid] == target: return mid
        # 搜索区间变为 [mid+1, right]
        if nums[mid] < target: l = mid + 1
        # 搜索区间变为 [left, mid - 1]
        if nums[mid] > target: r = mid - 1
    return -1
#左模板
def binarySearchLeft(nums, target):
    # 左右都闭合的区间 [l, r]
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) >> 1
        if nums[mid] == target:
            # 收缩右边界
            r = mid - 1;
        # 搜索区间变为 [mid+1, right]
        if nums[mid] < target: l = mid + 1
        # 搜索区间变为 [left, mid - 1]
        if nums[mid] > target: r = mid - 1
    if l >= len(nums) or nums[l] != target: return -1
    return l

#面试题08.03解法1
class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == i:
                return nums[i]
        return -1
        
#面试题08.03解法2
class Solution:
    def findMagicIndex(self, nums: List[int]) -> int:
        return self.find_magic_index(nums, 0, len(nums) - 1)

    def find_magic_index(self, nums, left, right):
        # 未找到的符合要求的返回 -1
        if left > right:
            return -1

        # 取中间元素
        mid = left + (right - left) // 2

        # 先看是否能找到第一个魔术索引，先往左侧找
        left_ans = self.find_magic_index(nums, left, mid-1)

        # 如果左侧存在，那么返回 left_ans
        if left_ans != -1:
            return left_ans
        # 如果不存在，先比较 nums[mid] == mid
        elif nums[mid] == mid:
            return mid
        # 不存在，且 nums[mid] != mid 时，往右侧寻找
        return self.find_magic_index(nums, mid + 1, right)


#右模板
def binarySearchRight(nums, target):
    # 左右都闭合的区间 [l, r]
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) >> 1
        if nums[mid] == target:
            # 收缩左边界
            l = mid + 1;
        # 搜索区间变为 [mid+1, right]
        if nums[mid] < target: l = mid + 1
        # 搜索区间变为 [left, mid - 1]
        if nums[mid] > target: r = mid - 1
    if r < 0 or nums[r] != target: return -1
    return r
#左插入模板
def bisect_left(nums, x):
    # 手写
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] >= x: r = mid - 1
        else: l = mid + 1
    return l
#右插入模板
def bisect_right(nums, x):
    # 手写
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] <= x: l = mid + 1
        else: r = mid - 1
    return r
#leetcode 33 解法一
class Solution(object):
    def search(self, nums, target):
        if not nums:
            return -1
        n = len(nums)
        # 查找最小值的下标
        def findMin():
            begin = 0
            end = n-1
            # 如果第一个值比最后一个值小，说明整个数组是有序的
            if nums[begin]<=nums[end]:
                return begin
            while begin<=end:
                mid = begin+(end-begin)//2
                # 前一个值比后一个值大，找到了旋转点
                if mid<n-1 and nums[mid]>nums[mid+1]:
                    return mid+1
                # 中间点大于等于第一个元素，左半边是有序的，转去右边查找   
                if nums[0]<=nums[mid]:
                    begin = mid+1
                # 左边是无序的，继续在左边查找        
                else:
                    end = mid-1
            return 0
        # 正常的二分查找   
        def binarySearch(begin,end):
            while begin<=end:
                mid = begin+(end-begin)//2
                if nums[mid]>target:
                    end = mid-1
                elif nums[mid]<target:
                    begin = mid+1
                else:
                    return mid
            return -1
        # 查找最小值的下标  
        minIndex = findMin()
        # 如果最小值下标为0，说明整个数组是有序的
        if minIndex==0:
            return binarySearch(0,n-1)
        # 最终结果在[0,min_index-1]中 
        if nums[0]<=target:
            return binarySearch(0,minIndex-1)
        # 最终结果在[min_index-1,length-1]中  
        return binarySearch(minIndex,n-1)
#leetcode 33 解法2
class Solution(object):
    def search(self, nums, target):
        if not nums:
            return -1
        begin = 0
        end = len(nums)-1
        while begin<=end:
            mid = begin+(end-begin)//2
            # 找到目标值了直接返回
            if nums[mid]==target:
                return mid
            # 如果左侧是有序的  
            if nums[begin]<=nums[mid]:
                # 同时target在[ nums[begin],nums[mid] ]中
                # 那么就在这段有序区间查找
                if nums[begin]<=target<=nums[mid]:
                    end = mid-1
                # 否则去反方向查找  
                else:
                    begin = mid+1
            # 如果右侧是有序的      
            else:
                # 同时target在 ( nums[mid],nums[end] ]中
                # 那么就在这段有序区间查找
                if nums[mid]<target<=nums[end]:
                    begin = mid+1
                # 否则去反方向查找  
                else:
                    end = mid-1
        return -1

#leetcode 33 解法2变形
class Solution(object):
    def search(self, nums, target):
        if not nums:
            return -1
        begin = 0
        end = len(nums)-1
        while begin<=end:
            mid = begin+(end-begin)//2
            if nums[mid]==target:
                return mid
            if nums[mid]<=nums[end]:
                if nums[mid]<=target<=nums[end]:
                    begin = mid+1
                else:
                    end = mid-1
            else:
                if nums[begin]<=target<nums[mid]:
                    end = mid-1
                else:
                    begin = mid+1
        return -1
#leetcode 81 
class Solution:
    def search(self, nums, target):
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                return True
            while l < mid and nums[l] == nums[mid]:  # tricky part
                l += 1
            # the first half is ordered
            if nums[l] <= nums[mid]:
                # target is in the first half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # the second half is ordered
            else:
                # target is in the second half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False
#面试10.03
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            # # the first half is ordered
            if nums[l] < nums[mid]:
                # target is in the first half
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # # the second half is ordered
            elif nums[l] > nums[mid]:
                # target is in the second half
                if nums[l] <= target or target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[l] == nums[mid]:
                if nums[l] != target:
                    l += 1
                else:
                    # l 是一个备胎
                    r = l - 1
        return l if l < len(nums) and nums[l] == target else -1
#leetcode35
class Solution(object):
    def searchInsert(self, nums, target):
        if not nums:
            return -1
        begin = 0
        end = len(nums)-1
        while begin<=end:
            mid = begin+(end-begin)//2
            if nums[mid]>target:
                end = mid-1
            elif nums[mid]<target:
                begin = mid+1
            else:
                return mid
        return begin
#leetcode 34
class Solution(object):
    def searchRange(self, nums, target):
        if not nums:
            return [-1,-1]
        n = len(nums)
        # 查找第一个和最后一个元素
        def find(is_find_first):
            begin = 0
            end = n-1
            # if和elif的逻辑跟正常的二分查找一样
            while begin<=end:
                mid = begin+(end-begin)//2
                if nums[mid]>target:
                    end = mid-1
                elif nums[mid]<target:
                    begin = mid+1
                # 找到目标值了，开始定位到第一个和最后一个位置    
                else:
                    # 查找第一个和最后一个逻辑很类似，这里用一个变量标记
                    # 是查找第一个还是查找最后一个
                    if is_find_first:
                        # 如果不满足条件，缩小右边界，继续往左边查找
                        if mid>0 and nums[mid]==nums[mid-1]:
                            end = mid-1
                        else:
                            return mid
                    else:
                        # 如果不满足条件，增大左边界，继续往右边查找
                        if mid<n-1 and nums[mid]==nums[mid+1]:
                            begin = mid+1
                        else:
                            return mid
            return -1
        return [find(True), find(False)]
#leetcode 74
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])

        x = m - 1
        y = 0
        while x >= 0 and y < n:
            if matrix[x][y] > target:
                x -= 1
            elif matrix[x][y] < target:
                y += 1
            else:
                return True
        return False
#leetcode 240解法1
class Solution:
    def searchMatrix(self, matrix, target):
        # 特判
        rows = len(matrix)
        if rows == 0:
            return False

        cols = len(matrix[0])
        if cols == 0:
            return False

        # 起点：左下角
        x = rows - 1
        y = 0
        # 不越界的条件是：行大于等于 0，列小于等于 cols - 1

        while x >= 0 and y < cols:
            if matrix[x][y] > target:
                x -= 1
            elif matrix[x][y] < target:
                y += 1
            else:
                return True
        return False

#leetcode 240 解法2
class Solution:
    def searchMatrix(self, matrix, target):
        # 特判
        rows = len(matrix)
        if rows == 0:
            return False

        cols = len(matrix[0])
        if cols == 0:
            return False

        # 起点：右上
        x = 0
        y = cols -1
        
        # 不越界的条件是：行小于等于 rows - 1，列大于等于 0
        while x < rows and y >= 0:
            if matrix[x][y] > target:
                y -= 1
            elif matrix[x][y] < target:
                x += 1
            else:
                return True
        return False

#leetcode 153 解法1
class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            # important
            if nums[l] < nums[r]:
                return nums[l]
            mid = (l + r) // 2
            # left part
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                # right part
                r = mid
        # l or r is not important
        return nums[l]
#leetcode 153 解法2
class Solution:
    def findMin(self, nums):
        # If the list has just one element then return that element.
        if len(nums) == 1:
            return nums[0]

        # left pointer
        left = 0
        # right pointer
        right = len(nums) - 1

        # if the last element is greater than the first element then there is no rotation.
        # e.g. 1 < 2 < 3 < 4 < 5 < 7. Already sorted array.
        # Hence the smallest element is first element. A[0]
        if nums[right] > nums[0]:
            return nums[0]

        # Binary search way
        while right >= left:
            # Find the mid element
            mid = left + (right - left) // 2
            # if the mid element is greater than its next element then mid+1 element is the smallest
            # This point would be the point of change. From higher to lower value.
            if nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            # if the mid element is lesser than its previous element then mid element is the smallest
            if nums[mid - 1] > nums[mid]:
                return nums[mid]

            # if the mid elements value is greater than the 0th element this means
            # the least value is still somewhere to the right as we are still dealing with elements greater than nums[0]
            if nums[mid] > nums[0]:
                left = mid + 1
            # if nums[0] is greater than the mid value then this means the smallest value is somewhere to the left
            else:
                right = mid - 1
#leetcode 235 迭代
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur_node = root
        while cur_node:
            if p.val > cur_node.val and q.val > cur_node.val:
                cur_node = cur_node.right
            elif p.val < cur_node.val and q.val < cur_node.val:
                cur_node = cur_node.left
            else:
                return cur_node
#leetcode 235 递归
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right,p,q)

        elif root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left,p,q)

        else:
            return root
#leetcode 450
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:
        if root is None:
            return None

        # 递归调用左子树
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
            return root

        # 递归调用右子树
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
            return root

        # 当前节点的val正好等于key
        # 当前节点的左子节点不存在，直接提升右子节点即可
        if root.left is None:
            new_root = root.right
            root.right = None
            return new_root

        # 当前节点的右子节点不存在，直接提升左子节点即可
        if root.right is None:
            new_root = root.left
            root.left = None
            return new_root

        # 当前节点的左右子节点均存在，这里我用左子树中最大的点来替换
        # 寻找左子树中最大的点（即最右边这个节点）
        node = root.left
        while node.right != None:
            node = node.right
        # 左子树中最大的点变为新的根节点
        new_root = TreeNode(node.val)
        # 新的根节点的左子树需要更新
        new_root.left = self.removeMax(root.left)
        # 新的根节点的右子树即为原来的右子树
        new_root.right = root.right

        root.left = None
        root.right = None
        return new_root

    def removeMax(self, node):
        if node.right == None:
            new_root = node.left
            node.left = None
            return new_root
        node.right = self.removeMax(node.right)
        return node
#leetcode 669解法1
class Solution:
    def trimBST(self, root, L, R):
        if root is None:
            return None
        l_res = self.trimBST(root.left, L, R)
        r_res = self.trimBST(root.right, L, R)
        if L <= root.val <= R:
            root.left = l_res
            root.right = r_res
        elif root.val < L:
            root = r_res
        else:
            root = l_res
        return root
#leetcode 669 解法2
class Solution:
    def trimBST(self, root, L, R):
        if root is None:
            return None
        if root.val < L and root.right is None:
            return None
        if root.val > R and root.left is None:
            return None
        
        while root.val < L or root.val > R:
            if root.val < L:
                root = root.right
            else:
                root = root.left

        p = root
        while p is not None:
            while p.left is not None and p.left.val < L:
                p.left = p.left.right
            p = p.left
        p = root
        while p is not None:
            while p.right is not None and p.right.val > R:
                p.right = p.right.left
            p = p.right
        return root
#leetcode 700 解法1
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root is None or val == root.val:
            return root
        
        return self.searchBST(root.left, val) if val < root.val \
            else self.searchBST(root.right, val)

#leetcode 700 解法2
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        while root is not None and root.val != val:
            root = root.left if val < root.val else root.right
        return root

#leetcode 701
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        res = copy.deepcopy(root)
        cur_node = res

        # 如果二叉搜索树为空树，用val构造二叉树节点作为根节点并返回
        if cur_node == None:
            return TreeNode(val)

        while cur_node:
            if val > cur_node.val:
                # 走向右子树
                if cur_node.right != None:
                    cur_node = cur_node.right
                # 应该走向右子树而右子树为空，即找到了插入位置
                else:
                    cur_node.right = TreeNode(val)
                    return res
            elif val < cur_node.val:
                # 走向左子树
                if cur_node.left != None:
                    cur_node = cur_node.left
                # 应该走向左子树而左子树为空，即找到了插入位置
                else:
                    cur_node.left = TreeNode(val)
                    return res
#leetcode 98 方法1
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def helper(root,max_val,min_val):
            if root == None:
                return True
            if root.val < max_val and root.val > min_val:
                return helper(root.left,root.val,min_val) and helper(root.right,max_val,root.val)
            else:
                return False


        max_val = float('inf')
        min_val = -float('inf')
        return helper(root,max_val,min_val)
#leetcode98 方法2
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root == None:
            return True

        pre = -float('inf')
        stack = []

        p_node = root
        while stack or p_node:
            # 把所有当前访问节点的左孩子都入栈
            while p_node:
                stack.append(p_node)
                p_node = p_node.left

            # 操作栈顶节点，如果是第一次运行到这步，那么这是整棵树的最左节点
            cur_node = stack.pop()
            # 检查是否从小到大
            if cur_node.val > pre:
                pre = cur_node.val
            else:
                return False

            # 将指针指向当前节点的右节点
            if cur_node.right != None:
                p_node = cur_node.right

        return True
#leetcode 99 解法1
class Solution(object):
    def recoverTree(self, root):
        nodes = []
        # 中序遍历二叉树，并将遍历的结果保存到list中        
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            nodes.append(root)
            dfs(root.right)
        dfs(root)
        x = None
        y = None
        pre = nodes[0]
        # 扫面遍历的结果，找出可能存在错误交换的节点x和y
        for i in range(1,len(nodes)):
            if pre.val>nodes[i].val:
                y=nodes[i]
                if not x:
                    x = pre
            pre = nodes[i]
        # 如果x和y不为空，则交换这两个节点值，恢复二叉搜索树 
        if x and y:
            x.val,y.val = y.val,x.val
#leetcode 99 解法2
class Solution(object):
    def recoverTree(self, root):
        # 用两个变量x，y来记录需要交换的节点
        self.x = None
        self.y = None
        self.pre = None
        # 中序遍历二叉树，并比较上一个节点(pre)和当前节点的值，如果pre的值大于当前节点值，则记录下这两个节点
        def dfs(root):
            if not root:
                return
            dfs(root.left)
            if not self.pre:
                self.pre = root
            else:
                if self.pre.val>root.val:
                    self.y = root
                    if not self.x:
                        self.x = self.pre
                self.pre = root
            dfs(root.right)
        dfs(root)
        # 如果x和y都不为空，说明二叉搜索树出现错误的节点，将其交换
        if self.x and self.y:
            self.x.val,self.y.val = self.y.val,self.x.val
#leetcode 99 解法3
class Solution(object):
    def recoverTree(self, root):
        x = None
        y = None
        pre = None
        tmp = None
        while root:
            if root.left:
                tmp = root.left
                while tmp.right and tmp.right!=root:
                    tmp = tmp.right
                if tmp.right is None:
                    tmp.right = root
                    root = root.left
                else:
                    if pre and pre.val>root.val:
                        y = root
                        if not x:
                            x = pre
                    pre = root
                    tmp.right = None
                    root = root.right
            else:
                if pre and pre.val>root.val:
                    y = root
                    if not x:
                        x = pre
                pre = root
                root = root.right
        if x and y:
            x.val,y.val = y.val,x.val

#leetcode 230
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if root == None:
            return None

        # 中序遍历二叉树
        res = []
        stack = []
        p_node = root

        while stack or p_node:
            while p_node:
                stack.append(p_node)
                p_node = p_node.left

            cur_node = stack.pop()
            res.append(cur_node.val)

            if cur_node.right != None:
                p_node = cur_node.right

        # 返回第k个元素
        return res[k-1]
#leetcode 501 解法1
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if root == None:
            return None
        
        dicts = {}
        queue = [root]
        while queue:
            length = len(queue)
            for _ in range(length):
                node = queue.pop(0)
                # 节点值存入字典
                if node.val in dicts:
                    dicts[node.val] += 1
                else:
                    dicts[node.val] = 1

                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)

        # 计算众数
        max_num = 0
        for i,counts in dicts.items():
            if counts > max_num:
                res = [i]
                max_num = counts
            # 输出所有众数
            elif counts == max_num:
                res.append(i)

        return res
#leetcode 501 方法2
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        if root == None:
            return None

        stack = []
        p_node = root
        pre_node = TreeNode(float('inf'))
        maxTimes = 0
        res = []

        while stack or p_node:
            # 把所有当前访问节点的左孩子都入栈
            while p_node != None:
                stack.append(p_node)
                p_node = p_node.left

            cur_node = stack.pop()

            # 更新当前节点出现次数
            if pre_node.val == cur_node.val:
                curTimes += 1
            else:
                curTimes = 1
            # 最大出现次数
            if maxTimes == curTimes:
                res.append(cur_node.val)
            elif maxTimes < curTimes:
                res = [cur_node.val]
                maxTimes = curTimes
            
            # 更新前驱节点
            pre_node = cur_node

            if cur_node.right != None:
                # 将指针指向当前节点的右节点
                p_node = cur_node.right

        return res
