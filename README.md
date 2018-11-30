Object Extraction from Images using OpenCV Haar Cascades
===

> This is a demo of detecting and extracting (crop) objects in an image.

#### Setup:
1. Run `pip install -r requirements.txt`
2. Download an haar cascade (aka: https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalcatface.xml )
3. Place the haar cascade file in the same folder of the project.

#### Run:
```bash
python extract.py -i \<image input\> -o \<image output\> -c <haar cascade file>
```

### Usage: extract.py [OPTIONS]

Options:
  -i, --inputpath PATH    Path of input file or directory  [required]
  -o, --outputpath PATH   Path of output file or directory  [required]
  --verbose               Will print verbose messages.
  --grayscale             Save images as grayscale
  -w, --width INTEGER     Output image width size (in pixels)
  -h, --height INTEGER    Output image height size (in pixels)
  -c, --haarcascade PATH  Specify the haar-cascade file that will be used by
                          the object classifier  [required]



##### Dependencies:
- [opencv-python](http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_tutorials.html)
- [click](https://click.palletsprojects.com/en/7.x/)
