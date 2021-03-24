import cv2


def test():
    # Use a breakpoint in the code line below to debug your script.
    img = cv2.imread('./demo-img/1.jpeg')

    b, g, r = cv2.split(img)
    bgr = cv2.merge([b, g, r])
    brg = cv2.merge([b, r, g])
    rgb = cv2.merge([r, g, b])
    rbg = cv2.merge([r, b, g])
    gbr = cv2.merge([g, b, r])
    grb = cv2.merge([g, r, b])

    cv2.imshow('My Image', img)
    cv2.imshow('bgr Image', bgr)
    cv2.imshow('rgb Image', rgb)
    cv2.imshow('brg Image', brg)
    cv2.imshow('rbg Image', rbg)
    cv2.imshow('gbr Image', gbr)
    cv2.imshow('grb Image', grb)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == '__main__':
    test()
