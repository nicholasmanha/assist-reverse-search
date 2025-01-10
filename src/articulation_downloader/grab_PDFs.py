import urllib, json
from urllib.error import HTTPError
import requests
import os

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
        
        for college_id in colleges:
            major_url = urllib.request.urlopen(
                "https://assist.org/api/agreements?receivingInstitutionId=" + str(id) + "&sendingInstitutionId=" + str(
                    college_id) + "&academicYearId=72&categoryCode=major"
            )
            major_data = json.load(major_url)

            key = None

            for major_entry in major_data['reports']:
                curr_major = major_entry['label']
                if curr_major == major:
                    key = major_entry['key']
                    download_url = 'https://assist.org/api/artifacts/' + str(key)
                    response = requests.get(download_url, allow_redirects=True)
                    if response.status_code == 200:
                        ROOT_DIR = os.path.dirname(os.path.abspath("main.py"))
                        output_path = os.path.join(ROOT_DIR, 'articulation_downloader', 'outputs')
                        pdf = open(output_path + "\pdf" + str(key) + ".pdf", 'wb')
                        pdf.write(response.content)
                        pdf.close()
                    break



    except HTTPError as e:
        content = e.read()
        print()