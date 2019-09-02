/*
@Author:huuuuusy
@GitHub:https://github.com/huuuuusy
系统:Ubuntu 18.04
IDE:VS Code 1.37
工具:GCC == 7.4.0
内容:输入两个整数，打印两个整数之间的所有值
*/

# include <iostream>

int main(){
    std::cout << "please enter 2 integers:";
    std::cout <<std::endl;
    int v1, v2;
    std::cin >> v1 >> v2;
    if(v1>v2){
        while(v1>=v2){
            std::cout <<v1<<" ";
            v1--;
        }
    }
    else{
        while(v1<=v2){
            std::cout <<v1<<" ";
            v1++;
        }
    }
    std::cout <<std::endl;
    return 0;
}