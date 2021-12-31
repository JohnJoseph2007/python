import cv2

def thenameofthefunction():
  capture = cv2.VideoCapture(0)
  yourchoice = True
  while yourchoice:
    ret, frame = capture.read()
    cv2.imwrite("buddy.png", frame)
    yourchoice = False
  capture.release()
  cv2.destroyAllWindows() 

thenameofthefunction()