import time
from datetime import datetime as dt

host_path = "C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

website_list = input("Enter the website")
website_list = [""]

while True:
    if dt(dt.now().year,dt.now().month,dt.now().day,9)< dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18):

        with open(host_path,"r+") as file:
            content = file.read()
            for website in website_list:
                if website in content :
                    pass
                else:
                    file.write(redirect+ " "+website+"\n")

        print("Ta sites poy evales exoyn blockaristei !!!")
        break
    else:

         with open(host_path,"r+")as file:
             content = file.readline()
             file.seek(0)

             for line in content:

                if not any(website in line for website in website_list):
                    file.write(line)

             file.truncate()
         print("Ta Websites poy evales eginan unblock")
         break

