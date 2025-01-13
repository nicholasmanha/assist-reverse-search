from file_reader.file_organizer import courseList
from articulation_downloader.grab_PDFs import grabPDFs

grabPDFs()
lis = courseList()
print(lis)
print(len(lis))