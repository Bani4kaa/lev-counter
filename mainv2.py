import cv2
import subprocess
import torch

def main():
    yolo_process = subprocess.Popen(["python", "detect.py", "--source", "0", "--weights", "best.pt"], stdout=subprocess.PIPE)

    while True:
        detection_output = yolo_process.stdout.readline().strip().decode()
        if detection_output:
            labels = parse_detection_output(detection_output)
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()

            # Run YOLOv5 inference on the frame
            results = model_inference(frame)

            # Filter detections based on confidence threshold
            confidence_threshold = 0.5
            filtered_detections = []
            for detection in results.pred:
                scores = detection[:, 4]  # Confidence scores are in the 5th column
                keep_indices = (scores >= confidence_threshold).nonzero().squeeze(1)
                if keep_indices.numel() > 0:
                    detection = detection[keep_indices]
                    filtered_detections.append(detection)

            # Display filtered detections on the frame
            for detection in filtered_detections:
                # Draw bounding box and label
                # Modify this part according to your specific display requirements
                pass

            cv2.imshow('frame', frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            cap.release()
            cv2.destroyAllWindows()

def parse_detection_output(output):
    labels = output.split(',')
    return labels

if __name__ == "__main__":
    main()