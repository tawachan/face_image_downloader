import cv2
import numpy as np

cascade_path = "./haarcascade_frontalface_alt.xml"
origin_image_path = "./cropped/"
dir_path = "./rotated/"

i = 0

for angle in [10, 20, 30, 40, 50, 60, 70, 80, 90]:
  for line in open('./cropped/index.txt','r'):
      line = line.rstrip()
      print(line)
      image = cv2.imread(origin_image_path+line, cv2.IMREAD_COLOR)
      if image is None:
          print('Not open : ',line)
          continue

      h, w = image.shape[:2]
      size = (w, h)

      angle_rad = angle/180.0*np.pi

      w_rot = int(np.round(h*np.absolute(np.sin(angle_rad))+w*np.absolute(np.cos(angle_rad))))
      h_rot = int(np.round(h*np.absolute(np.cos(angle_rad))+w*np.absolute(np.sin(angle_rad))))
      size_rot = (w_rot, h_rot)

      center = (w/2, h/2)
      scale = 1.0
      rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

      affine_matrix = rotation_matrix.copy()
      affine_matrix[0][2] = affine_matrix[0][2] -w/2 + w_rot/2
      affine_matrix[1][2] = affine_matrix[1][2] -h/2 + h_rot/2

      img_rot = cv2.warpAffine(image, affine_matrix, size_rot, flags=cv2.INTER_CUBIC)

      save_path = dir_path + '/' + 'image(' + str(i) + ')' + '.jpg'
      
      cv2.imwrite(save_path, img_rot)
      print("save!")
      i += 1
print("Finish")