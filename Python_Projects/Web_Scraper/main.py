import requests
from bs4 import BeautifulSoup

URL = "https://realpython.github.io/fake-jobs/"
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

result = soup.find(id="ResultsContainer")

# print(page.text)
# print(result.prettify())

def getJobAndCompany():
    job_elements = result.find_all("div", class_ = "card-content")

    for job_element in job_elements:

        # print(job_element, end="\n"*2)

        title_element = job_element.find("h2", class_="title")
        company_element = job_element.find("h3", class_="company")
        location_element = job_element.find("p", class_="location")

        print(title_element.text.strip())
        print(company_element.text.strip())
        print(location_element.text.strip())
        print()

def getJob():
    python_jobs = result.find_all(
        "h2", 
        string=lambda text: "python" in text.lower()
    )
    
    python_jobs_elements = [
        h2_element.parent.parent.parent for h2_element in python_jobs
    ]

    for job_element in python_jobs_elements:
        links = job_element.find_all("a")
        for link in links:
            link_url = link["href"]
            if(link.text.strip() == "Apply") :
                print(f"Apply here: {link_url}\n")

# getJobAndCompany()
getJob()