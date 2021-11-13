import cv2
import numpy as np
import time
import sys
from imutils import face_utils
from face_utilities import Face_utilities
from signal_processing import Signal_processing

if __name__ == "__main__":

    cam = cv2.VideoCapture(0)

    fu = Face_utilities()
    sp = Signal_processing()

    fps = 0   # real time capture
    video_fps = cam.get(cv2.CAP_PROP_FPS)

    while cam.isOpened():
        t0 = time.time()

        ret_read, img = cam.read()

        if img is None:
            print("End of video")
            cv2.destroyAllWindows()
            break

        img = cv2.flip(img, 1)  # flip image to mirror

        ret_fu = fu.no_age_gender_face_process(img, "68")

        # if ret_fu is None:
        #     cv2.putText(img, "No face detected")
        #     cv2.imshow("img", img)

        cv2.imshow('frame', img)
        key = cv2.waitKey(1)
        if key == 113:
            break   # q to quit

    cam.release()
    cv2.destroyAllWindows()



