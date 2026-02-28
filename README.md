# Brick Breaker

A classic arcade-style Brick Breaker game built in Python using Pygame, featuring a power-up system, multi-ball mechanics, and physics-based ball movement built around clean object-oriented design.

---

## Overview

This project was developed to explore physics simulation, collision response, and object-oriented design in a real-time game context. Each game object — the paddle, ball, bricks, and power-ups — is encapsulated in its own class, responsible for its own state, movement, and rendering.

The objective was not only to build a playable game, but to design a system where each component is self-contained and new mechanics can be added without touching unrelated code.

---

## Key Features

- Ball physics with velocity, wall bouncing, and paddle collision response
- Power-up system with timed effects and automatic reversion
- Multi-ball support via power-up
- Grid-based brick layout with per-brick collision detection
- Paddle boundary clamping and speed controls

---

## Architecture Highlights

- Object-oriented design with distinct classes for the paddle, ball, bricks, and power-ups
- Each class handles its own movement, collision, and draw logic
- Game loop cleanly separated from entity logic
- Power-up state managed entirely within the Player and Powerup classes

---

## Technologies Used

- Python
- Pygame

---

## What I Learned

- Implementing physics simulation — velocity, bounce angles, and collision response
- Designing classes with well-defined responsibilities that do not bleed into each other
- Managing timed game state such as power-up activation and expiry
- Separating concerns so the ball, paddle, and bricks interact without tight coupling

---

## Controls

- A - Move paddle left
- D - Move paddle right

---

## How to Run

1. Install Python 3.11
2. Install Pygame:
```
pip install pygame
```
3. Run the game:
```
python BRICK BREAKER.py
```
