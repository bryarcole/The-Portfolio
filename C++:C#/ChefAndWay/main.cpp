#include <iostream>
#include <sstream>
#include <string>


using namespace std;

int main(){
    string K, N;
    int num;

    while((cout << "Please enter a number: ")
        && getline(cin, K)
        && !(istringstream{K} >> num)
            ){
        cerr << "Invald input, try again." << endl;
    }



}