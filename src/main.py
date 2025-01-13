from file_reader.file_organizer import courseList
from articulation_downloader.grab_PDFs import grabPDFs
import click

@click.command()
@click.option('--university', prompt='Univerity',
              help='The University you wish to attend.')
@click.option('--major', prompt='Major',
              help='The major you wish to look at.')
@click.option('--course', prompt='Course',
              help='The course you wish to take.')

def find_colleges(university, major, course):
  grabPDFs(university, major)
  lis = courseList(course)
  print(lis)
  print(len(lis))
        
if __name__ == '__main__':
    find_colleges()
