#Assuming the x and y values in the boundary object represent centers of the boundaries
#Assuming the instance_id in the boundary object represent the class-number of the object annotatated

import json
import os

IMAGE_HEIGHT = 720 #looked at it from the internal_format.json file
IMAGE_WIDTH =  1280

#functions for normalizing the Height, Width , X and Y Cordinates of the boundary data
def normalize_H(y):
    return y / IMAGE_HEIGHT

def normalize_W(x):
    return x / IMAGE_WIDTH

#Function for extracting the boundaries and putting it into a folder in YOLO format
def extract_boundaries(data, output_folder):
    #opening a new folder for the output in yolo file format
    try:
        os.mkdir(output_folder)
    except:
        print('Folder already exists')
    
    for ann in data['annotations']:
        for frame in ann['frames']:
            #open the frame's file in the annotation foler
            try:
                file = open(f'./{output_folder}/{frame}.txt','a')
                boundary = ann['frames'][frame]['bounding_box']
                class_number = ann['frames'][frame]['instance_id']['value']
                file.write(f'{class_number} {normalize_H(boundary["x"])} {normalize_W(boundary["y"])} {normalize_H(boundary["h"])} {normalize_W(boundary["w"])}\n')
            except:
                print(f'Error opening file for frame {frame}')
            finally:
                file.close()


if __name__ == '__main__':
    #Open the file and load the json data into a variable
    k = open('./internal_format.json')
    data = json.load(k)
    k.close()
    extract_boundaries(data, 'annotations')
