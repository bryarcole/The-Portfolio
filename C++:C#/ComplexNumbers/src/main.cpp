
/* Creator: Bryar Cole
 * Date: 11/6/2015
 * Course: COSC 1337
 * Purpose: Combine like terms of Imaginary numbers
 * Resources utilized; http://stackoverflow.com/questions/23335209/error-overloaded-operator-must-be-a-binary-operator-has-3-parameters
 * http://www.learncpp.com/cpp-tutorial/92-overloading-the-arithmetic-operators/
 *
 */


#include <iostream>
#include "../include/Complex.h"
using namespace std;

int main( int argc, char * argv[] ) {

    Complex a(2.0, 4.0);
    Complex b(7.0, 2.0);
    Complex c(3, 5);
    Complex d(4, 3);
    Complex e(9.2);
    Complex f(2, 11);
    Complex g(4);

    cout << "Addition: " << endl;
    cout << (a + b + c) + (a + b) << " " << (e + c) + (b + c) << endl;
    cout << "Suptraction: " << endl;
    cout << b - d - e - c << " " << (d - e) - (b - c) << " " << b - a << endl;
    cout << "Multipcation: " << endl;
    cout << a + c + a * d + e * d + f * c << " " << (a * c - b * d) << endl;
    cout << "Division: " << endl;
    cout << g * (a + b) / (c + d) << " " <<
            (a * c + b * d) / (c * c + d * d) + (b * c - a * d) / (c * c / d * d)  << endl;
    cout << "Messing Around: " << endl;
    cout << g * (a + b) << " " << 86 + a << " " << f +34 << endl;

}