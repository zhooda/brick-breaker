//
//  GameClass.cpp
//  brick-break
//
//  Created by Zeeshan Hooda on 2/18/20.
//  Copyright © 2020 Deceptive Labs. All rights reserved.
//

#include <SFML/Graphics.hpp>
#include <vector>
#include "GameClass.hpp"

namespace z {

Game::Game() {
    sf::RenderWindow screen(sf::VideoMode(800, 600), "breakout");
    running = true;
}

void Game::newGame() {
    sf::Color RED(198, 73, 75);
    sf::Color ORANGE(196, 108, 64);
    sf::Color AMBER(179, 121, 56);
    sf::Color YELLOW(162, 161, 54);
    sf::Color GREEN(75, 159, 76);
    sf::Color BLUE(67, 77, 197);
    sf::Color GREY(142, 142, 142);
    sf::Color BLACK(0, 0, 0);
    z::Player player;
    allSprites.push_back(player);
    std::vector<z::Brick> bricks;
    
    for (float i = 0.0f; i < 8; i += 1.0f) {
        bricks.push_back(z::Brick(RED, i*100.0f + 50, 100-15));
        bricks.push_back(z::Brick(ORANGE, i*100.0f + 50, 130-15));
        bricks.push_back(z::Brick(AMBER, i*100.0f + 50, 160-16));
        bricks.push_back(z::Brick(YELLOW, i*100.0f + 50, 190-16));
        bricks.push_back(z::Brick(GREEN, i*100.0f + 50, 220-16));
        bricks.push_back(z::Brick(BLUE, i*100.0f + 50, 250-16));
        
    }
    for (int i = 0; i < bricks.size(); i++) {
        allSprites.push_back(bricks[i]);
    }
    
    z::Ball ball;
    allSprites.push_back(ball);
    
    loop();

}

void Game::loop() {
    while (screen.isOpen()) {
        
        sf::Event event;
        
        switch (event.type) {
            case sf::Event::Closed:
                screen.close();
                break;
                
            default:
                break;
        }
        
        if (event.type == sf::Event::Closed) {
            screen.close();
        }
        
    }
    
//    update();
//    draw();
}

void Game::update() {
    for (int i = 0; i < allSprites.size(); i++) {
        allSprites[i].update();
    }
}

}
