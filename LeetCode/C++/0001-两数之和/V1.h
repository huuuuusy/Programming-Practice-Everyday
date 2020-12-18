/*
@Author: huuuuusy
@GitHub: https://github.com/huuuuusy
系统： Ubuntu 18.04
IDE:  VS Code 1.36
工具： GCC == 7.4.0
*/

/* 
思路:
    暴力解法
结果：
    执行用时 : 212 ms, 在所有 C++ 提交中击败了38.82%的用户
    内存消耗 : 9.2 MB, 在所有 C++ 提交中击败了91.43%的用户
*/

#include <vector>
using std::vector;
#include <unordered_map>
using std::unordered_map;

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        int i,j;
        for(i = 0; i < nums.size()-1; i++){
            for(j = i+1; j < nums.size(); j++){
                if(nums[i] + nums[j] == target){
                    return {i,j};
                }
            }
        }
        return {i,j};
    }
};