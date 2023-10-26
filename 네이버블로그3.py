# 파이썬에서 openpyxl라이브러리를 사용해서 c:\work\result.xlsx파일로 결과를 저장하는 코드로 변경해줘

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

# Create a new Excel workbook and add a worksheet
workbook = Workbook()
worksheet = workbook.active

# Define the search keyword
search_keyword = "your_search_keyword"

# Iterate through pages 1 to 100
for page in range(1, 101):
    # Define the URL for the current page
    url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}&start={page}"

    # Send an HTTP GET request
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')

        # Extract the search results
        search_results = soup.find_all('li', class_='bx _svp_item')

        for result in search_results:
            # Extract blog name
            blog_name = result.find('a', class_='sub_txt')
            blog_name_text = blog_name.get_text() if blog_name else "N/A"

            # Extract blog address
            blog_address = result.find('a', class_='sub_txt').get('href') if blog_name else "N/A"

            # Extract post title
            post_title = result.find('a', class_='api_txt_lines')
            post_title_text = post_title.get_text() if post_title else "N/A"

            # Extract date
            date = result.find('span', class_='sub_time')
            date_text = date.get_text() if date else "N/A"

            # Write the extracted data to the Excel worksheet
            worksheet.append([f"Page {page}", blog_name_text, blog_address, post_title_text, date_text])

    else:
        print(f"Failed to retrieve page {page}.")

# Save the workbook to the specified file
workbook.save('c:/work/result.xlsx')
