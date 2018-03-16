import cv2
import numpy as np
 

## Exercício 9 da APS4 de Robótica Computacional
## Por Gabriel Monteiro , Guilherme Leite , Hugo Carl e Rafael Vieira

## feito em quarteto pela mudanças de salas que ocorreram, como conversado com prof. Fábio Miranda


cap = cv2.VideoCapture(0)
 
while True:
    _, frame = cap.read()
 
    cv2.circle(frame, (180, 95), 5, (0, 0, 255), -1)
    cv2.circle(frame, (375, 175), 5, (0, 0, 255), -1)
    cv2.circle(frame, (94, 300), 5, (0, 0, 255), -1)
    cv2.circle(frame, (302, 375), 5, (0, 0, 255), -1)
 
    pts1 = np.float32([[180, 95], [375, 175], [94, 300], [302, 375]])
    pts2 = np.float32([[0, 0], [500, 0], [0, 600], [500, 600]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
 
    result = cv2.warpPerspective(frame, matrix, (500, 600))
 
 
    cv2.imshow("Frame", frame)
    cv2.imshow("Perspective transformation", result)
 
    key = cv2.waitKey(1)
    if key == 27:
        break
 
cap.release()
cv2.destroyAllWindows()

