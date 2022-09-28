// old test program stripped to just running other exes

#include <iostream>
#include <cstdlib>
#include <cstring>
#include <sys/stat.h>
#include <unistd.h>
#include <fstream>

//# include qt shit


inline bool fileexists(const std::string& name)
{
    // https://stackoverflow.com/questions/12774207/fastest-way-to-check-if-a-file-exists-using-standard-c-c11-14-17-c
    // LOL
    struct stat buffer;   
    return (stat (name.c_str(), &buffer) == 0); 
}

int rungame(std::string filename)
{
    std::string prefix = "./gamelib/";
    std::string combo = prefix + filename;
    char c[combo.length()+1];
    std::strcpy(c, combo.c_str());
    if (fileexists(c))
    {
    std::system(c);
    return 0;
    }
    return 1;
}

int main()
{

    return 0;
}