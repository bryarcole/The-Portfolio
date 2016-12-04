//
// Created by Bryar Cole on 9/22/15.
//

#ifndef LAB3CLASSES_PEOPLE_H
#define LAB3CLASSES_PEOPLE_H
#include <string>


using namespace std;



class People {

private:
    string first_name;
    string last_name;
    string maiden_name;
    string birth_town;

public:
    void set_name(string first_name, string last_name);
    void set_maiden(string maiden_name);
    void set_birth(string birth_town);

    string gen_star_wars(void);


};



#endif //LAB3CLASSES_PEOPLE_H
