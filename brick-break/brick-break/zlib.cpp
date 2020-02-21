//
//  zlib.cpp
//  sfml tut
//
//  Created by Zeeshan Hooda on 2/17/20.
//  Copyright © 2020 Deceptive Labs. All rights reserved.
//


#include <iostream>
#include <string>
#include "zlib.hpp"

namespace zlib {

std::string input(std::string prompt) {
    std::string output;
    std::cout << prompt;
    std::getline(std::cin, output);
    return output;
}

void print(std::string input) {
    std::cout << input << std::endl;
}

void print(std::string input, std::string end) {
    std::cout << input << end;
}

void Log(int type, std::string input) {
    if (type == 1) {
        std::cout << "[INFO]: " << input << std::endl;
    } else if (type == 2) {
        std::cout << "[WARNING]: " << input << std::endl;
    } else if (type == 3) {
        std::cout << "[ERROR]: " << input << std::endl;
    }
}

void Log(int type, int input) {
    if (type == 1) {
        std::cout << "[INFO]: " << input << std::endl;
    } else if (type == 2) {
        std::cout << "[WARNING]: " << input << std::endl;
    } else if (type == 3) {
        std::cout << "[ERROR]: " << input << std::endl;
    }
}

void Log(std::string input) {
    std::cout << "[INFO]: " << input << std::endl;
}

void Log(std::string custom, std::string input) {
    std::cout << "[" << custom << "]: " << input << std::endl;
}


}



