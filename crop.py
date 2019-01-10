import cv2

cascade_path = "./haarcascade_frontalface_alt.xml"
origin_image_path = "./images/"
dir_path = "./cropped/"

i = 0

for line in open('./images/index.txt','r'):
    line = line.rstrip()
    print(line)
    image = cv2.imread(origin_image_path+line, cv2.IMREAD_COLOR)
    if image is None:
        print('Not open : ',line)
        continue

    cascade = cv2.CascadeClassifier(cascade_path)
    facerect = cascade.detectMultiScale(image, scaleFactor=1.5, minNeighbors=1, minSize=(200, 200))

    if len(facerect) > 0:
        for rect in facerect:
            
            x = rect[0] - 500
            y = rect[1] - 500
            width = rect[2] + 1000
            height = rect[3] + 1000
            dst = image[y:y + height, x:x + width]
            save_path = dir_path + '/' + 'image(' + str(i) + ')' + '.jpg'
            
            cv2.imwrite(save_path, dst)
            print("save!")
            i += 1
print("Finish")