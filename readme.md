# Function
1. get images from url list you give
2. detect faces on each pictures
3. download images of each detected face to your working directory

# Info
this module is using cs2 to detect faces.

# How To Use
1. download the module [face_image_downloader].
2. create instance with the arguments blow.
  first arg: array of file paths or array of urls
  second arg(optional): base name of the image files that will be created
  third arg(optional): folder name the created images will be stored
3. execute either of the 2 methods
  "analyze" method for array of path
  "download" for array of urls
