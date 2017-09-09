import cv2
import os
import numpy as np
import urllib.request
from datetime import datetime as dt

class FaceImage:
  def __init__(self, image_urls, filename = dt.now().strftime('%Y%m%d'), foldername = "image"):
    self.urls = image_urls
    self.filename = filename
    self.count = 1
    self.folderpath = os.path.join(os.getcwd(), foldername)

  def __str__(self):
    return str(self.urls)

  def url_to_image(self, url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urllib.request.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    # return the image
    return image

  def image_file_name(self):
    number_padded = '{0:04d}'.format(self.count)
    return self.filename + number_padded + '.jpg'

  def count_up(self):
    self.count += 1

  def face_position(self, url):
    face_cascade_path = '/usr/local/opt/opencv/share/' \
                        'OpenCV/haarcascades/haarcascade_frontalface_default.xml'

    face_cascade = cv2.CascadeClassifier(face_cascade_path)

    img = self.url_to_image(url)
    faces = face_cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=1, minSize=(150, 150))

    for (x, y, w, h) in faces:
      x_expand = int(w * 0.1)
      y_expand = int(h * 0.1)
      x_start = int(x - x_expand / 2)
      y_start = int(y - y_expand / 2)

      face_image = img[y_start : y + h + y_expand, x_start : x + w + x_expand]

      if not os.path.exists(self.folderpath):
        os.mkdir(self.folderpath)
      cv2.imwrite(os.path.join(self.folderpath, self.image_file_name()), face_image)
      self.count_up()

  def download(self):
    for url in self.urls:
      self.face_position(url)

