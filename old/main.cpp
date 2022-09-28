// program to run basic programs

#include <iostream>
#include <cstdlib>
#include <cstring>
#include <sys/stat.h>
#include <unistd.h>
#include <fstream>
// #include "test copy.cpp"

inline bool fileexists(const std::string& name)
{
    // https://stackoverflow.com/questions/12774207/fastest-way-to-check-if-a-file-exists-using-standard-c-c11-14-17-c
    // LOL
    struct stat buffer;   
    return (stat (name.c_str(), &buffer) == 0); 
}

void clearconsole()
{
    for (int i = 0; i <60; i++)
    {std::cout<<"\n";}
}

int rungame(std::string filename)
{
    std::string prefix = "./gamelib/";
    std::string combo = prefix + filename;
    char c[combo.length()+1];
    std::strcpy(c, combo.c_str());
    if (fileexists(c))
    {
    clearconsole();
    std::system(c);
    return 0;
    }
    return 1;
}


int main()
{
    std::cout << "\nGame list:\n";
    std::system("cd gamelib && ls");
    std::cout << "Pick a game:\n";
    std::string filename;
    std::cin >> filename;
    if (rungame(filename))
    {
        std::cout << "\nerror, missing file\n";
        main();
        return 0;
    }
    std::cout << "main.cpp exit\n";
    return 0;
}