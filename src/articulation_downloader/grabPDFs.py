import urllib, json
from urllib.error import HTTPError

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
    try:
        institution_agreements = urllib.request.urlopen("https://assist.org/api/institutions/"+ str(id) + "/agreements")
        agreement_data = json.load(institution_agreements)
        colleges = [] # list of all college id's that have an agreement with the target college
        for entry in range(len(agreement_data)):
            colleges.append(agreement_data[entry]['institutionParentId'])

    except HTTPError as e:
        content = e.read()
        print()