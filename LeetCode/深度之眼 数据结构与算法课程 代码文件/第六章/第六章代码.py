#leetcode 100 递归
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p == None and q == None:
            return True

        if p == None or q == None:
            return False

        if p.val != q.val:
            return False
        
        return self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
#leetcode 100 迭代
class Solution:
	def isSameTree(self, p, q):
		# 用栈来保存p和q遍历时的节点
		stack = [(p,q)]
		while stack:
			# 首先比较当前的两个节点
			a,b = stack.pop()
			# 如果a和b都为空就继续下一轮比较
			if not (a or b):
				continue
			# 如果a和b相同，则将a的left和b的left
			# 以及a的right，b的right都放入栈中
			if a and b and a.val==b.val:
				stack.append((a.left,b.left))
				stack.append((a.right,b.right))
			# 否则就直接返回错误
			else:
				return False
		# 如果循环比较结束，说明p和q是相同的
		return True




#leetcode 101 递归
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def isSymmetric(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		if not root:
			return True
		def dfs(left,right):
			# 递归的终止条件是两个节点都为空
			# 或者两个节点中有一个为空
			# 或者两个节点的值不相等
			if not (left or right):
				return True
			if not (left and right):
				return False
			if left.val!=right.val:
				return False
			return dfs(left.left,right.right) and dfs(left.right,right.left)
		# 用递归函数，比较左节点，右节点
		return dfs(root.left,root.right)

#leetcode 101 迭代
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
	def isSymmetric(self, root):
		"""
		:type root: TreeNode
		:rtype: bool
		"""
		if not root or not (root.left or root.right):
			return True
		# 用队列保存节点	
		queue = [root.left,root.right]
		while queue:
			# 从队列中取出两个节点，再比较这两个节点
			left = queue.pop(0)
			right = queue.pop(0)
			# 如果两个节点都为空就继续循环，两者有一个为空就返回false
			if not (left or right):
				continue
			if not (left and right):
				return False
			if left.val!=right.val:
				return False
			# 将左节点的左孩子， 右节点的右孩子放入队列
			queue.append(left.left)
			queue.append(right.right)
			# 将左节点的右孩子，右节点的左孩子放入队列
			queue.append(left.right)
			queue.append(right.left)
		return True

#leetcode 110 方法1
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if root == None:
            return True

        # 当前节点满足平衡树，继续递归判断子树是否满足平衡树条件
        if abs(self.depth(root.left)-self.depth(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return False

    # 计算树高度
    def depth(self, root):
        if root == None:
            return 0

        if root.left == None and root.right == None:
            return 1

        if root.left != None or root.right != None:
            return 1+max(self.depth(root.left),self.depth(root.right))
#leetcode 110 方法2
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if self.depth(root) == -1:
            return False
        else:
            return True

    def depth(self, root):
        if root == None:
            return 0

        depth_left = self.depth(root.left)
        # 提前阻断
        if depth_left == -1:
            return -1

        depth_right = self.depth(root.right)
        # 提前阻断
        if depth_right == -1:
            return -1

        if abs(depth_left-depth_right) <= 1:
            return 1+max(depth_left,depth_right)
        # 提前阻断
        else:
            return -1
#leetcode104 方法1
class Solution(object):
	def maxDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		if(not root):
			return 0
		stack = [(1,root)]
		depth = 0
		# 将(1,root)加入栈后不断遍历栈
		while stack:
			# 首先从栈中弹出元素
			cur_depth,node = stack.pop()
			# 如果弹出的节点不为空
			if node:
				# 比较这个节点的深度和depth的大小
				depth = max(cur_depth,depth)
				# 将 (当前深度+1，left)放入栈中
				stack.append((cur_depth+1,node.left))
				# 同理将(当前深度+1,right)放入栈中
				stack.append((cur_depth+1,node.right))
	return depth
#leetcode104 方法2
class Solution(object):
	def maxDepth(self, root):
		"""
		:type root: TreeNode
		:rtype: int
		"""
		# 如果节点为空，那么深度就是0
		if(not root):
			return 0
		# 否则递归的计算  max(左子树的最大深度，右子树的最大深度)
		# 不管左子树，右子树是否为空，他们的父节点肯定是不为空
		# 所以计算出的总深度要把父节点也要加上，也就是 +1
		return max( self.maxDepth(root.left), self.maxDepth(root.right) ) + 1

#leetcode 111 方法1
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
      
        queue = [(root,1)]

        while queue:
            node,depth = queue.pop(0)
            if node.left == None and node.right == None:
                return depth

            if node.left != None:
                queue.append((node.left,depth+1))

            if node.right != None:
                queue.append((node.right,depth+1))
#leetcode 111 方法2

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if root == None:
            return 0
        
        # 叶子节点，返回1
        if root.left == None and root.right == None:
            return 1

        # 当左右孩子有一个为空时，返回不为空的孩子节点的深度
        if root.left == None or root.right == None:
            return 1+max(self.minDepth(root.left),self.minDepth(root.right))

        # 当左右孩子都不为空时，返回左右孩子较小深度的节点值
        if root.left != None and root.right != None:
            return 1+min(self.minDepth(root.left),self.minDepth(root.right))

#leetcode 662
class Solution:
    def widthOfBinaryTree(self, root: TreeNode) -> int:
    	if root == None:
            return 0
        queue = [(root,1)]
        width = 0
        while queue:
            length = len(queue)
            for i in range(length):
                node,nums = queue.pop(0)
                # 记录该层第一个节点的编号、最后一个节点的编号
                if i == 0:
                    first_num = nums
                if i == length-1:
                    last_num = nums
                    # 更新最大宽度
                    width = max(width,last_num-first_num+1)
                # 左右子树入队
                if node.left != None:
                    queue.append((node.left,2*nums))
                if node.right != None:
                    queue.append((node.right,2*nums+1))
        
        return width
#leetcode 144 方法一
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []

        output = []
        
        output.append(root.val)
        output += self.preorderTraversal(root.left)
        output += self.preorderTraversal(root.right)
        
        return output
#leetcode 144 方法2
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []

        stack = [root]
        output = []
        
        while stack:
            root = stack.pop()
            if root != None:
                # 先入栈右节点
                stack.append(root.right)
                # 后入栈左节点
                stack.append(root.left)
                # 栈顶元素并入输出
                output.append(root.val)
        
        return output
#leetcode 144 方法3
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root == None:
            return []
        
        WHITE,GRAY = 0,1
        stack = [(WHITE,root)]
        output = []

        while stack:
            color,root = stack.pop()
            if root != None:
                if color == WHITE:
                    stack.append((WHITE,root.right))
                    stack.append((WHITE,root.left))
                    stack.append((GRAY,root))
                else:
                    output.append(root.val)
        
        return output
#leetcode94 方法1
class Solution(object):
    def inorderTraversal(self, root):
        if root == None:
            return []

        output = []

        output += self.inorderTraversal(root.left)
        output.append(root.val)
        output += self.inorderTraversal(root.right)

        return output
#leetcode94 方法2
class Solution(object):
    def inorderTraversal(self, root):
        if root == None:
            return []

        stack = []
        output = []

        # 当前访问节点指针
        p_node = root
        while stack or p_node:
            # 把所有当前访问节点的左孩子都入栈
            while p_node:
                stack.append(p_node)
                p_node = p_node.left

            # 操作栈顶节点，如果是第一次运行到这步，那么这是整棵树的最左节点
            cur_node = stack.pop()
            # 因为已经保证没有左节点，可以访问根节点
            output.append(cur_node.val)

            if cur_node.right:
                # 将指针指向当前节点的右节点
                p_node = cur_node.right

        return output
#leetcode94 方法3
class Solution(object):
    def inorderTraversal(self, root):
        if root == None:
            return []

        WHITE,GRAY = 0,1
        
        stack = [(WHITE,root)]
        output = []

        while stack:
            color,root = stack.pop()
            if root != None:
                if color == WHITE:
                    stack.append((WHITE,root.right))
                    stack.append((GRAY,root))
                    stack.append((WHITE,root.left))
                else:
                    output.append(root.val)
        
        return output
#leetcode145 方法1
class Solution(object):
    def postorderTraversal(self,root):
        if root == None:
            return []

        output = []
        
        output += self.postorderTraversal(root.left)
        output += self.postorderTraversal(root.right)
        output.append(root.val)

        return output
#leetcode145 方法2
class Solution(object):
    def postorderTraversal(self,root):
        if root == None:
            return []

        stack = [root]
        output = []

        while stack:
            root = stack.pop()
            if root != None:
                output.append(root.val)
                stack.append(root.left)
                stack.append(root.right)
        
        return output[::-1]
#leetcode145 方法3
class Solution(object):
    def postorderTraversal(self,root):
        if root == None:
            return []

        WHITE,GRAY = 0,1

        stack = [(WHITE,root)]
        output = []

        while stack:
            color,root = stack.pop()
            if root != None:
                if color == WHITE:
                    stack.append((GRAY,root))
                    stack.append((WHITE,root.right))                
                    stack.append((WHITE,root.left))
                else:
                    output.append(root.val)
        
        return output
#leetcode102 方法1
class Solution(object):
	def levelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		if not root:
			return []
		res = []
		queue = [root]
		while queue:
			# 获取当前队列的长度，这个长度相当于 当前这一层的节点个数
			size = len(queue)
			tmp = []
			# 将队列中的元素都拿出来(也就是获取这一层的节点)，放到临时list中
			# 如果节点的左/右子树不为空，也放入队列中
			for _ in range(size):
				r = queue.pop(0)
				tmp.append(r.val)
				if r.left:
					queue.append(r.left)
				if r.right:
					queue.append(r.right)
			# 将临时list加入最终返回结果中
			res.append(tmp)
		return res

#leetcode102 方法2
class Solution(object):
	def levelOrder(self, root):
		"""
		:type root: TreeNode
		:rtype: List[List[int]]
		"""
		if not root:
			return []
		res = []
		def dfs(index,r):
			# 假设res是[ [1],[2,3] ]， index是3，就再插入一个空list放到res中
			if len(res)<index:
				res.append([])
			#  将当前节点的值加入到res中，index代表当前层，假设index是3，节点值是99
			# res是[ [1],[2,3] [4] ]，加入后res就变为 [ [1],[2,3] [4,99] ]
			res[index-1].append(r.val)
			# 递归的处理左子树，右子树，同时将层数index+1
			if r.left:
				dfs(index+1,r.left)
			if r.right:
				dfs(index+1,r.right)
		dfs(1,root)
		return res

#leetcode103 方法1
class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        import collections
        # 定义一个双端队列，初始时候将根节点放入队列
        queue = collections.deque()
        queue.append(root)
        # 定义index，用来控制输出的方向的，是正向输出，还是反向输出
        index = 1
        res = []
        while queue:
            # 获取queue的长度，因为队列的长度是在不断变化的，这里需先确定要遍历多少次
            size = len(queue)
            tmp = []
            for _ in range(size):
                node = queue.popleft()
                tmp.append(node.val)
                # 如果左节点不为空，则继续放入队列中
                if node.left:
                    queue.append(node.left)
                # 如果右节点不为空，则继续放入队列中
                if node.right:
                    queue.append(node.right)
            # 当index为奇数时，就正向输出
            if (index & 1)==1:
                res.append(tmp)
            # 当index偶位数时，就反向输出，即先调用一次reverse，再保存
            else:
                res.append(tmp[::-1])
            index += 1
        return res
#leetcode103 方法2

class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []
        res = []
        def dfs(root, index):
            if not root:
                return
            if len(res) < index:
                res.append(collections.deque())
            if index % 2:
                res[index - 1].append(root.val)
            else:
                res[index - 1].appendleft(root.val)
            dfs(root.left, index + 1)
            dfs(root.right, index + 1)
        dfs(root, 1)
        return [list(q) for q in res]




#leetcode107 方法1
class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []
        # 创建一个队列，将根节点放入其中    
        queue = [root]
        # 用来存放最终结果
        res = []
        while queue:
            # 每次遍历的数量为队列的长度
            size = len(queue)
            tmp = []
            # 将这一层的元素全部取出，放入到临时数组中，如果节点的左右孩子不为空，继续放入队列
            for _ in range(size):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp)
        # 翻转最终结果并返回
        return res[::-1]

#leetcode107 方法2
class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []
        queue = [root]
        # 改用双端队列实现，每次都插入到第一位
        res = collections.deque()
        while queue:
            size = len(queue)
            tmp = []
            for _ in range(size):
                node = queue.pop(0)
                tmp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # 每次插入到第一位，这样自带了翻转的功能       
            res.appendleft(tmp)
        return list(res)
#leetcode107 方法3
class Solution(object):
    def levelOrderBottom(self, root):
        if not root:
            return []
        # 用来存放最终结果    
        res = []
        def dfs(root,index):
            if not root:
                return
            # 如果index大于res大小，说明这一层没有对应的集合，需要新创建    
            if index>len(res):
                res.append([])
            # 将当前层的元素直接放到对应层的末尾即可    
            res[index-1].append(root.val)
            # 继续遍历左右节点，同时将层高+1
            dfs(root.left,index+1)
            dfs(root.right,index+1)
        dfs(root,1)
        return res[::-1]


#leetcode116 方法1
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
	def connect(self, root):
		"""
		:type root: Node
		:rtype: Node
		"""
		if not root:
			return root
		queue = [root]
		while queue:
			size = len(queue)
			# 将队列中的元素串联起来
			tmp = queue[0]
			for i in range(1,size):
				tmp.next = queue[i]
				tmp = queue[i]
			# 遍历队列中的每个元素，将每个元素的左右节点也放入队列中
			for _ in range(size):
				tmp = queue.pop(0)
				if tmp.left:
					queue.append(tmp.left)
				if tmp.right:
					queue.append(tmp.right)
		return root

#leetcode116 方法2
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
	def connect(self, root):
		"""
		:type root: Node
		:rtype: Node
		"""
		if not root:
			return root
		pre = root
		# 循环条件是当前节点的left不为空，当只有根节点
		# 或所有叶子节点都出串联完后循环就退出了
		while pre.left:
			tmp = pre
			while tmp:
				# 将tmp的左右节点都串联起来
				# 注:外层循环已经判断了当前节点的left不为空
				tmp.left.next = tmp.right
				# 下一个不为空说明上一层已经帮我们完成串联了
				if tmp.next:
					tmp.right.next = tmp.next.left
				# 继续右边遍历
				tmp = tmp.next
			# 从下一层的最左边开始遍历	
			pre = pre.left
		return root

#leetcode116 方法3
class Solution(object):
	def connect(self, root):
		"""
		:type root: Node
		:rtype: Node
		"""
		def dfs(root):
			if not root:
				return
			left = root.left
			right = root.right
			# 配合动画演示理解这段，以root为起点，将整个纵深这段串联起来
			while left:
				left.next = right
				left = left.right
				right = right.left
			# 递归的调用左右节点，完成同样的纵深串联
			dfs(root.left)
			dfs(root.right)
		dfs(root)
		return root

		
#leetcode117 方法1
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
	def connect(self, root):
		"""
		:type root: Node
		:rtype: Node
		"""
		if not root:
			return root
		queue = [root]
		while queue:
			size = len(queue)
			# 将队列中的元素串联起来
			tmp = queue[0]
			for i in range(1,size):
				tmp.next = queue[i]
				tmp = queue[i]
			# 遍历队列中的每个元素，将每个元素的左右节点也放入队列中
			for _ in range(size):
				tmp = queue.pop(0)
				if tmp.left:
					queue.append(tmp.left)
				if tmp.right:
					queue.append(tmp.right)
		return root
#leetcode 117 方法2
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':

        if root == None:
            return root

        rootNode = root  # 初始状态

        oneNode_Next = None  # 初始状态
        first_Next = None  # 初始状态

        while rootNode:  # 当前层节点不是空的时候
            if rootNode.left:  # 当前层节点下面的左子节点不是空
                if not first_Next:  # 还没有记录first_Next的话，第一时间记录下来。
                    first_Next = rootNode.left
                if oneNode_Next:  # 如果之前有记录的oneNode_Next就把它的next指向现在这个位置。
                    oneNode_Next.next = rootNode.left
                oneNode_Next = rootNode.left # 移动oneNode_Next到当前位置。

            if rootNode.right: # 同上一段。
                if not first_Next:
                    first_Next = rootNode.right
                if oneNode_Next:
                    oneNode_Next.next = rootNode.right
                oneNode_Next = rootNode.right

            rootNode = rootNode.next  # 当前行内rootNode往右移动。

            if not rootNode:  # 移动rootNode到下一行的初始位置。
                rootNode = first_Next
                oneNode_Next = None
                first_Next = None

        return root

#leetcode 117 方法3
class Solution(object):
	def connect(self, root):
		"""
		:type root: Node
		:rtype: Node
		"""
		if not root:
			return root
		queue = [root]
		while queue:
			size = len(queue)
			# 将队列中的元素串联起来
			tmp = queue[0]
			for i in range(1,size):
				tmp.next = queue[i]
				tmp = queue[i]
			# 遍历队列中的每个元素，将每个元素的左右节点也放入队列中
			for _ in range(size):
				tmp = queue.pop(0)
				if tmp.left:
					queue.append(tmp.left)
				if tmp.right:
					queue.append(tmp.right)
		return root

#leetcode 105
class Solution(object):
	def buildTree(self, preorder, inorder):
		if not (preorder and inorder):
			return None
		# 根据前序数组的第一个元素，就可以确定根节点	
		root = TreeNode(preorder[0])
		# 用preorder[0]去中序数组中查找对应的元素
		mid_idx = inorder.index(preorder[0])
		# 递归的处理前序数组的左边部分和中序数组的左边部分
		# 递归处理前序数组右边部分和中序数组右边部分
		root.left = self.buildTree(preorder[1:mid_idx+1],inorder[:mid_idx])
		root.right = self.buildTree(preorder[mid_idx+1:],inorder[mid_idx+1:])
		return root

#leetcode106
class Solution(object):
    def buildTree(self, inorder, postorder):
        if not (inorder and postorder):
            return None
        # 将中序数组的下标、值保存到map中省去解法一中线性查找
        d = {val:idx for idx,val in enumerate(inorder)}
        self.post_idx = len(postorder)-1
        def dfs(left,right):
            if left>right:
                return None
            # 从后序数组中拿最后一个元素，根据这个元素去map中找到中序数组对应的index
            # 然后递归的处理右边[index+1,right]，递归处理左边[left,index-1]
            val = postorder[self.post_idx]
            self.post_idx -= 1
            root = TreeNode(val)
            index = d[val]
            root.right = dfs(index+1,right)
            root.left = dfs(left,index-1)
            return root
        return dfs(0,len(inorder)-1)

#leetcode 889
class Solution(object):
    def constructFromPrePost(self, pre, post):
        def dfs(pre,post):
            if not pre:
                return None
            # 数组长度为1时，直接返回即可
            if len(pre)==1:
                return TreeNode(pre[0])
            # 根据前序数组的第一个元素，创建根节点     
            root = TreeNode(pre[0])
            # 根据前序数组第二个元素，确定后序数组左子树范围
            left_count = post.index(pre[1])+1
            # 递归执行前序数组左边、后序数组左边
            root.left = dfs(pre[1:left_count+1],post[:left_count])
            # 递归执行前序数组右边、后序数组右边
            root.right = dfs(pre[left_count+1:],post[left_count:-1])
            # 返回根节点
            return root
        return dfs(pre,post)

#leetcode 112 方法1
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False

        # 当前节点是叶子，检查 root.val 值是否为 sum
        if root.left == None and root.right == None and root.val == sum:
            return True

        # 当前节点不是叶子，对它的所有孩子节点，递归调用 hasPathSum() 函数
        return self.hasPathSum(root.left,sum-root.val) or self.hasPathSum(root.right,sum-root.val)
#leetcode 112 方法2
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root == None:
            return False

        stack = [(root,sum)]
        while stack:
            node,sum = stack.pop()
            # 判断叶子节点是否满足了条件
            if node.left == None and node.right == None and node.val == sum:
                return True
            
            # 左节点不为空，我们把左节点和剩余值打包压栈
            if node.left != None:
                stack.append((node.left,sum-node.val))
            # 右节点不为空，我们把右节点和剩余值打包压栈
            if node.right != None:
                stack.append((node.right,sum-node.val))

        return False
#leetcode113 方法1
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        # 辅助函数（因为需要一个变量记录路径）       
        def helper(root, sum, temp):
            if root == None:
                return

            # 路径和满足sum，路径添加到结果数组res
            if root.left == None and root.right == None and root.val == sum:
                temp += [root.val]
                res.append(temp)

            # 递归搜索左右子树，传入剩余和以及路径
            helper(root.left,sum-root.val,temp+[root.val])
            helper(root.right,sum-root.val,temp+[root.val])


        res = []
        helper(root,sum,[])

        return res
#leetcode113 方法2
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root == None:
            return []

        res = []
        temp = []
        stack = [(root,sum,temp)]

        while stack:
            node,sum,temp = stack.pop()
            # 判断叶子节点是否满足了条件
            if node.left == None and node.right == None and node.val == sum:
                temp += [node.val]
                res.append(temp)

            if node.left != None:
                stack.append((node.left,sum-node.val,temp + [node.val]))

            if node.right != None:
                stack.append((node.right,sum-node.val,temp + [node.val]))

        return res
#leetcode129 递归
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        def helper(root, nums):
            if root == None:
                return 0

            # 更新路径和
            nums *= 10
            nums += root.val

            # 如果已经是叶子节点，保存路径和到列表中
            if root.left == None and root.right == None:
                res.append(nums)

            if root.left != None:
                helper(root.left,nums)

            if root.right != None:
                helper(root.right,nums)

        
        res = []
        helper(root,0)

        return sum(res)
#leetcode129 迭代
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if root == None:
            return 0

        stack = [(root,0)]
        res = []

        while stack:
            node,nums = stack.pop()
            # 更新路径和
            nums *= 10
            nums += node.val

            # 如果已经是叶子节点，保存路径和到列表中
            if node.left == None and node.right == None:
                res.append(nums)

            if node.left != None:
                stack.append((node.left,nums))

            if node.right != None:
                stack.append((node.right,nums))

        return sum(res)
#leetcode 124
class Solution:
    def __init__(self):
        self.maxSum = float("-inf")

    def maxPathSum(self, root: TreeNode) -> int:
        def maxGain(node):
            if not node:
                return 0

            # 递归计算左右子节点的最大贡献值
            # 只有在最大贡献值大于 0 时，才会选取对应子节点
            leftGain = max(maxGain(node.left), 0)
            rightGain = max(maxGain(node.right), 0)
            
            # 节点的最大路径和取决于该节点的值与该节点的左右子节点的最大贡献值
            priceNewpath = node.val + leftGain + rightGain
            
            # 更新答案
            self.maxSum = max(self.maxSum, priceNewpath)
        
            # 返回节点的最大贡献值
            return node.val + max(leftGain, rightGain)
   
        maxGain(root)
        return self.maxSum
#leetcode257
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if root == None:
            return None

        res = []
        queue = [(root,'')]

        while queue:
            temp = ''
            length = len(queue)

            for _ in range(length):
                node,temp = queue.pop(0)
                temp += str(node.val)

                # 如果是叶子节点，记录路径
                if node.left == None and node.right == None:    
                    res.append(temp)

                # 格式要求
                temp += '->'

                if node.left != None:
                    queue.append((node.left,temp))

                if node.right != None:
                    queue.append((node.right,temp))

        return res



