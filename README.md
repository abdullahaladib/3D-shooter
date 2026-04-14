# Combat Arena 3D Shooter 🎮🔥

> Fast-paced Python + OpenGL arena combat where survival, aim, and movement decide your score.

## 🚀 Why This Project Is Fun

Combat Arena drops you into a 3D tiled battlefield where enemies keep coming from every side.  
Your mission: **stay alive**, **land clean shots**, and **push your high score** before your misses catch up.

## ✨ Highlight Features

- 🧱 3D arena rendered with OpenGL primitives
- 👾 Enemies with animated scaling behavior
- 🔫 Projectile-based shooting system
- 🎥 Two camera experiences:
  - Third-person orbit camera
  - First-person style view
- 📊 Live HUD for score, life, and misses
- 🤖 Auto mode (`C`) for demo/testing fun
- 🔁 Quick restart flow after game over

## 🕹️ Gameplay Rules (Quick View)

- ❤️ You start with **5 life points**
- ✅ Every enemy hit gives **+10 score**
- ☠️ Game over when:
  - life reaches **0**, or
  - missed shots reach **10**

## 🎯 Controls

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

## 🧰 Tech Stack

- 🐍 Python 3
- 🖼️ OpenGL via `PyOpenGL`
- 🪟 GLUT for windowing + input

## 📁 Project Structure

- `3D_shooter.py` → Main game loop, rendering, input handling, and gameplay logic
- `OpenGL/` → Local OpenGL package files bundled with the project

## ▶️ Run The Game

From the project root:

```bash
python3 "3D_shooter.py"
```

If OpenGL bindings are missing:

```bash
pip install PyOpenGL PyOpenGL_accelerate
```

## 📌 Good To Know

- Window size starts at **1000x800**
- Player movement is clamped inside arena bounds
- Enemy pressure is continuous for arcade-style intensity

## 🙌 Author

**Abdullah Al Adib**
