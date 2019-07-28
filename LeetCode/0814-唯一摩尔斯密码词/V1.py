""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： python == 3.7.3
"""

"""
思路:
    利用字典和set，字典保存键值，set剔除重复密码
结果：
    执行用时 : 52 ms, 在所有 Python3 提交中击败了72.4%的用户
    内存消耗 : 13.9 MB, 在所有 Python3 提交中击败了5.01%的用户
"""

class Solution:
    def uniqueMorseRepresentations(self, words):
        dict={'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
        word_cag = []
        for  i,j in enumerate(words):
            emp=''
            j=list(j)
            for n,m in enumerate(j):
                emp += dict[m]
            word_cag.append(emp)
        return len(set(word_cag))


if __name__ == "__main__":
    words = ["gin", "zen", "gig", "msg"]
    answer = Solution().uniqueMorseRepresentations(words)
    print(answer)