# Combat Arena 3D Shooter

A lightweight 3D shooter built with Python and OpenGL (GLUT), featuring real-time enemy spawning, projectile combat, dual camera perspectives, and an optional auto-fire challenge mode.

## Overview

Combat Arena drops the player into a tiled arena where enemies continuously approach from all directions. Your objective is simple: survive, aim efficiently, and maximize score while avoiding excessive missed shots.

## Key Features

- 3D arena rendered with OpenGL primitives
- Animated enemy behavior with scaling effect
- Projectile-based shooting system
- Two camera modes:
  - Third-person orbit camera
  - First-person style view
- HUD with real-time score, life, and miss counter
- Optional auto mode (cheat mode) for testing/demo
- Restart flow after game over

## Gameplay Rules

- You start with 5 life points.
- Each enemy hit grants +10 score.
- The game ends when either:
  - life reaches 0, or
  - missed shots reach 10.

## Controls

| Input              | Action                     |
| ------------------ | -------------------------- |
| `W`                | Move forward               |
| `S`                | Move backward              |
| `A`                | Rotate left                |
| `D`                | Rotate right               |
| Left Mouse Click   | Fire projectile            |
| Right Mouse Click  | Toggle camera mode         |
| Left / Right Arrow | Rotate third-person camera |
| Up / Down Arrow    | Zoom camera in / out       |
| `C`                | Toggle auto mode           |
| `R`                | Restart after game over    |

## Tech Stack

- Python 3
- OpenGL via `PyOpenGL`
- GLUT windowing/input

## Project Structure

- `21201789_Abdullah Al Adib_section18_Assignment3.py`: Main game loop, rendering, input, and game logic.
- `OpenGL/`: Local OpenGL package files included with the project.

## How To Run

From the project root:

```bash
python3 "21201789_Abdullah Al Adib_section18_Assignment3.py"
```

If your environment is missing OpenGL bindings, install:

```bash
pip install PyOpenGL PyOpenGL_accelerate
```

## Notes

- The game window launches as `1000x800`.
- Arena boundaries clamp player movement to keep gameplay inside the map.
- Enemy count is maintained continuously for persistent pressure.

## Author

Abdullah Al Adib
