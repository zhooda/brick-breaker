//
//  GameClass.hpp
//  brick-break
//
//  Created by Zeeshan Hooda on 2/18/20.
//  Copyright © 2020 Deceptive Labs. All rights reserved.
//

#pragma once

#include <stdio.h>
#include <vector>
#include "SpriteClasses.hpp"

namespace z {

class Game {

public:
    sf::RenderWindow screen;
    bool running;
    std::vector<z::Sprite> allSprites;
    std::vector<z::Brick> bricks;
    z::Player player;
    z::Ball ball;
    bool gameActive;
    Game();
    void newGame();
    void loop();
    void update();
    void events();
    void draw();
    bool getRunning();
    void setRunning();
    
};

}
