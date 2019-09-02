/*
@Author:huuuuusy
@GitHub:https://github.com/huuuuusy
系统:Ubuntu 18.04
IDE:VS Code 1.37
工具:GCC == 7.4.0
内容:使用while打印10~0之间的整数
*/

# include <iostream>

int main(){
    int i = 10;
    while(i>=0){
        std::cout <<i<<" ";
        i--;
    }
    std::cout <<std::endl;
    return 0;
}