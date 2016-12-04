//
// Created by Bryar Cole on 12/14/15.
//

#ifndef ANIMATITINGI35_VEHICLE_H
#define ANIMATITINGI35_VEHICLE_H


class Vehicle {

public:
    int size;
    int xPos;
    int yPos;
    int xSpeed;
    int ySpeed;

    Vehicle();
    void setPosition(int x, int y);
    void setSpeed(int xv, int yv);

    void move(void);



};


#endif //ANIMATITINGI35_VEHICLE_H
