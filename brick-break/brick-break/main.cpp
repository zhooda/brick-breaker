//
//  main.cpp
//  brick-break
//
//  Created by Zeeshan Hooda on 2/18/20.
//  Copyright © 2020 Deceptive Labs. All rights reserved.
//

#include <iostream>
#include <SFML/Graphics.hpp>
#include <vector>
#include "SpriteClasses.hpp"
#include "zlib.hpp"
#include "InitTest.hpp"

static std::string WINDOW_TITLE = "New Window";

int WIDTH = 800;
int HEIGHT = 600;
int FPS = 60;

float PLAYER_ACC = 1.0f;
float PLAYER_FRICTION = -0.1f;

sf::Color RED(198, 73, 75);
sf::Color ORANGE(196, 108, 64);
sf::Color AMBER(179, 121, 56);
sf::Color YELLOW(162, 161, 54);
sf::Color GREEN(75, 159, 76);
sf::Color BLUE(67, 77, 197);
sf::Color GREY(142, 142, 142);
sf::Color BLACK(0, 0, 0);

bool checkBrickCollision(z::Ball ball, z::Brick brick) {
    if (ball.getGlobalBounds().intersects(brick.getGlobalBounds())) {
        return true;
    } else {
        return false;
    }
}

int game(sf::RenderWindow &window) {
    z::Player player;
        z::Ball ball;
        std::vector<z::Brick> bricks;
        
        for (float i = 0.0f; i < 8; i += 1.0f) {
            bricks.push_back(z::Brick(RED, i*100.0f + 50, 100-15));
            bricks.push_back(z::Brick(ORANGE, i*100.0f + 50, 130-15));
            bricks.push_back(z::Brick(AMBER, i*100.0f + 50, 160-16));
            bricks.push_back(z::Brick(YELLOW, i*100.0f + 50, 190-16));
            bricks.push_back(z::Brick(GREEN, i*100.0f + 50, 220-16));
            bricks.push_back(z::Brick(BLUE, i*100.0f + 50, 250-16));
            
        }
        
        zlib::Log("Openning window.");
        while (window.isOpen()) {
            
            sf::Event evnt;
            
            while (window.pollEvent(evnt)) {
                
                switch (evnt.type) {
                    case sf::Event::Closed:
                        window.close();
                        return 1;
                        break;
                    case sf::Event::Resized:
                        zlib::Log("New Window Size -> " + std::to_string(evnt.size.width) + "x" + std::to_string(evnt.size.height) + ".");
                        break;
    //                case sf::Event::TextEntered:
    //                    if (evnt.text.unicode < 128) {
    //                        printf("%c", evnt.text.unicode);
    //                    }
                        
                    default:
                        break;
                }
                
                if (evnt.type == sf::Event::Closed) {
                    zlib::Log("Window close requested, closing window...");
                    window.close();
                    return 1;
                }
                
            }

    //        if (sf::Keyboard::isKeyPressed(sf::Keyboard::Key::W)) {
    //            player.move(sf::Vector2f(0.0f, -1.0f));
    //        }
    ////
    //        test.setPosition((float)sf::Mouse::getPosition(window).x, test.getPosition().y);
            
            for (int i = 0; i < bricks.size(); i++) {
                if (checkBrickCollision(ball, bricks[i])) {
                    if (ball.vel.y <= 0) {
                        ball.vel.y = -ball.vel.y;
                    } else {
                        ball.vel.y = ball.vel.y;
                    }
                    bricks.erase(bricks.begin() + i);
                }
            }
            
            if (player.getGlobalBounds().intersects(ball.getGlobalBounds())) {
                ball.vel.y = -ball.vel.y;
            }
            
            if (ball.getPosition().y + ball.getSize().y/2 > 600 - 30) {
                return 0;
            }
            
            player.update();
            ball.update();
            if (ball.vel.y < 0) {
                ball.vel.y -= 0.0001f;
            } else if (ball.vel.y >= 0) {
                ball.vel.y += 0.0001f;
            }
            if (ball.vel.x < 0) {
                ball.vel.x -= 0.0001f;
            } else if (ball.vel.x >= 0) {
                ball.vel.x += 0.0001f;
            }
            for (int i = 0; i < bricks.size(); i++) {
                bricks[i].update();
            }
            
            window.clear();
            for (int i = 0; i < bricks.size(); i++) {
                window.draw(bricks[i]);
            }
            
            window.draw(ball);
            window.draw(player);
            
            window.display();
            
        }
    return 1;
}

int main(void) {
    
    
    TestLog();
    
    sf::RenderWindow window(sf::VideoMode(800, 600), WINDOW_TITLE, sf::Style::Close | sf::Style::Resize);
    window.setFramerateLimit(FPS);
    zlib::Log("Window Created.");
    
    int gamething = game(window);
    while (!gamething) {
        gamething = game(window);
    }
    
    return 0;
}
