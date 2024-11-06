from os.path import isfile, join
import os
from pathlib import Path
import pymupdf

def courseList():
    ROOT_DIR = os.path.dirname(os.path.abspath("main.py"))
    output_path = os.path.join(ROOT_DIR, 'articulation_downloader', 'outputs')

    college_list = []
    # all files in directory
    files = [f for f in os.listdir(output_path) if isfile(join(output_path, f))]

    for file in files:
        col = isCourseArticulated(file)
        if col is not None:
            college_list.append(col)

    return college_list

def isCourseArticulated(file):
    ROOT_DIR = os.path.dirname(os.path.abspath("main.py"))
    output_path = os.path.join(ROOT_DIR, 'articulation_downloader', 'outputs')
    print(output_path)
    

    