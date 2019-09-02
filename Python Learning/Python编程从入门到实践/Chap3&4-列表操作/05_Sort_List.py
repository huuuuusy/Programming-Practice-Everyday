""" 
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy

系统： Ubuntu 18.04
IDE:  VS Code 1.35.1
工具： python == 3.7.3
任务： 对列表进行排序操作
"""

"""不改变原始列表的排序"""

# 将这些地方存储在一个列表中，并确保其中的元素不是按字母顺序排列的
locations = ['himalaya', 'andes', 'tierra del fuego', 'labrador', 'guam']

# 按原始排列顺序打印该列表
print("Original order:")
print(locations)

# 使用sorted()按字母顺序打印这个列表，同时不修改它
print("\nAlphabetical:")
print(sorted(locations))

# 使用sorted()按与字母顺序相反的顺序打印这个列表，同时不修改它
print("\nReverse alphabetical:")
print(sorted(locations, reverse=True))

"""改变原始列表的排序"""

# 使用reverse()修改列表元素的排列顺序;打印该列表，核实排列顺序确实变了
print("\nReversed:")
locations.reverse()
print(locations)

# 使用reverse()再次修改列表元素的排列顺序;打印该列表，核实已恢复到原来的排列顺序
print("\nOriginal order:")
locations.reverse()
print(locations)

# 使用sort()修改该列表，使其元素按字母顺序排列。打印该列表，核实排列顺序确实变了
print("\nAlphabetical")
locations.sort()
print(locations)

# 使用sort()修改该列表，使其元素按与字母顺序相反的顺序排列。打印该列表，核实排列顺序确实变了
print("\nReverse alphabetical")
locations.sort(reverse=True)
print(locations)