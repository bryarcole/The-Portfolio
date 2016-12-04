#include <iostream>
#include "Graphics.h"
#include "Highway.h"
#include "Vehicle.h"
#include "Random.h"

using namespace std;
int cycles = 0;
Highway I35;

int xRoad = 50;
int yRoad = 50;

const int MAX_CARS = 10;
Vehicle cars[MAX_CARS];
Random sim_rand;

void init_veh(int car) {
    int xCar, yCar, sCar, lane;

    sim_rand.seed();
    //ine
        sCar = I35.speed + sim_rand.get_random(0,3);
        cars[car].setSpeed(sCar, 0);

        lane = sim_rand.get_random(0, I35.lanes -1);

        xCar = xRoad + sim_rand.get_random(0, 100);

        yCar = yRoad + I35.lWidth/2 + lane * I35.lWidth;
        cars[car].setPosition(xCar, yCar);
    }


void trafficSetup(void) {
    for (int c = 0; c < MAX_CARS; c++)
        init_veh(c);
}






int xPos = xRoad;
int yPos = yRoad + I35.lWidth/2;
int xSpeed = I35.speed;
int ySpeed = 0;

Vehicle car;

}

void drawLanes(void){
    int X0 = xRoad;
    int X1 = xRoad + I35.length;
    int Y0 = yRoad;
    int y;
    setColor(BLACK);
    for (int lane = 0; lane < (I35.lanes +1); lane++){
        y = Y0 + (lane * I35.lWidth);
        drawLine(X0, y, X1, y);
    }
}

void drawVehicle(int lane){
    //lanes numbers start at 1
    int y0 = yRoad + (lane -1) * I35.lWidth + I35.lWidth/2;
    setColor(RED);
    drawFilledCircle(xPos, y0, 5);

}

void drawScene(void){
    clearWindow();
    drawLanes();
    drawVehicle(1);
    glutSwapBuffers();

}

void animate(){
    //move your objects here
    car.move();
    xPos += xSpeed;
    yPos += ySpeed;
    if(xPos > (xRoad + I35.length)) exit(0);
    glutPostRedisplay();
    pause_ms(16);
    cycles++;

}

void handleKey(unsigned char key, int x, int y){
    switch(key){
        case 'q':
            exit(0);
            break;
    }
}


int main(int argc, char **argv) {
    trafficSetup();
    graphicsSetup(argc, argv);
    glutDisplayFunc(drawScene);
    glutIdleFunc(animate);
    glutKeyboardFunc(handleKey);
    glutMainLoop();

    return 0;
}