//
// Created by Bryar Cole on 10/13/15.
//

#ifndef POOL_POOLBALL_H
#define POOL_POOLBALL_H


class POOLBALL {
private:
    int radius = 5;
    int xPos, yPos, xVel, yVel;
public:
    int getRadius(void);
    POOLBALL(void);
    POOLBALL(int radius);
    POOLBALL(int radius, int xPos, int yPos, int xVel, int yVel);




};


#endif //POOL_POOLBALL_H
