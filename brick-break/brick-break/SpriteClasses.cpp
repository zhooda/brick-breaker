//
//  SpriteClasses.cpp
//  brick-break
//
//  Created by Zeeshan Hooda on 2/18/20.
//  Copyright © 2020 Deceptive Labs. All rights reserved.
//

#include <SFML/Graphics.hpp>
#include "SpriteClasses.hpp"

static sf::Color RED(198, 73, 75);
static sf::Color ORANGE(196, 108, 64);
static sf::Color AMBER(179, 121, 56);
static sf::Color YELLOW(162, 161, 54);
static sf::Color GREEN(75, 159, 76);
static sf::Color BLUE(67, 77, 197);
static sf::Color GREY(142, 142, 142);
static sf::Color BLACK(0, 0, 0);

namespace z {

//class MySprite : public sf::RectangleShape {
//public:
//    MySprite(sf::Vector2f rectSize, sf::Color col, float xpos, float ypos) {
//        setSize(rectSize);
//        setFillColor(col);
//        setPosition(xpos, ypos);
//    }
//
//};
Sprite::Sprite(sf::Vector2f rectSize, sf::Color col, float xpos, float ypos) {
    setSize(rectSize);
    setOrigin(rectSize.x/2, rectSize.y/2);
    setFillColor(col);
    setPosition(xpos, ypos);
}

void Sprite::update() {
    int pass = 1;
}
// PLAYER

Player::Player() : Sprite(sf::Vector2f(150.0f, 10.0f), RED, 400, 570){
    vel = sf::Vector2f(0.0f, 0.0f);
    acc = sf::Vector2f(0.0f, 0.0f);
}

void Player::update() {

    acc = sf::Vector2f(0.0f, 0.0f);
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Key::Left)) {
        move(-5.0f, 0.0f);
    }
    if (sf::Keyboard::isKeyPressed(sf::Keyboard::Key::Right)) {
        move(5.0f, 0.0f);
    }
    
    // Screen wrapping I think
    if (getPosition().x > 800 - getSize().x/2) {
        setPosition(800 - getSize().x/2, getPosition().y);
    }
    if (getPosition().x < getSize().x/2) {
        setPosition(getSize().x/2, getPosition().y);
    }
}

// BALL

Ball::Ball() : Sprite(sf::Vector2f(10.0f, 10.0f), RED, 400, 540) {
    vel = sf::Vector2f(3.0f, -3.0f);
}

void Ball::update() {
    if (getPosition().x > 795) {
        vel.x = -vel.x;
    } else if (getPosition().x < 5) {
        vel.x = -vel.x;
    }
    
    if (getPosition().y > 595) {
        vel.y = -vel.y;
    } else if (getPosition().y < 5) {
        vel.y = -vel.y;
    }
    
    setPosition(getPosition().x + vel.x, getPosition().y + vel.y);

}

// BRICK

Brick::Brick(sf::Color col, float xpos, float ypos) : Sprite(sf::Vector2f(100.0f, 30.0f), col, xpos, ypos) {
    id = 0;
}

void Brick::update() {
    setSize(getSize());
}

}
