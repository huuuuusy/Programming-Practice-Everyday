""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 
工具： python == 3.7.6
介绍： 深度之眼《Python高手之路》作业08：迭代生成
"""

"""
练习
解决八皇后问题：国际象棋棋盘是8 * 8的方格，每个方格里放一个棋子。皇后这种棋子可以攻击同一行或者同一列或者斜线（左上左下右上右下四个方向）上的棋子。在一个棋盘上如果要放八个皇后，使得她们互相之间不能攻击（即任意两两之间都不同行不同列不同斜线），求出布局方式。
"""

def conflict(chesses_placed, next_chess_xcor):
    """
    接受用状态元组表示的既有皇后的位置，并确定下一个皇后的位置是否会导致冲突。
    :param chesses_placed: 存放已经摆放的棋子的位置
    :param next_chess_xcor: 下一个棋子的x坐标（列坐标）
    :return: 如果下一个皇后与当前皇后的 x 坐标相同或在同一条对角线上，将发生冲突，因此返回True ；如果没有发生冲突，就返回False 。
    """
    # get the next y coordinate by chessed placed下一个棋子的y坐标（行坐标）
    next_chess_ycor = len(chesses_placed)

    # use next chess y coordinate to confirm the count of loop
    for i in range(next_chess_ycor):

        # 表示两个皇后的x距离（为0或等于y距离）时为真、否则为假
        if abs(chesses_placed[i] - next_chess_xcor) in (0, abs(i - next_chess_ycor)):
            return True
    return False


def place_queens(num=8, chesses_placed_tuple=()):
    """
    This is a placing queens function defined
    :param num: the count of queens
    :param chesses_placed_tuple: such as (1, 5, 0)
    :return: a generator
    处理好基线条件后，可在递归条件中假设来自更低层级（编号更大的皇后）的结果都是正确的。因此，只需在函数place_queens的基线条件的另一分支返回当前层级的所有正确结果。
    """
    for i in range(num):
        if not conflict(chesses_placed_tuple, i):

            # 基线条件：最后一个皇后。如果当前已经摆放到最后一个皇后（len(chesses_placed_tuple) == num-1），找到所有不冲突的位置，并返回（yield (i,)）
            if len(chesses_placed_tuple) == num - 1:
                yield (i,)
            else:

                # get one bye one element from the generator
                for j in place_queens(num, chesses_placed_tuple + (i,)):
                    # superimpose elements to the newest tuple
                    yield (i,) + j


res = list(place_queens(4))
print(res)
print(len(res))
