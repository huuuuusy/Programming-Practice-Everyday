#最基本的算法实现，无优化版：
def bubble_sort(collection):
    """
    无任何优化版
    """
    compare_count=0
    length = len(collection)
    for i in range(length-1):
        print(collection) #方便查看数组的排序过程
        for j in range(length-1-i):
            compare_count+=1
            if collection[j] > collection[j+1]:
                tmp = collection[j]
                collection[j] = collection[j+1]
                collection[j+1] = tmp
    print(f"总循环次数{compare_count}")
    return collection
print("bubble_sort begin.")
unsorted = [3,4,2,1,5,6,7,8]
print("bubble_sort end: ",*bubble_sort(unsorted))

   # 优化一
def bubble_sort2(collection):
    """
    如果没有元素交换，说明数据在排序过程中已经有序，直接退出循环
    """
    compare_count=0
    length = len(collection)
    for i in range(length-1):
        swapped = False
        print(collection)
        for j in range(length-1-i):
            compare_count+=1
            if collection[j] > collection[j+1]:
                swapped = True
                tmp = collection[j]
                collection[j] = collection[j+1]
                collection[j+1] = tmp
        if not swapped: break  # Stop iteration if the collection is sorted.
    print(f"总循环次数{compare_count}")
    return collection
print("bubble_sort2 begin.")
unsorted = [3,4,2,1,5,6,7,8]
print("bubble_sort2 end:",*bubble_sort2(unsorted))

   # 优化二：
def bubble_sort3(collection):
    """
    bubble_sort2的基础上再优化。
    优化思路：在排序的过程中，数据可以从中间分为两段，一段是无序状态，另一段是有序状态。
    每一次循环的过程中，记录最后一个交换元素的公交车，它便是有序和无序状态的边界
    下一次仅循环到边界即可，从而减少循环次数，达到优化。
    """
    compare_count=0
    length = len(collection)
    last_change_index = 0 #最后一个交换的位置
    border = length-1 #有序和无序的分界线
    for i in range(length-1):
        swapped = False
        print(collection)

        for j in range(0,border):
            compare_count+=1
            if collection[j] > collection[j+1]:
                swapped = True
                collection[j], collection[j+1] = collection[j+1], collection[j]
                last_change_index = j
        if not swapped: break  # Stop iteration if the collection is sorted.

        border = last_change_index # 最后一个交换的位置就是边界

    print(f"总循环次数{compare_count}")
    return collection
    
print("bubble_sort3 begin.")
unsorted = [3,4,2,1,5,6,7,8]
print("bubble_sort3 end:",*bubble_sort3(unsorted))

#选择排序无优化版：
def selection_sort(data_list):
    count = 0 
    length = len(data_list)
    for i in range(length -1):
        print(data_list) #打印每一次选择后的结果
        min_index = i #存储最小值的下标，以便最后交换
        for j in range(i+1,length):
            count +=1
            if data_list[min_index] > data_list[j]:
                min_index = j
        if min_index != i: #说明需要交换，否则不需要自己自己交换 
            tmp = data_list[i]
            data_list[i] = data_list[min_index]
            data_list[min_index] = tmp
    print(f"总循环次数为 {count}")
    return data_list
unsort = [3,4,2,1,5,6,7,8]
print("selection_sort 的结果",*selection_sort(unsort))
#优化版
def selection_sort2(data_list):
    count = 0 
    length = len(data_list)
    for i in range(length -1):
        print(data_list) #打印每一次选择后的结果
        min_index = i #存储最小值的下标 
        max_index = length - i -1 #最大值的下标，以便最后交换

        for j in range(i+1,length - i -1):
            count +=1
            if data_list[min_index] > data_list[j]:
                min_index = j
            if data_list[max_index] < data_list[j]:
                max_index = j

            #退出条件
        if min_index +1 == max_index:
            break

        #前面的数据与最小值交换
        if min_index != i: #说明需要交换，否则不需要自己自己交换 
            tmp = data_list[i]
            data_list[i] = data_list[min_index]
            data_list[min_index] = tmp

        #后面的数据与最大值交换
        if max_index != length - i -1: #说明需要交换，否则不需要自己与自己交换 
            tmp = data_list[length - i -1 ]
            data_list[length -i -1 ] = data_list[max_index]
            data_list[max_index] = tmp


    print(f"总循环次数为 {count}")
    return data_list
unsort = [3,4,2,1,5,6,7,8]
print("selection_sort2 的结果",*selection_sort2(unsort)
#未优化版插入排序
#encoding=utf-8
def insert_sort(data_list):
    '''
    无优化版
    '''
    count=0 #统计循环次数
    length = len(data_list)
    for i in range(1,length ): #默认第一个位置的元素是已排序区间，因此下标从 1 开始
        tmp = data_list[i] #待插入的数据
        j = i 
        while j > 0: #从已排序区间查找插入位置
            count +=1
            if tmp < data_list[j-1]:
                data_list[j] = data_list[j-1]  #元素向后移动，腾出插入位置
            else:
                break
            j -= 1
        data_list[j] = tmp #插入操作
        print(data_list)
    print(f"总循环次数为 {count}")
    return data_list
if __name__ == "__main__":
    unsort = [1,3,4,2,1,5,6,7,8,4]
    print(*insert_sort(unsort))
 #   优化版插入排序
def insert_sort2(data_list):
    '''
    使用二分查找函数确定待插入元素在有序区间的插入位置
    '''
    count=0 #统计循环次数
    length = len(data_list)
    for i in range(1,length ): #默认第一个位置的元素是已排序区间，因此下标从 1 开始
        print(data_list)
        wait_insert_data = data_list[i] ##等待插入元素
        move_index = i 
        insert_index,count1 = binary_search(data_list[0:i],wait_insert_data) #寻找插入位置
        count+=count1 #统计循环次数需要加上二分查找的循环次数
        while move_index > insert_index: #移动元素，直到待插入位置处
            count+=1
            data_list[move_index] = data_list[move_index - 1]
            move_index -= 1
        data_list[insert_index] = wait_insert_data #插入操作
        print(data_list)
    print(f"总循环次数为 {count}")
    return data_list
def binary_search(data_list,data):    
    """
    输入:有序列表，和待查找的数据data
    输出：data 应该在该有序列表的插入位置
    count 变量纯粹是为了统计循环次数而使用的，实际应用时可去除。
    """
    count = 0
    length = len(data_list)
    low = 0
    high = length-1
    ##如果给定元素大于等于最后一个元素，则插入最后元素位置的后面
    ##如果小于第一个元素，则插入位置0 
    if data >= data_list [length -1]: return length,0
    elif data < data_list [0]: return 0,0
    insert_index = 0 
    while low < high-1:
        count +=1
        mid = (low + high)//2 #python中的除法结果默认为浮点数取整数部分时使用 //
        if data_list[mid] > data:
            high = mid
            insert_index = high
        else:
            low = mid
            insert_index = low+1  #如果值相同或者值大于mid的值，那么插入位置位于其后面
    return insert_index,count

if __name__ == "__main__":
    unsort = [1,3,4,2,1,5,6,7,8,4]
    print(*insert_sort2(unsort))
    
#希尔排序实现，假如数据的长度为 n 我就简单地采取除以 2 来求步长，最后到 1 结束，最终也可以达到效果，分别使用 for 循环和 while 循环来实现
    '''
    思想：分治策略
   使用 for 循环
    '''
def shell_sort(data_list):
    length = len(data_list)
    space  = length//2
    while space > 0:
        for i in range(space,length ): #默认第一个位置的元素是已排序区间，因此下标从 1 开始
            tmp = data_list[i] #待插入的数据
            index = i 
            for j in range(i-space,-1,-space): #从已排序区间查找插入位置
                if tmp < data_list[j]:
                    data_list[j+space] = data_list[j]  #元素向后移动，腾出插入位置
                    index = j #最后的j即为插入的位置
                else:
                    break
            data_list[index] = tmp #插入操作
            print(data_list)
        space = space // 2
    return data_list

def shell_sort2(data_list):
    '''
    思想：分治策略
    使用 while 循环
    '''
    length = len(data_list)
    space  = length//2
    while space > 0:
        i = space
        while i < length: #默认第一个位置的元素是已排序区间，因此下标从 1 开始
            tmp = data_list[i] #待插入的数据
            j = i
            while j >= space and data_list[j - space] > tmp: #从已排序区间查找插入位置
                data_list[j] = data_list[j-space]  #元素向后移动，腾出插入位置                    
                j -= space
            data_list[j] = tmp #插入操作
            print(data_list)
            i +=1
        space = space // 2
    return data_list
unsort = [9,8,7,6,5,4,3,2,1]
print(*shell_sort(unsort)) 
unsort = [9,8,7,6,5,4,3,2,1]
print(*shell_sort2(unsort))

#归并排序代码
def merge_sort(data_list):
    '''
    归并排序程序入口
    '''
    length = len(data_list)
    merge_sort_c(data_list,0,length)

def merge_sort_c(data_list,p,q):
    '''
    递归调用
    '''
    #退出条件
    if p+1>=q:
        return 
    else:
        r = (p+q)//2 
        merge_sort_c(data_list,p,r)
        merge_sort_c(data_list,r,q)
        merge(data_list,p,r,q)  #将data_list[p:r] 与 data_list[r:q] 按顺序归并到 data_list 相应位置

def merge(data_list,p,r,q):
    '''
    归并函数
    例如 data_list[p:q] = [...,1,4,2,3,...]
    data_list[p:r] = [1,4]
    data_list[r:q] = [2,3]
    tmp = [1,2,3,4]
    归并后 data_list[p:q] = [...,1,2,3,4,...]     
    '''
    tmp = []    
    i = p
    j = r 
    while i < r and j < q:
        if data_list[i] <= data_list[j]:
            tmp.append(data_list[i])
            i+=1
        else:
            tmp.append(data_list[j])
            j+=1

    while i < r :
        tmp.append(data_list[i])
        i+=1

    while j < q:
        tmp.append(data_list[j])
        j+=1

    #将 tmp 数据复制到 data_list
    for tmp_index,index in enumerate(range(p,q)):
        data_list[index] = tmp[tmp_index]
if __name__ == "__main__":
    data_list = [38, 50, 63, 27, 89, 94, 11, 82, 9, 13]
    print(data_list)
    merge_sort(data_list)
    print(data_list)
    
#使用哨兵的 merge 函数如下所示：

def merge2(data_list,p,r,q):
    '''
    利用哨兵的归并函数
    例如 data_list[p:q] = [...,1,4,2,3,...]
    part_left = [1,4]
    part_right = [2,3]
    归并后 data_list[p:q] = [...,1,2,3,4,...] 
    '''
    part_left = [data_list[index] for index in range(p,r)]  #临时数组保存左部分
    part_right = [data_list[index] for index in range(r,q)] #临时数组保存右部分

    #对左边部分或右边部分增加哨兵，哨兵为待排序数据的最大值如99999
    max_value = 99999
    part_left.append(max_value)
    part_right.append(max_value)
    i = 0
    j = 0
    k = p
    # while i != r-p: # 也可以这样写，看自己喜好
    while part_left[i] != max_value:
        if part_left[i] <= part_right[j]:
            data_list[k] = part_left[i]
            i += 1
        else:
            data_list[k] = part_right[j]
            j += 1
        k +=1 #依次从左边部分和右边部分按顺序抽取数据
#快速排序实现
#encoding=utf-8
import random

def quick_sort(data_list):
    length = len(data_list)
    quick_sort_c(data_list,0,length-1)

def quick_sort_c(data_list,begin,end):
    """
    可以递归的函数调用
    """
    if begin >= end:
        return
    else:
        #获取分区数据partition_data最后的下标
        index = partition(data_list,begin,end)
        print(data_list)
        quick_sort_c(data_list,begin,index-1)
        quick_sort_c(data_list,index+1,end)

def partition(data_list,begin,end):
    #选择最后一个元素作为分区键
    partition_key = data_list[end]

    #index为分区键的最终位置
    #比partition_key小的放左边，比partition_key 大的放右边
    index = begin 
    for i in range(begin,end):
        if data_list[i] < partition_key: 
            data_list[i],data_list[index] = data_list[index],data_list[i] 
            index+=1

    data_list[index],data_list[end] = data_list[end],data_list[index] 
    return index


if __name__ == "__main__":
    data_list = [random.randint(0,100) for i in range(10)]
    # data_list = [25, 77, 52, 49, 85, 28, 1, 28, 100, 36]
    print("原始数组:", data_list)
    print("排序过程如下")
    quick_sort(data_list)
    print("最终结果:",data_list)
#查找第k大
def find_top_k(data_list,K):
    length = len(data_list)
    begin = 0
    end = length-1
    index = partition(data_list,begin,end) #这里的partition函数就是上面快排用到的函数
    while index != length - K:
        if index >length - K:
            end = index-1
            index = partition(data_list,begin,index-1)
        else:
            begin = index+1
            index = partition(data_list,index+1,end)
    return data_list[index]

data_list = [25, 77, 52, 49, 85, 28, 1, 28, 100, 36]
for i in [1,2,3,4,5]:
    print(f"第 {i} 大元素是 {find_top_k(data_list,i)}")
    
    
#桶排序实现
#encoding = utf-8
import random
from quick_sort import quick_sort

DEFAULT_BUCKET_SIZE = 5 

def bucket_sort(data_list,bucket_size = DEFAULT_BUCKET_SIZE):
    length = len(data_list)
    min = max = data_list[0]

    #寻找最小值和最大值
    for i in range(0,length):
        if data_list[i] < min:
            min = data_list[i]
        if data_list[i] > max:
            max = data_list[i]

    #定义多个桶并初始化
    num_of_buckets = (max - min) // bucket_size +1 
    buckets = []
    for i in range(num_of_buckets):
        buckets.append([])

    #将数据放入桶中
    for i in range(0,length):
        buckets[(data_list[i] - min)//bucket_size ].append(data_list[i])

    #依次对桶内数据进行快速排序
    data_list.clear()

    for i in range(num_of_buckets):
        print(f"第{i}个桶排序前的内容是{buckets[i]}")
        quick_sort(buckets[i])
        # print(f"第{i}个桶排序后的内容是{buckets[i]}")
        for data in buckets[i]:
            data_list.append(data) 

if __name__ == "__main__":
    data_list = [random.randint(0,15) for _ in range(0,15)]
    print(data_list)
    bucket_sort(data_list)
    print(data_list)

    
#计数排序实现
def counting_sort(data_list):
    length = len(data_list)

    #定义桶
    bucket = [] 
    max = data_list[0]
    for d in data_list:
        if d > max:
            max = d
    #初始化
    for i in range(max+1):
        bucket.append(0)

    #计数
    for i in range(length):
        bucket[data_list[i]] = bucket[data_list[i]] + 1

    ##累加
    for i in range(1,max+1):
        bucket[i] = bucket[i]+bucket[i-1]

    #计数排序,定义结果数组并初始化
    result = []
    for i in range(length):
        result.append(0)

    #从尾至头查找分数在result的插入位置，如果从头到尾的话就不是稳定的排序算法。
    for i in range(length-1,-1,-1):
        result[bucket[data_list[i]]-1] = data_list[i]
        bucket[data_list[i]] = bucket[data_list[i]] -1

    #将结果复制到原来的数组中，达到修改传入数组的效果
    for i in range(length):
        data_list[i] = result[i]


if __name__ == "__main__":
    data_list = [2,5,3,0,2,3,0,3]
    print(data_list)
    counting_sort(data_list)
    print(data_list)

#基数排序实现
#encoding=utf-8
import random

class phone_num(object):

    num = ""

    def __init__(self,num=""):
        self.num = num

    def get_bit(self,bit):
        return int(self.num[bit-1:bit])

    def __str__(self):
        return self.num

    def __repr__(self):
        return self.num

def radix_sort(data_list):
    radix = 11
    ##借助稳定排序算法从尾至头排序 radix 次
    for i in range(radix,0,-1):
        counting_sort(data_list,i)

#改写的计数排序，方便基数排序调用,radix 指示是待排序数据的哪一位
def counting_sort(data_list,radix):
    length = len(data_list)
    #定义桶
    bucket = [] 
    max = data_list[0].get_bit(radix)
    for i in range(length):
        if data_list[i].get_bit(radix) > max:
            max = data_list[i].get_bit(radix)

    #初始化
    for i in range(max+1):
        bucket.append(0)

    #计数
    for i in range(length):
        bucket[data_list[i].get_bit(radix)] = bucket[data_list[i].get_bit(radix)] + 1

    ##累加
    for i in range(1,max+1):
        bucket[i] = bucket[i]+bucket[i-1]

    #计数排序,定义结果数组并初始化
    result = []
    for i in range(length):
        result.append(0)

    #从尾至头查找分数在result的插入位置，如果从头到尾的话就不是稳定的排序算法。
    for i in range(length-1,-1,-1):
        result[bucket[data_list[i].get_bit(radix)]-1] = data_list[i]
        bucket[data_list[i].get_bit(radix)] = bucket[data_list[i].get_bit(radix)] -1

    #将结果复制到原来的数组中，达到修改传入数组的效果
    for i in range(length):
        data_list[i] = result[i]

def create_phone_num():
    prelist = ["130", "131", "132", "133", "134", "135", "136", "137", "138", "139", "147", "150", "151", "152",
               "153", "155", "156", "157", "158", "159", "186", "187", "188"]
    randomPre = random.choice(prelist)
    Number = "".join(random.choice("0123456789") for i in range(8))
    phoneNum = randomPre +Number
    return phoneNum

if __name__ == "__main__":
    data_list = [phone_num(create_phone_num()) for _ in range(10)]
    print("排序前")
    for i in data_list:
        print(i)

    radix_sort(data_list)

    print("排序后")
    for i in data_list:
        print(i)
#leetcode 21
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        cur = dummy
        while l1 != None or l2 != None:
            # l1链表已经取完
            if l1 == None:
                cur.next = l2
                break
            # l2链表已经取完
            if l2 == None:
                cur.next = l1
                break

            if l1.val >= l2.val:
                cur.next = ListNode(l2.val)
                cur = cur.next
                l2 = l2.next
            else:
                cur.next = ListNode(l1.val)
                cur = cur.next
                l1 = l1.next
        return dummy.next
        
#leetcode 23
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        k = len(lists)
        if k == 0:
            return None

        interval = 1
        # 两两合并
        while interval < k:
            for i in range(0,k,interval*2):
                # 最后落单的链表直接保留
                if i + interval < k:
                    lists[i] = self.mergeLists(lists[i],lists[i+interval])
            interval *= 2
        
        return lists[0]
        
    # 合并两个链表函数
    def mergeLists(self,l1,l2):
        dummy = ListNode(0)
        cur = dummy

        while l1 != None or l2 != None:
            if l1 == None:
                cur.next = l2
                break
            if l2 == None:
                cur.next = l1
                break

            if l1.val < l2.val:
                cur.next = ListNode(l1.val)
                cur = cur.next
                l1 = l1.next
            else:
                cur.next = ListNode(l2.val)
                cur = cur.next
                l2 = l2.next
        
        return dummy.next
#leetcode 148
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 递归终止条件
        if head == None:
            return None
        
        if head.next == None:
            return head

        # 双指针寻找链表中点
        slow = head
        fast = head

        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next

        # 中点处切断链表，得到两个链表
        mid = slow.next
        slow.next = None

        # 递归
        l1 = self.sortList(head)
        l2 = self.sortList(mid)
        return self.merge(l1,l2)

    # 合并函数
    def merge(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy
        while l1 != None or l2 != None:
            # l1链表已经取完
            if l1 == None:
                cur.next = l2
                break
            # l2链表已经取完
            if l2 == None:
                cur.next = l1
                break

            if l1.val >= l2.val:
                cur.next = ListNode(l2.val)
                cur = cur.next
                l2 = l2.next
            else:
                cur.next = ListNode(l1.val)
                cur = cur.next
                l1 = l1.next
        return dummy.next
        