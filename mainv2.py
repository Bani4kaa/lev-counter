import cv2
import subprocess

def main():
    yolo_process = subprocess.Popen(["python", "detect.py", "--source", "0", "--weights", "best.pt"], stdout=subprocess.PIPE)

    while True:
        detection_output = yolo_process.stdout.readline().strip().decode()
        if detection_output:
            labels = parse_detection_output(detection_output)
            cap = cv2.VideoCapture(0)
            ret, frame = cap.read()

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
