//
// Created by Bryar Cole on 12/14/15.
//

#include "Vehicle.h"
#include <iostream>
using namespace std;

Vehicle::Vehicle() {
    xPos = 0;
    yPos = 0;
    xSpeed = 0;
    ySpeed = 0;
    size = 5;

}

void Vehicle::setPosition(int x, int y) {
    xPos = x;
    yPos = y;

}

void Vehicle::setSpeed(int xv, int yv) {
    xSpeed = xv;
    ySpeed = yv;


}

void Vehichle::move(void){
    xPos += xSpeed;
    yPos += ySpeed;
    cout << xPos << " " << yPose << endl;
}