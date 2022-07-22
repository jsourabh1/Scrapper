
from bs4 import BeautifulSoup as beauty
import requests
import pandas as pd

header = {
    "x-csrf-token": "x",
}

url = requests.post(
    "https://www.uber.com/api/loadSearchJobsResults?localeCode=en", headers=header)


# content comes in the form of the Json so we don't make it's soup simple etracting the data/
page_content_ = url.content


data = []


# we are extracting  the team ,title and the location data from the json
def get_content(index):

    global data, page_content
    content = page_content["data"]["results"][index]

    #We are extracting the only the Engineering feild Jobs if you want another then you can look into the uber sites

    if content["department"] == "Engineering":
        job_title = content["title"]
        job_id = content["id"]
        job_url = "https://www.uber.com/global/en/careers/list/"+str(job_id)

#         generated url: https://www.uber.com/global/en/carrers/list/111709/
#         wanted url: https://www.uber.com/global/en/careers/list/111779/

        #Preparing the data of the location
        if len(content["allLocations"]) > 1:
            job_location = "Multiple Locations"

        else:
            job_location = content["location"]["city"] + \
                content["location"]["region"]+content["location"]["country"]

        job = {

            "title": job_title,
            "url": job_url,
            "location": job_location
        }

        data.append(job)


# Going through all pages of the site
for i in range(1000):

    get_content(i)

df = pd.DataFrame(data)
df.to_csv("uber.csv")
print("Program Done")
