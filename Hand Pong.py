import cv2
import random
from ultralytics import YOLO

# Φορτώνουμε YOLO (για demo με COCO, αν έχεις hand dataset βάλε το εκεί)
model = YOLO("yolov8n.pt")

# Pong game settings
WIDTH, HEIGHT = 640, 480
paddle_height = 100
paddle_width = 15
ball_radius = 10

paddle_y = HEIGHT // 2
ball_x, ball_y = WIDTH // 2, HEIGHT // 2
ball_dx, ball_dy = 5, 5
score = 0

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv2.resize(frame, (WIDTH, HEIGHT))

    # YOLO ανίχνευση
    results = model(frame)
    for r in results[0].boxes:
        cls = int(r.cls[0])
        # Στο COCO δεν έχει χέρι, για demo χρησιμοποίησε "person" (class 0)
        if cls == 0:  
            x1, y1, x2, y2 = map(int, r.xyxy[0])
            cx = (x1 + x2) // 2
            cy = (y1 + y2) // 2
            paddle_y = cy  # Paddle ακολουθεί το χέρι

    # Σχεδίαση paddle
    cv2.rectangle(frame, (20, paddle_y - paddle_height//2),
                  (20 + paddle_width, paddle_y + paddle_height//2),
                  (0, 255, 0), -1)

    # Κίνηση μπάλας
    ball_x += ball_dx
    ball_y += ball_dy

    # Αναπήδηση πάνω-κάτω
    if ball_y - ball_radius <= 0 or ball_y + ball_radius >= HEIGHT:
        ball_dy *= -1

    # Αναπήδηση στο paddle
    if (20 < ball_x - ball_radius < 20 + paddle_width and
        paddle_y - paddle_height//2 < ball_y < paddle_y + paddle_height//2):
        ball_dx *= -1
        score += 1

    # Αν χάσουμε
    if ball_x - ball_radius <= 0:
        cv2.putText(frame, "GAME OVER", (200, HEIGHT//2), cv2.FONT_HERSHEY_SIMPLEX,
                    2, (0, 0, 255), 3)
        cv2.putText(frame, f"Score: {score}", (250, HEIGHT//2 + 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)
        cv2.imshow("Hand Pong", frame)
        cv2.waitKey(3000)
        break

    # Αν χτυπήσει δεξί τοίχο
    if ball_x + ball_radius >= WIDTH:
        ball_dx *= -1

    # Σχεδίαση μπάλας
    cv2.circle(frame, (ball_x, ball_y), ball_radius, (255, 0, 0), -1)

    # Σχεδίαση σκορ
    cv2.putText(frame, f"Score: {score}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    cv2.imshow("Hand Pong", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
