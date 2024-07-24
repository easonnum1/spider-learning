import requests
from bs4 import BeautifulSoup

def baidu_search(query):
    url = f"https://www.baidu.com/s?wd={query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"}
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        results = []
        
        for item in soup.find_all('div', class_='result c-container'):
            title = item.find('h3').text
            link = item.find('a')['href']
            results.append({'title': title, 'link': link})
        
        return results
    else:
        print("Failed to retrieve the web page. Status code:", response.status_code)
        return None

if __name__ == "__main__":
    query = "Python 爬虫"
    results = baidu_search(query)
    
    if results:
        for idx, result in enumerate(results):
            print(f"{idx + 1}. {result['title']}")
            print(f"   Link: {result['link']}")
