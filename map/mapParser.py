from screen.elements import *
import csv


walls = []
sectors = []

def map_editor_parser (map_editor_output):
    first_wall = 0
    wall_count = 0
    for sector in map_editor_output:
        first_wall = wall_count
        if sector != 0:
            for wall in sector:
                x1 = wall[0]
                y1 = wall[1]
                x2 = wall[2]
                y2 = wall[3]
                color = color_to_rgb(wall[4])
                walls.append(Wall(x1,y1,x2,y2,color))
                wall_count += 1
            last_wall = wall_count
            sectors.append(Sector(first_wall,last_wall,0,40,[0, 160, 160],[160, 100, 0]))

def color_to_rgb(color_name):
    colors = {
        "black": [0, 0, 0],
        "red": [255, 0, 0],
        "green": [0, 255, 0],
        "blue": [0, 0, 255],
        "yellow": [255, 255, 0],
        "orange": [255, 165, 0],
        "purple": [128, 0, 128],
        "pink": [255, 192, 203],
        "cyan": [0, 255, 255],
        "magenta": [255, 0, 255]
    }
    return colors.get(color_name.lower(), [0, 0, 0])

def read_map(filename):
    data = []
    with open(filename, 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            data.append(row)
    cleaned_data_list = []
    for sublist_str in data[0]:
        sublist_cleaned_str = sublist_str.strip('"')
        sublist_cleaned_list = eval(sublist_cleaned_str)
        cleaned_data_list.append(sublist_cleaned_list)
    return cleaned_data_list
