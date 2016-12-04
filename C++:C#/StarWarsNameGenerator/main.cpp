
#starwars name generator llol

#include <iostream>
#include <string>
using namespace std;

int main(int argc, char *argv[]) {
    string first_name;
    string last_name;
    string mothers_maiden_name;
    string home_town_name;

    cout << "Example Program from LEcture 5" << endl;
    cout << endl << "What is your frist name ";
    cin >> first_name;
    cout << " What is your last name: ";
    cin >> last_name;
    cout << "What is your mothers maiden name? ";
    cin >> mothers_maiden_name;
    cout << "What is the name of your hometown? ";
    cin >> home_town_name;
    cout << endl << "Hello " << first_name <<
                                " " << last_name << endl;
    cout << "You were born in " << home_town_name << endl;
    cout << "and your mother's maiden name is: " <<
            mothers_maiden_name << endl;

    string part1 = last_name.substr(0, 3),
            part2 = first_name.substr(0, 3),
            part3 = mothers_maiden_name.substr(0, 2),
            part4 = home_town_name.substr(0, 3);


    string star_wars_name;

    part2[0] = tolower(part2[0]);
    part4[0] = tolower(part4[0]);

    star_wars_name = part1 + part2 + " " + part3 + part4;
    cout << "You're star wars name is " << star_wars_name;







    return 0;
}