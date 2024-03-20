from yolov5 import detect

while True:
    ret, frame = cap.read()
    
    # Perform object detection on the frame
    # You need to replace 'detect' with the appropriate function from YOLOv5
    detections = detect(frame)
    
    # Process detections and draw bounding boxes on the frame
    
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break