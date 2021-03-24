# coding=utf-8
# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import cv2


def print_hi():
    # Use a breakpoint in the code line below to debug your script.
    # print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.
    # img = cv2.imread('1.jpeg')
    # cv2.imshow('My Image', img)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # Load the cascade
    face_cascade = cv2.CascadeClassifier('./haarcascade/haarcascade_frontalface_default.xml')
    # Read the input image
    img = cv2.imread('demo-img/test.jpeg')
    # Convert into grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    # Display the output
    cv2.imshow('img', img)
    cv2.waitKey()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.tbrains.com/help/pycharm/
