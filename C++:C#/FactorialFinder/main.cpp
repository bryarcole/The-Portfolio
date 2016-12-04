#include <iostream>

using namespace std;

int factorfinder(int x){
    if (x==1) {
        return 1;
    }else{
        return x*factorfinder(x-1);
    }
}

int main()
{
    int Y = 40;
    cout << factorfinder(5);


}