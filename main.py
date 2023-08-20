import keyboard
import argparse
import time
import uuid
import cv2


def main(folder, continuous=False):
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()

        cv2.imshow("Window", frame)

        k = cv2.waitKey(1)

        if k & 0xFF == ord('s'):
            cv2.imwrite(f"{folder}/{uuid.uuid1()}.jpg", frame)
            if not continuous:
            	time.sleep(.5)

        if k & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='''
    Program to disable basic inputs to pc such as keyboard, mouse, webcam, and microphone
    ''')

    parser.add_argument("--folder", type=str,
                        help="the folder to save the pictures to")
    parser.add_argument("--continuous", type=bool,
			default=False, help="if false, add a half second delay after saving a picture")

    args = parser.parse_args()

    main(args.folder, args.continuous)
