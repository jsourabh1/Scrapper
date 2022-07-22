import requests
from bs4 import BeautifulSoup as beauty
import pandas as pd

#Requirements for this scrapper


# Getting the content div for particular for extractng the lastest jos
def get_content_div(page):

    #This is not the original urls of the site this is the api link for the pagenation you can find this link in the network tab inside the GET or POST request

    job_url = requests.get(
        "https://jobs.amd.com/go/Engineering/2566900/{}/?q=&sortColumn=referencedate&sortDirection=desc".format(page))
    page_content = job_url.text

    soup = beauty(page_content, "html.parser")

    # (tag_name,div name from which you have to extract the data)
    content_div = soup.find_all("tr", "data-row clickable")

    return content_div

#Getting the necessary content from the particular div


def get_content(content_div):

    global data

    for i in content_div:
        #You can modify the data according to you requirements

        # Getting the Title of the job
        job_title = i.find("a", "jobTitle-link").text
        # Getting the link of the job
        job_url = i.find("a", "jobTitle-link").get("href")
        # getting the location of the job
        job_location = i.find("span", "jobLocation").text

        job = {"title": job_title, "url": "https://jobs.amd.com/" +
               job_url, "location": job_location}  # Storing the data
        data.append(job)


data = []  # Stroing the final data in the form of json


#Running the loop for the pagenation

for k in range(0, 2, 25):

    content_div = get_content_div(k)  # Getting the particular content Div

    get_content(content_div)  # Getting the content from the div


df = pd.DataFrame(data)
df.to_csv("amd.csv")
print("yes")
