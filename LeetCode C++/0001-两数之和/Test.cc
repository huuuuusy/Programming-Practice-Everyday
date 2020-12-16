#define CATCH_CONFIG_MAIN
#include "../Catch2/single_include/catch2/catch.hpp"

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

int main()
{
    Solution s;
    vector<int> v1{2, 7, 11, 15};
    ans = s.twoSum(v1, 9);
    cout << ans;
}
