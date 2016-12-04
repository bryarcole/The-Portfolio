//
// Created by Bryar Cole on 12/14/15.
//

#include "Random.h"

#include <cstdlib>
#include <iostream>
using namespace std;
#include "Random.h"

void Random::seed(void){
    srand((unsigned) time(0));
}

int Random::get_random(int min, int max) {
int range = max - min + 1;
return min + (rand() % range);
}