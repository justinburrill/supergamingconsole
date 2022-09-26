#include <iostream>
#include <time.h>
int main()
{
    srand(time(NULL));
    int num = rand()%100;
    int guesscount = 0;
    bool solved = false;
    while (!solved)
    {

        std::cout << "Enter a number from 1-100:\n";
        int x;
        std::cin >> x;
        guesscount++;
        if (x == num) 
        {
            solved = true;
            std::cout << "You got it!\n Guess count:" <<guesscount<< std::endl;
            
        }
        else if (x < num)
        {
            std::cout << "Too low!\n";
        }
        else if (x > num)
        {
            std::cout << "Too high!\n";
        }
    }
    return 0;
}