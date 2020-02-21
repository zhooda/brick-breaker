//
//  zlib.hpp
//  sfml tut
//
//  Created by Zeeshan Hooda on 2/17/20.
//  Copyright © 2020 Deceptive Labs. All rights reserved.
//

#pragma once

#include <stdio.h>
#include <string>

namespace zlib {
std::string input(std::string prompt);
void print(std::string input);
void print(std::string input, std::string end);
void Log(int type, std::string input);
void Log(int type, int input);
void Log(std::string input);
void Log(std::string custom, std::string input);
}
