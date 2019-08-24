""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37.1
工具： python == 3.7.3
"""

"""
思路:
    数字N如果是奇数，它的约数必然都是奇数；若为偶数，则其约数可奇可偶。
    无论N初始为多大的值，游戏最终只会进行到N=2时结束，那么谁轮到N=2时谁就会赢。
    因为爱丽丝先手，N初始若为偶数，爱丽丝则只需一直选1，使鲍勃一直面临N为奇数的情况，这样爱丽丝稳赢；
    N初始若为奇数，那么爱丽丝第一次选完之后N必为偶数，那么鲍勃只需一直选1就会稳赢。
    综述，判断N是奇数还是偶数，即可得出最终结果！
结果：
    执行用时 : 40 ms, 在所有 Python3 提交中击败了96.94%的用户
    内存消耗 : 13.7 MB, 在所有 Python3 提交中击败了100%的用户
"""

class Solution:
    def divisorGame(self, N):
        return N%2==0

if __name__ == "__main__":
    N = 3
    answer = Solution().divisorGame(N)
    print(answer)


