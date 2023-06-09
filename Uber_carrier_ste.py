

from bs4 import BeautifulSoup as beauty
import requests
import pandas as pd
import json
from pymongo import MongoClient
from datetime import datetime

client =MongoClient("mongodb://Saaurabh:Saurabh@ac-lhssquu-shard-00-00.yh1d1ea.mongodb.net:27017,ac-lhssquu-shard-00-01.yh1d1ea.mongodb.net:27017,ac-lhssquu-shard-00-02.yh1d1ea.mongodb.net:27017/JobHunter?ssl=true&replicaSet=atlas-tr39w0-shard-0&authSource=admin&retryWrites=true&w=majority")



database = client["JobHunter"]

my_collection = database["jobs"]



header = {
    "x-csrf-token": "x",
}

url = requests.post(
    "https://www.uber.com/api/loadSearchJobsResults?localeCode=en", headers=header)


# content comes in the form of the Json so we don't make it's soup simple etracting the data/
page_content = url.content
my_json = page_content.decode('utf8')
print('- ' * 20)

# Load the JSON to a Python list & dump it back out as formatted JSON
page_content_ = json.loads(my_json)



data = []


# we are extracting  the team ,title and the location data from the json
def get_content(index):

    global data, page_content_
    content = page_content_["data"]["results"][index]

    #We are extracting the only the Engineering feild Jobs if you want another then you can look into the uber sites

    job_department = content["department"]
    job_title = content["title"]
    job_id = content["id"]
    job_url = "https://www.uber.com/global/en/careers/list/"+str(job_id)

#         generated url: https://www.uber.com/global/en/carrers/list/111709/
#         wanted url: https://www.uber.com/global/en/careers/list/111779/

    #Preparing the data of the location
    if len(content["allLocations"]) > 1:
        city=set()
        country=set()
        for i in content["allLocations"]:
          city.add(i["countryName"])
          country.add(i["city"])

        job_city = list(city)
        job_country = list(country)
          

    else:
        job_city = [content["location"]["city"]]
        job_country = [content["location"]["countryName"]]

    job = {

        "title": job_title,
        "url": job_url,
        "job_department":job_department,
        "company":"uber",
        "city":job_city,
        "country":job_country,
        "description": content["description"]
      
    }

    data.append(job)
    my_collection.insert_one(job)
    print(len(data))


# Going through all pages of the site
for i in range(1000):

    get_content(i)

df = pd.DataFrame(data)
df.to_csv("uber.csv")
print("Program Done")


