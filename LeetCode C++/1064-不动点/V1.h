/*
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.37
工具： GCC == 7.4.0
*/

/* 
思路:
    二分法
结果：
    执行用时 : 20 ms, 在所有 C++ 提交中击败了47.06%的用户
    内存消耗 : 9.7 MB, 在所有 C++ 提交中击败了100%的用户
*/

#include <vector>
using std::vector;

class Solution {
public:
    int fixedPoint(vector<int>& A) {
        int left = 0; //左边界
        int right = A.size() - 1;　//右边界是数组长度  
        while(left < right){
            int mid = (left + right) / 2; //左中位数
            if(A[mid] < mid){　//如果中间数的数值小于索引，说明左边界以外的数字可以排除，左边界收缩
                left = mid + 1;   
            }
            else{
                right = mid; //否则中间数为右边界　
            }
        }
        if(A[left] == left){　//判断是否找到
            return left;
        }
        else{
            return -1;
        }
    }
};