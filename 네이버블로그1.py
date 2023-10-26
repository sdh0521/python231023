import requests
from bs4 import BeautifulSoup

# Replace {search_keyword} with your actual search keyword
search_keyword = "맥북"

# Define the URL
url = f"https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}&start=1"

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

        # Print the extracted data
        print(f"Blog Name: {blog_name_text}")
        print(f"Blog Address: {blog_address}")
        print(f"Post Title: {post_title_text}")
        print(f"Date: {date_text}")
        print("\n")
else:
    print("Failed to retrieve the page.")

# https://search.naver.com/search.naver?where=view&sm=tab_jum&query={search_keyword}&start=%EB%A7%A5%EB%B6%81
# 파이썬으로 위의 주소에서 BeautifulSoup으로 크롤링하는 코드를 작성해줘. 블로그명, 블로그주소, 글의제목, 날짜를 가지고 오는 형태의 코드

# 네이버블로그를 검색할때 1페이지에서 100페이지까지 처리하는 코드로 변경해줘
