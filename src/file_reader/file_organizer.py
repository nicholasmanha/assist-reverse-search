from os.path import isfile, join
import os
from pathlib import Path
import pymupdf


def courseList():
    ROOT_DIR = os.path.dirname(os.path.abspath("main.py"))
    output_path = os.path.join(ROOT_DIR, 'articulation_downloader', 'outputs')

    college_list = []
    # all files in directory
    files = [f for f in os.listdir(
        output_path) if isfile(join(output_path, f))]

    for file in files:
        col = isCourseArticulated(file)
        if col is not None:
            college_list.append(col)

    return college_list


def isCourseArticulated(file):
    ROOT_DIR = os.path.dirname(os.path.abspath("main.py"))
    doc = pymupdf.open("articulation_downloader/outputs/" + file)  # open a document
    search_term = "MATH​ 53"
    for page_number in range(len(doc)):  # iterate the document pages via page number
        page = doc.load_page(page_number)
        college = ""
        if page_number == 1: # get the name of the college via the first page
            college = text[text.find('From:') + 6:text.find('2', text.find('From:')) - 1] # format: "From: [college] 2021-2022"
        text = page.get_text()  
        search_position = text.find(search_term)
        if search_position != -1: 
            arrow_index = text.find("←", search_position + len(search_term))
            if "No Course Articulated" not in text[arrow_index:arrow_index + 30]:
                return college
    
