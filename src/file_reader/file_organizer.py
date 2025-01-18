from os.path import isfile, join
import os
from pathlib import Path
import pymupdf


def courseList(course):
    ROOT_DIR = os.path.dirname(os.path.abspath("main.py"))
    output_path = os.path.join(ROOT_DIR, 'articulation_downloader', 'outputs')

    college_list = []
    # all files in directory
    files = [f for f in os.listdir(
        output_path) if isfile(join(output_path, f))]

    for file in files:
        col = isCourseArticulated(file, course)
        if col is not None:
            college_list.append(col)

    return college_list


def isCourseArticulated(file, course):
    course = course.replace("​", "") # remove unrendered character
    doc = pymupdf.open("articulation_downloader/outputs/" + file)  # open the agreement
    college = ""
    for page in doc:  # iterate through the document pages
        text = page.get_text().replace("​", "") # remove unrendered character
        if text.find('From:') != -1: # if the page doesn't have "From:", then the college title isn't on that page
            college = text[text.find('From:') + 6:text.find('2', text.find('From:')) - 1] # format: "From: [college] 2021-2022"
        search_position = text.find(course)
        if search_position != -1: 
            arrow_index = text.find("←", search_position + len(course)) # look after first arrow after the course
            articulated_course = text[arrow_index:arrow_index + 30]
            # if the course is articulated
            if "No Course Articulated" not in articulated_course and \
                "No Comparable Course" not in articulated_course and \
                    "Course(s) Denied" not in articulated_course:
                doc.close()
                return college
            else:
                doc.close()
                os.remove("articulation_downloader/outputs/" + file)
                return
            
    
