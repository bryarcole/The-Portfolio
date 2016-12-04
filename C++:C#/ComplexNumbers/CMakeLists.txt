cmake_minimum_required(VERSION 3.2)
project(ComplexNumbers)

set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -std=c++11")

set(SOURCE_FILES
    include/catch.hpp
    include/Complex.h
    src/Complex.cpp
    src/main.cpp
    tests/test_complex.cpp
    tests/test_main.cpp
    make.deps
    Makefile)

add_executable(ComplexNumbers ${SOURCE_FILES})