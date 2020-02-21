//
//  InitTest.cpp
//  sfml tut
//
//  Created by Zeeshan Hooda on 2/17/20.
//  Copyright © 2020 Deceptive Labs. All rights reserved.
//

#include <iostream>
#include "zlib.hpp"
#include "InitTest.hpp"

void TestLog() {
    int INFO = 1;
    int WARN = 2;
    int ERR  = 3;
    
    zlib::Log(INFO, "Info Log Test    --- passed.");
    zlib::Log(WARN, "Warning Log Test --- passed.");
    zlib::Log(ERR,  "Error Log Test   --- passed.");
    std::cout << std::endl;
    zlib::Log("Empty Log Test   --- Passed.");
}
