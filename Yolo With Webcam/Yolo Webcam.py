from ultralytics import YOLO
import cv2
import cvzone
import math

cap = cv2.VideoCapture(0) # For Webcam
#cap.set(3,1280) # High Resolution
#cap.set(4, 720)

cap.set(3,640) # Low Resolution
cap.set(4,480) 

model = YOLO("../Yolo-Weight/yolov8n.pt")

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]

while True:
    success, img = cap.read()
    results = model(img, stream=True)
    for r in results:
        boxes = r.boxes
        for box in boxes:

            # For Bounding Box
            #box.xy
            x1,y1,x2,y2 = box.xyxy[0]
            x1,y1,x2,y2 = int(x1),int(y1),int(x2),int(y2)
            #print(x1,y1,x2,y2)
            #cv2.rectangle(img,(x1,y1),(x2,y2),(255,255,0),3)
            #box.wxwh
            w,h = x2-x1,y2-y1
            cvzone.cornerRect(img,(x1,y1,w,h))
            
            # For Confidence
            conf = math.ceil((box.conf[0] * 100))/100
            #print(conf)
            #cvzone.putTextRect(img,f"{conf}", (max(0,x1),max(30,y1)))

            # For Class Name
            cls = int(box.cls[0])
            #print(cls)
            cvzone.putTextRect(img,f"{classNames[cls]} {conf}", (max(0,x1),max(30,y1)),scale=0.9,thickness=1)

    cv2.imshow("Image",img)
    cv2.waitKey(1)