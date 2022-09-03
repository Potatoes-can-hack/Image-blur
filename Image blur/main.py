import cv2

def main():
    image = cv2.imread('image.jpg')
    blurredImage = cv2.GaussianBlur(image, (15, 15), 5)
    cv2.imwrite('Blurred-Image.jpg', blurredImage)

if __name__ == '__main__':
    main()