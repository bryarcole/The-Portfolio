// Complex.h - complex number class
#include <iostream>
#include <string>
using namespace std;

class Complex {
    private:
        double r;       // real part
        double i;       // imaginary part

    public:
        Complex();      // default constructor
        Complex( double r, double i );  // normal constructor
        Complex( double r );            // alternate constructor
        
        string toString( void );
        Complex operator + ( const Complex &rhs );
        Complex operator - ( const Complex &rhs );
        Complex operator * ( const Complex &rhs );
        Complex operator / ( const Complex &rhs );

    //Operators:
        friend ostream & operator << ( ostream & lhs, const Complex & rhs );
        friend Complex operator + (double rhs, const Complex &lhs);
        friend Complex operator - (double lhs, const Complex &rhs);
        friend Complex operator + (double lhs, const Complex &rhs);
        friend Complex operator - (const Complex &lhs, double rhs);
        friend Complex operator * (double lhs, const Complex &rhs);
        friend Complex operator * (double rhs, const Complex &lhs);
        friend Complex operator / (const Complex &rhs, double lhs);
        friend Complex operator / (double rhs, const Complex &lhs);




};


