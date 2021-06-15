
 
#leetcode 1046 解法
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # 初始化
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        # 模拟
        while len(heap) > 1:
            x,y = heapq.heappop(heap),heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap,x-y)

        if heap: return -heap[0]
        return 0

#leetcode 295
import heapq


class MedianFinder:

    def __init__(self):
        # 当前大顶堆和小顶堆的元素个数之和
        self.count = 0
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        self.count += 1
        # 因为 Python 中的堆默认是小顶堆，所以要传入一个 tuple，用于比较的元素需是相反数，
        # 才能模拟出大顶堆的效果
        heapq.heappush(self.max_heap, (-num, num))
        _, max_heap_top = heapq.heappop(self.max_heap)
        heapq.heappush(self.min_heap, max_heap_top)
        if self.count & 1:
            min_heap_top = heapq.heappop(self.min_heap)
            heapq.heappush(self.max_heap, (-min_heap_top, min_heap_top))

    def findMedian(self) -> float:
        if self.count & 1:
            # 如果两个堆合起来的元素个数是奇数，数据流的中位数大顶堆的堆顶元素
            return self.max_heap[0][1]
        else:
            # 如果两个堆合起来的元素个数是偶数，数据流的中位数就是各自堆顶元素的平均值
            return (self.min_heap[0] + self.max_heap[0][1]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()



#leetcode 1439
class Solution:
    def kthSmallest(self, mat, k: int) -> int:
        h = []
        cur = (sum(vec[0] for vec in mat), tuple([0] * len(mat)))
        heapq.heappush(h, cur)
        seen = set(cur)

        for _ in range(k):
            acc, pointers = heapq.heappop(h)
            for i, pointer in enumerate(pointers):
                if pointer != len(mat[0]) - 1:
                    t = list(pointers)
                    t[i] = pointer + 1
                    tt = tuple(t)
                    if tt not in seen:
                        seen.add(tt)
                        heapq.heappush(h, (acc + mat[i][pointer + 1] - mat[i][pointer], tt))
        return acc
 #leetcode264 解法1

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [2,3,5]
        explored = {1}
        pq = [1]
        for i in range(1, n+1):
            x = heapq.heappop(pq)
            if i == n:
                return x
            for num in nums:
                t = num * x
                if t not in explored:
                    explored.add(t)
                    heapq.heappush(pq,t)
        return -1

#leetcode264 解法2
class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # ans 用作存储已有丑数（从下标 1 开始存储，第一个丑数为 1）
        ans = [0] * (n+1)
        ans[1] = 1
        # 由于三个有序序列都是由「已有丑数」*「质因数」而来
        # i2、i3 和 i5 分别代表三个有序序列当前使用到哪一位「已有丑数」下标（起始都指向 1）
        i2 = i3 = i5 = 1
        idx = 2
        while idx <= n:
            # 由 ans[iX] * X 可得当前有序序列指向哪一位
            a,b,c = ans[i2] *2,ans[i3]*3,ans[i5]*5
            # 将三个有序序列中的最小一位存入「已有丑数」序列，并将其下标后移
            m = min(a,b,c)
            # 由于可能不同有序序列之间产生相同丑数，因此只要一样的丑数就跳过（不能使用 else if ）
            if m == a:
                i2 += 1
            if m == b:
                i3 += 1
            if m == c:
                i5 += 1
            ans[idx] = m
            idx += 1
        return ans[n]

#leetcode 871
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        stations += [(target, 0)]
        cur = startFuel
        ans = 0

        h = []
        last = 0
        for i, fuel in stations:
            cur -= i - last
            while cur < 0 and h:
                cur -= heapq.heappop(h)
                ans += 1
            if cur < 0:
                return -1
            heappush(h, -fuel)

            last = i
        return ans


#leetcode 1642
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        h = []
        for i in range(1, len(heights)):
            diff = heights[i] - heights[i - 1]
            if diff <= 0:
                continue
            if bricks < diff and ladders > 0:
                ladders -= 1
                if h and -h[0] > diff:
                    bricks -= heapq.heappop(h)
                else:
                    continue
            bricks -= diff
            if bricks < 0:
                return i - 1
            heapq.heappush(h, -diff)
        return len(heights) - 1
        