import cv2
import numpy
import math

def line(path):
    img=cv2.imread(path)
    img2=img.copy()

    pt1=[]
    pt2=[]

    def mouse(event,x,y,flags,parameter):
        if event==cv2.EVENT_LBUTTONDOWN:
            print(f'({x},{y})')
            if pt1==[]:
                pt1.append(x)
                pt1.append(y)
                print(f'POINT-1: {pt1}')
            elif pt2==[]:
                pt2.append(x)
                pt2.append(y)
                print(f'POINT-2: {pt2}')

    def x_reference_line():
        cv2.line(img2,(pt1[0],pt1[1]),(img.shape[1],pt1[1]),(255,0,0),3)
        cv2.line(img2, (pt1[0], pt1[1]), (pt2[0], pt2[1]), (255, 0, 0), 3)

    def y_reference_line():
        cv2.line(img2, (pt1[0], pt1[1]), (pt1[0],0), (0,0,255), 3)
        cv2.line(img2, (pt1[0], pt1[1]), (pt2[0], pt2[1]), (0, 0,255), 3)

    def x_reference_gradient():
        gradient_x=(pt2[1]-pt1[1])/(pt2[0]-pt1[0])
        return gradient_x

    def y_reference_gradient():
        gradient_y=(pt2[1]-pt1[1])/(pt2[0]-pt1[0])
        return gradient_y

    def x_reference_angle():
        angle_radians_x=abs(math.atan(x_reference_gradient()))
        if pt2[1]<pt1[1] and pt2[0]<pt1[0]:
            angle_degree_x=str(180-((180/math.pi)*angle_radians_x))
        elif pt1[1]<pt2[1] and pt2[0]<pt1[0]:
            angle_degree_x = str(180-((180 / math.pi) * angle_radians_x))
        else:
            angle_degree_x=str((180/math.pi)*angle_radians_x)
        cv2.putText(img2,angle_degree_x,(400,400),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)

    def y_reference_angle():
        angle_radians_y=abs(math.atan(y_reference_gradient()))
        if pt2[1]<pt1[1] and pt1[0]<pt1[0]:
            angle_degree_y = str(90-((180 / math.pi) * angle_radians_y))
        elif pt1[1]<pt2[1] and pt1[0]<pt2[0]:
            angle_degree_y = str(90+((180 / math.pi) * angle_radians_y))
        elif pt1[1]<pt2[1] and pt2[0]<pt1[0]:
            angle_degree_y = str(90+((180 / math.pi) * angle_radians_y))
        else:
            angle_degree_y = str(90-((180 / math.pi) * angle_radians_y))
        cv2.putText(img2,angle_degree_y,(400,400),cv2.FONT_HERSHEY_PLAIN,2,(0,0,255),2)

    def reference_line():
        axis = input("Enter the coordinate axis (x/y): ")

        if axis == 'x' or axis == 'X':
            x_reference_line()
            x_reference_gradient()
            x_reference_angle()
        elif axis == 'y' or axis == 'Y':
            y_reference_line()
            y_reference_gradient()
            y_reference_angle()
        else:
            print('Invalid Reference Line')

        return axis

    while True:
        cv2.imshow("IMAGE", img)
        cv2.setMouseCallback("IMAGE", mouse)
        if pt1!=[] and pt2!=[]:
            reference_line()
            break
        cv2.waitKey(1)

    cv2.imshow("IMAGE2",img2)
    cv2.waitKey(0)

line(r'C:\Users\Suyash R\Documents\OpenCV\resources\sample9.jpg')