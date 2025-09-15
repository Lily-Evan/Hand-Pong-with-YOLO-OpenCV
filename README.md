# 🏓 Hand Pong with YOLOv8 & OpenCV  

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)  
![YOLOv8](https://img.shields.io/badge/YOLOv8-Object%20Detection-green?logo=github)  
![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-red?logo=opencv)  

---

## 📖 Overview  
**Hand Pong** is an interactive computer vision game where you control a Pong paddle using **your hand** instead of a keyboard or mouse.  
With **YOLOv8** for object detection and **OpenCV** for video processing, your webcam tracks your hand in real time to move the paddle and keep the ball in play.  

---

## ✨ Features  
- 🎥 **Real-time hand tracking** with YOLOv8  
- 🕹️ **Classic Pong mechanics** (ball bouncing, scoring, game over)  
- 🤚 **Hand-controlled paddle** instead of keyboard input  
- 👥 **Expandable to multiplayer** with two paddles  
- 🔧 Easy to modify and extend  

---

## 🛠️ Requirements  

- Python **3.8+**  
- [Ultralytics YOLOv8](https://github.com/ultralytics/ultralytics)  
- OpenCV (`pip install opencv-python`)  
- A webcam  

Install dependencies:  
```bash
pip install ultralytics opencv-python
🚀 Getting Started

Clone this repository:

git clone https://github.com/your-username/hand-pong.git
cd hand-pong


Run the game:

python hand_pong.py


Move your hand in front of the webcam to control the paddle.

🎮 Gameplay

The ball bounces off the top and bottom walls.

Use your hand to move the paddle up and down.

If the ball touches the paddle → ✅ you score a point.

If you miss → ❌ Game Over.

<p align="center"> <img src="docs/demo.gif" alt="Hand Pong Demo" width="500"/> </p>
🔮 Roadmap

 Train YOLO on a hand detection dataset (instead of "person")

 Add 2-player mode (left & right paddles)

 Power-ups: speed boost, multiple balls, shrinking paddle

 Add sounds and scoreboards

 Package release via pip install hand-pong
