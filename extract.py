# Author: Jonathan da Silva Santos, 11/2018, silva.santos.jonathan@gmail.com
# This project is license with GPL 2.0


import cv2
import click
from os import path, listdir


def show(message, verbose):
    if verbose:
        click.echo(message)

def detect(img, grayscale, width, height, classifier):

    # Before try to detect objects, we need to convert the image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    regions = classifier.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=5);

    objects = []
    for region in regions:
        (x, y, w, h) = region
        if grayscale:
            object = gray[y:y+w, x:x+h]
        else:
            object = img[y:y+w, x:x+h]
        if (width != -1) and (height != -1):
            object = cv2.resize(object, (width,height), interpolation = cv2.INTER_CUBIC)
        objects.append(object)

    return objects


def process(inputpath, outputpath, grayscale, width, height, classifier):
    # Loads image
    img = cv2.imread(inputpath)

    if img is None: return

    # fetch the roi's
    objects = detect(img, grayscale, width, height, classifier)

    # Save the new image
    filename_index = 0
    for object in objects:
        write_to_path = ''
        if path.isfile(outputpath):
            write_to_path = outputpath
        else:
            path_parts = inputpath.split("/")
            generated_filename = path_parts[len(path_parts)-1]
            write_to_path = click.format_filename(outputpath) + generated_filename
            if len(objects) > 1:
                write_to_path = click.format_filename(outputpath) + str(filename_index) + generated_filename
                filename_index += 1
        cv2.imwrite(write_to_path, object)
            




@click.command()
@click.option('--inputpath', '-i', type=click.Path(exists=True), required=True, help='Path of input file or directory')
@click.option('--outputpath', '-o', type=click.Path(exists=False), required=True, help='Path of output file or directory')
@click.option('--verbose', is_flag=True, help="Will print verbose messages.")
@click.option('--grayscale', is_flag=True, help="Save images as grayscale")
@click.option('--width','-w',  default=-1, help='Output image width size (in pixels)')
@click.option('--height','-h',  default=-1, help='Output image height size (in pixels)')
@click.option('--haarcascade', '-c', type=click.Path(exists=True), required=True, help='Specify the haar-cascade file that will be used by the object classifier')

def extract(inputpath, outputpath, verbose, grayscale, width, height, haarcascade):
    
    classifier = cv2.CascadeClassifier(haarcascade)


    show("Object Extraction from Images v0.0.1", verbose)
    show("Author: Jonathan S. Santos - 11/2018 - silva.santos.jonathan@gmail.com", verbose)

    
    # Check if the input path is a file or a directory
    isfile = path.isfile(inputpath)

    if isfile:
        show("Processing: " + str(inputpath), verbose)
        process(inputpath, outputpath, grayscale, width, height, classifier)
        
    else:
        # Input is a directory, so we presume that there are multiple files to be proccessed.
        for content in listdir(inputpath):
            input_file_path = str(inputpath) + content
            show("Processing: " + str(input_file_path), verbose)
            process(input_file_path, outputpath, grayscale, width, height, classifier)


    



if __name__ == '__main__':
    extract()

