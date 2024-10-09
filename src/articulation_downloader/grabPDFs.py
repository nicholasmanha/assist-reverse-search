import urllib, json

def grabPDFs():
    institutions_url = urllib.request.urlopen("https://assist.org/api/institutions")
    institutions = json.load(institutions_url)
    target_college = "University of California, Berkeley"
    major = "Computer Science, Lower Division B.A."
    id = None
    for entry in range(len(institutions)):
        curr_college = institutions[entry]['names'][0]['name']
        if curr_college == target_college:
            id = institutions[entry]['id']
            break