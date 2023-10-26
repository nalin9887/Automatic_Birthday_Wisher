
import pandas
from random import *
import smtplib
import datetime as dt
now=dt.datetime.now()
year=now.year
day=now.day
month=now.month
hour=now.hour
minute=now.minute
def sendmail(message,mail):
    mymail="nalindummy1@gmail.com"
    password="jcyrujpuarikiqoy"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=mymail,password=password)
        connection.sendmail(from_addr=mymail,to_addrs=mail,msg=f"Subject: Happy Birthdayy!!\n\n {message}")

data=pandas.read_csv("birthdays.csv")
for index, row in data.iterrows():
    col=data["name"][index]
    person_year=data[data.name==col].year
    person_month=data[data.name==col].month
    person_day=data[data.name==col].day
    person_email=data[data.name==col].email
    path=f"letter_templates/letter_{randint(1,3)}.txt"

    with open(path) as file:
         content=file.read()
         msg=content.replace("[NAME]",col)

    if person_year==year and person_day==day and person_month==month:
        sendmail(message=msg,mail=person_email)






