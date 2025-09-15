🏓 Hand Pong with YOLO & OpenCV
📖 Description

Hand Pong is an interactive game where you use your hand instead of a keyboard or mouse!
With the help of YOLOv8 (object detection) and OpenCV, your webcam tracks the position of your hand and moves the paddle on the screen.
Your goal: Don’t let the ball escape!

✨ Features

Real-time hand detection using YOLO.

Paddle moves vertically based on your hand position.

Classic Pong gameplay with score and Game Over.

Extendable to 2-player mode (second paddle with another hand/player).

🛠️ Requirements

Python 3.8+

Ultralytics YOLOv8

OpenCV (pip install opencv-python)

A webcam

🚀 How to Run

Clone this repository or download the code.

Install the dependencies:

pip install ultralytics opencv-python


Run the game:

python hand_pong.py


Move your hand in front of the camera to control the paddle.

Play and see how high you can score!

🎯 Gameplay

The ball bounces off the top and bottom walls.

If it hits the paddle → +1 point.

If you miss the ball → Game Over.

🔮 Future Improvements

Use a specialized YOLO model for hand detection instead of "person".

2-player mode (left and right paddles).

Power-ups (e.g., speed boost, double ball).

Dual-hand control (left hand = paddle, right hand = special moves).

👩‍💻 Author

Built for fun with YOLO & OpenCV ✋✨
