""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路：
    用left=0，right标记第一个数字和最后一个数字出现的位置
    首先strip()去掉左右的空格
    然后判断第一个字符是不是正负号，是的话left置为1
    判断left后一个字符是否为数字，不是直接返回0
    遍历不断更新right，找到第一个不是数字的字符后break
    用res=str[left:right+1]提取纯数字字符串
    需要注意的是，可能数字全为0.所以用lstrip()将左边的0清除
    最后利用eval()函数将双引号去除，并判断是否需要填正负号
结果：
    执行用时 : 52 ms, 在所有 Python3 提交中击败了91.89%的用户
    内存消耗 : 13.1 MB, 在所有 Python3 提交中击败了91.91%的用户
"""

class Solution:
    def myAtoi(self, str):
        str = str.strip()
        if str == '':
            return 0
        # 左右指针
        left = 0
        right = 0 
        # 上下界
        maxi=2147483647
        mini=-2147483648
        # 判断第一个字符是否为正负号
        if str[0] == '+' or str[0] == '-':
            left = 1
        if (left==1 and len(str)==1) or str[left]<'0' or str[left]>'9': 
            return 0
        for i in range(left,len(str)):#right移动到第一个不是数字的地方
            if str[i]>='0' and str[i]<='9':
                right=i
            else:
                break
        res=str[left:right+1].lstrip('0')#去除左边的0
        if len(res)==0:
            return 0#清除后可能没数字
        else :
            res=eval(res)
        if left==1 and str[0]=='-':#判断正负
            res=-res
        if res>maxi: 
            return maxi
        elif res<mini: 
            return mini
        else :
            return res

if __name__ == "__main__":
    str = "   +42"
    answer = Solution().myAtoi(str)
    print(answer)
