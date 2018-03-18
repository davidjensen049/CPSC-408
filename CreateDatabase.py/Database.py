import random
import string
from datetime import datetime
#from faker import Faker # pip install Faker
#fake = Faker(('it_IT'))

# Opening files to write

people = open("people.sql" ,"w")
# ID    name    birthdate    deathdate

jobs = open("jobs.sql", "w")
# ID  position  priority  work_id  home_id  clockin_time  clockout_time  people_ID

personal = open("personal.sql", "w")
# ID    street_address  sallary sibilings   jobs_ID

title = open("title.sql", "w")
# SID   years_employed  commute_time    salary  person_ID

vehicle = open("vehicle.sql", "w")
# commute_time  vehicle_year    position_SID

# now we will generate raw data

list_of_titles = ['Computer Scientist', 'Project Director', 'President', 'CEO', 'Dean', 'Administrative Assistant', 'Branch Advisor', 'Software Engineer']
list_of_names = ['David', 'Bob', 'Joe', 'Kelly', 'Shane' , 'Mark' 'Shane', 'Kane', 'Nathan', 'Tyler', 'kyle']
list_of_jobs = ['Laborer','Car Salsman', 'Mechanic', 'Librarian', ' Gym Owner', 'Barista', 'Criminal']
list_of_months = ['November', 'December', 'January', 'February', 'March', 'April' , 'May', 'june', 'july', 'August', 'September', 'October']
list_of_vecihles = ['Nissan', 'toyota', 'Ford', 'Honda', 'Chevy', 'GMC', 'Audi', 'Lexus',]

#people_primary_key = str(random.randint(200,800)) +'-' + str(random.randint(1,2000))

#list_job_primary_key = str(random.randint(1,200)) + '-' + str(random.randint(200, 1000))
#job_foreign_key =
#personal_primary_key = str(random.randint(200,1000)) + '-' + str(random.randint(200,600))
#personal_foreign_key =
#list_title_primary_key = str(random.randint(300,900)) + '-' + str(random.randint(200,3000))
#title_foreign_key =
#vehicle_primary_key = str(random.randint(1,2000)) + '-' + str(random.randint(300,600))
#vehicle_fireign_key =
for i in range(1,100002):
    # people table raw data generation
    titles = random.choice(list_of_titles)
    key = random.randint(600,8000) + random.randint(2,10000)
    name = random.choice(list_of_names)
    month = random.choice(list_of_months)
    b_year = random.randint(1989, 2001)
    b_month = random.randint(1, 13)
    b_day = random.randint(1, 30)
    d_year = random.randint(1989, 2001)
    d_month = random.choice(list_of_months)
    d_day = random.randint(1, 30)
    people.write(str("Primary Key:" + str(key)) + str(i) + ',' + "Name: " + name + '-' + "Year Born: " + str(b_year) + '-' + "Month Born: " + str(month) + '-' + "Day Born :" + str(b_day) + ',' + "Year Death: " + str(b_year) + '-' + "Month of Death :" + str(month) + '-' +"Day of Death: " + str(b_day) + '\n')

    # jobs table raw data generation
    time1 = str(random.randint(1,59))
    time2 = str(random.randint(1,59))

    jobs.write(str("Primary Key: "+ str(key)) + ',' + "Job Title: " + random.choice(list_of_titles) + '-' + "Priority number:"  + str(random.randint(1000,9999)) + ',' +" Work Extension: " + str(random.randint(1000,9999)) + ',' + "Home Extension: " + str(random.randint(1000,9999)) + ',' +"Clock in: "  + time1 + ',' + "Clock Out:"  + time2 + ',' + " Foreign Key: " + str(key) + "Referenced From People_ID" +'\n')
    
    # personal table raw data generation
    personal.write(str("Primary Key:" + str(key)) + ',' + "Street Name : " + random.choice(list_of_names) + ',' + " Sallary:"  + str(random.randint(1000, 20000)) + ',' + "Street Number " + str(random.randint(1, 10)) + ',' + str(i) + " Foreign Key: " + str(key) + " Referenced From Jobs_ID " + '\n')

    # position table raw data generation
    title.write(str("Primary Key:" + str(key)) + ',' + "Years Employed: " + str(random.randint(1,30)) + ',' + "Years Employed: " + str(random.randint(1,5)) + ',' +  " Commute Time: " + str(random.randint(1000,20000)) + ',' + str(i) + " Foreign Key: " + str(key) + " Referenced From Personal_ID " + '\n')

    # vehicle table raw data generation
    vehicle.write(str("Primary Key:" + str(key)) + ',' + str(i) + "Vehicle MPG: " + str(random.randint(1, 45)) + ',' "Vehicle Make: " + str(random.choice(list_of_vecihles)) +',' + " Vehicle Year: " + str(random.randint(1980, 2018)) + ',' + str(i) +  " Foreign Key: " + str(key) + " Referenced From Title_ID " +'\n')

people.close()
jobs.close()
personal.close()
title.close()
vehicle.close()
