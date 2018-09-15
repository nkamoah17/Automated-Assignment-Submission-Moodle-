import selenium
from selenium import webdriver
# time for pausing between navigation
import time
# Datetime for recording time of submission
import datetime
# os for file management
import os

def submit_assignment(file_tup):
    # Using Chrome to access web
    driver = webdriver.Chrome(r"C:\Users\Kenneth Amoah Nyame\Anaconda3\selenium\webdriver\chromedriver.exe")
    
    time.sleep(1)
    
    # Open the website
    driver.get('https://moodle.calvin.edu')

    # Password for Moodle
    with open(r'C:\Users\Kenneth Amoah Nyame\Desktop\pswd.txt') as f:
        pswd = f.read()
        
    # Locate id and password
    id_box = driver.find_element_by_name('username')
    pass_box = driver.find_element_by_name('password')

    # Send login information
    id_box.send_keys('ka32')
    pass_box.send_keys(pswd)

    # Click login
    login_button = driver.find_element_by_id("loginbtn")
    login_button.click()

    # Find and click on list of courses
    courses_button = driver.find_element_by_id('label_3_6')
    courses_button.click()

    # Wait for the page to load
    time.sleep(2)

    # Get the name of the folder
     folder = file_tup[0]

    # Class to select depends on folder
   if folder == 'HIST-151-BH':
        class_select = driver.find_element_by_link_text('Hist of the West & World')
   elif folder == 'PHYS-235-B':
        class_select = driver.find_element_by_link_text(
           'Intro Phys: Elect/Magnetism'
   elif folder == 'ENGR-209-B':
        class_select = driver.find_element_by_link_text(
            'Intro Laws of Conser & Thermo'
   elif folder == 'MATH-271-A':
        class_select = driver.find_element_by_link_text('Multivariable Calculus')
   elif folder == 'CS-104-C":
        class.select = driver.find_element_by_link_text('Applied Computing')

    # Click on the specific class
    class_select.click()

    assignment_button = driver.find_element_by_class_name('activityinstance')
    assignment_button.click()

    # Wait for the page to load
    time.sleep(2)
    open_link_button = driver.find_element_by_id('page-mod-url-view')
    open_link_button.click()

    # Send the name of the file to the button
    file_location = os.path.join(submission_dir, folder, file_name)
    choose_file.send_keys(file_location)

    submit_assignment = driver.find_element_by_id('submit_file_button')
    submit_assignment.click()
            
    # Wait for the page
    time.sleep(2)

    # Move the file to the submitted folder
   submitted_dir = (r'C:\Users\Kenneth Amoah Nyame\Desktop\Calvin College\Fall 2018')
   submitted_dir = os.path.join(submitted_dir, folder)
   submitted_file_name = 'Submitted ' + file_name

    submitted_file_location = os.path.join(submitted_dir, submitted_file_name)
     os.rename(file_location, submitted_file_location)

   print('{} Assignment for Class {} successfully submitted at {}.'.format(
       file_name, folder, datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))

    print('Submitted assignment available at {}.'.format(submitted_file_location))
    return
if __name__ == "__main__":

    # Build tuple of (folder, file) to turn in
    submission_dir =(r'C:\Users\Kenneth Amoah Nyame\Desktop\Calvin College\Fall 2018')
    dir_list = list(os.listdir(submission_dir))

    for directory in dir_list:
        file_list = list(os.listdir(os.path.join(submission_dir, directory)))
        if len(file_list) != 0:
            file_tup = (directory, file_list[0])

    if len(file_tup) == 0:
        print('No files to submit')

    else:
        print('Assignment "{}" for "{}" found.'.format(file_tup[1], file_tup[0]))
        input('Press enter to proceed: ')
        submit_assignment(file_tup)

      
