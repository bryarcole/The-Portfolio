cmake_minimum_required(VERSION 3.2)
project(Lab3Classes)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES main.cpp)
add_executable(Lab3Classes ${SOURCE_FILES} People.cpp People.h)