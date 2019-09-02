/*
@Author:huuuuusy
@GitHub:https://github.com/huuuuusy
系统:Ubuntu 18.04
IDE:VS Code 1.37
工具:GCC == 7.4.0
内容:使用while对50～100的整数求和
*/

# include <iostream>

int main(){
    int sum = 0;
    int i = 50;
    while(i<=100){
        sum += i;
        i++;
    }
    std::cout <<"the result is:"<<sum<<std::endl;
    return 0;
}