from ultralytics import YOLO
import cv2

model = YOLO("D:/data science/projects/my projects/Object Detection 101 Course/Yolo-Weight/yolov8l.pt")
results = model("D:/data science/projects/my projects/Object Detection 101 Course/Yolo with Images/Images/1.jpeg",show=True)
cv2.waitKey(0)
