from bs4 import BeautifulSoup as beauty
import requests
import pandas as pd

# Getting the content div for particular for extractng the lastest jos


def get_page_divs(page):

    #This is not the original urls of the site this is the api link for the pagination you can find this link in the network tab inside the GET or POST request

    page_content = requests.get(
        "https://ola.skillate.com/jobs?page={}&pageSize=140&department=&location=&title=&sortBy=&orderBy=ASC".format(page)).text

    soup = beauty(page_content, "html.parser")

    # (tag_name,div name from which you have to extract the data)
    content_div_1 = soup.find_all("div", "css-7fgnh3")

    # (tag_name,div name from which you have to extract the data)
    content_div_2 = soup.find_all("div", "css-1thhzg5")

    content_div = content_div_1+content_div_2

    return content_div


def get_content(content_div):
    global data

    for i in content_div:
        job_title_ = i.find("div", "css-1rl4sp4")
        job_title = job_title_.find("span").text
        job_url = job_title_.find("a").get("href")
        job_category = i.find("div", "css-1hsb4dt").text
        job_location = i.find(
            "div", "css-1hsb4dt").find_next_sibling("div").text

        job = {"title": job_title, "url": "https://ola.skillate.com" +
               job_url, "category": job_category, "location": job_location}

        data.append(job)


data = []
i = 1

# Running this loop for the pageination
while True:
    content_div = get_page_divs(i)

    if not content_div:
        break
    get_content(content_div)
    i += 1

df = pd.DataFrame(data)
df.to_csv("Ola.csv")
print("Program Done")
