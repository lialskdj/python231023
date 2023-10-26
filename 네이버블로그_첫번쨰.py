import requests
from bs4 import BeautifulSoup
import openpyxl

# Create a function to scrape data from a single page
def scrape_page(url, worksheet):
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the page with BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Find the elements containing the influencer search results
        search_results = soup.find_all('li', class_='bx')

        # Iterate through the search results and extract the desired information
        for result in search_results:
            influencer_name_element = result.find('a', class_='influe')
            if influencer_name_element:
                influencer_name = influencer_name_element.text
                influencer_url = influencer_name_element['href']
            else:
                influencer_name = "N/A"
                influencer_url = "N/A"

            influencer_info_element = result.find('p', class_='sub_info')
            influencer_info = influencer_info_element.text if influencer_info_element else "N/A"

            # Write the extracted information to the Excel file
            worksheet.append([influencer_name, influencer_url, influencer_info])

    else:
        print("Failed to retrieve the web page. Status code:", response.status_code)

# Create a new Excel workbook and worksheet
workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.append(["Influencer Name", "Influencer URL", "Influencer Info"])

# Loop through pages 1 to 100
for page in range(1, 101):
    page_url = f"https://search.naver.com/search.naver?where=influencer&sm=tab_jum&query=%EC%95%84%EC%9D%B4%ED%8F%B0&page={page}"
    print(f"Scraping page {page}...")
    scrape_page(page_url, worksheet)

# Save the workbook to a file
workbook.save("C:/work/influencer_results.xlsx")
