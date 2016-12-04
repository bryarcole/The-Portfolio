cmake_minimum_required(VERSION 3.2)
project(Functioncalltest)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES main.cpp)
add_executable(Functioncalltest ${SOURCE_FILES} hello.h hello.cpp Homework/LinkedList/lib/Node.h Homework/LinkedList/lib/Node.cpp)