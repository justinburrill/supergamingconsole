#include <iostream>
#include <cstdlib>
#include <cstring>
// #include "test copy.cpp"

void clearconsole()
{
    for (int i = 0; i <60; i++)
    {std::cout<<"\n";}
}

int main()
{
    std::cout << "Game list:\n";
    std::system("cd gamelib && ls");
    std::cout << "Pick a game:\n";
    std::string filename;
    std::cin >> filename;
    std::string prefix = "./gamelib/";
    std::string combo = prefix + filename;
    char c[combo.length()+1];
    std::strcpy(c, combo.c_str());
    clearconsole();
    std::system(c);
    std::cout << "main.cpp exit\n";
    return 0;
}