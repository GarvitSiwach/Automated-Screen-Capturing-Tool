import pyautogui
import cv2
import numpy as np
from datetime import datetime

resolution = (1920,1080)

codec = cv2.VideoWriter_fourcc(*"XVID")

filename = "recording.avi"
fps = 20.0
out = cv2.VideoWriter(filename, codec, fps, resolution)
cv2.namedWindow("Live", cv2.WINDOW_NORMAL)q
cv2.resizeWindow("Live", 480, 270)

while True:
    img = pyautogui.screenshot(str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")) + ".png")
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    out.write(frame)

    if cv2.waitKey(1) == ord('q'):
        break
        
out.release()

cv2.ishow("Live", frame)
cv2.destroyAllWindows()       