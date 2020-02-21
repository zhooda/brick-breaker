//
//  SpriteClasses.hpp
//  brick-break
//
//  Created by Zeeshan Hooda on 2/18/20.
//  Copyright © 2020 Deceptive Labs. All rights reserved.
//

#pragma once

#include <stdio.h>
#include <SFML/Graphics.hpp>

namespace z {

class Sprite : public sf::RectangleShape {
public:
    Sprite(sf::Vector2f rectSize, sf::Color col, float xpos, float ypos);
    void update();
};

class Player : public Sprite {
public:
    sf::Vector2f vel;
    sf::Vector2f acc;
    Player();
    void update();
};

class Ball : public Sprite {
public:
    sf::Vector2f vel;
    Ball();
    void update();
};

class Brick : public Sprite {
public:
    int id;
    Brick(sf::Color col, float xpos, float ypos);
    void update();
};

}
