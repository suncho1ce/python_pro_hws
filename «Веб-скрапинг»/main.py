import bs4
import requests

HEADERS = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cache-Control': 'max-age=0',
    'Connection': 'keep-alive',
    'Sec-Fetch-Dest': 'document',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-Site': 'same-origin',
    'Sec-Fetch-User': '?1',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Not_A Brand";v="99", "Google Chrome";v="109", "Chromium";v="109"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

URL = "https://habr.com"

# определяем список ключевых слов
KEYWORDS = ['Машинное обучение *', 'DIY или Сделай сам', 'web', 'python', 'Блог компании VK']

def print_hi(name):
    response = requests.get(URL, headers=HEADERS)
    text = response.text

    soup = bs4.BeautifulSoup(text, features="html.parser")
    articles = soup.find_all("article")

    result = []

    for article in articles:
        # не нашёл на странице "post_preview"
        preview_data = article.find(class_="tm-article-snippet tm-article-snippet").text

        for i in KEYWORDS:
            if i in preview_data:
                date = article.find(["time"])["title"]
                title = article.find(["h2"]).text
                short_link = article.find(class_="tm-article-snippet__title-link")["href"]
                link = (URL+short_link)
                matched_element = f"{date} - {title} - {link}"
                # print(f"Найдена статья, совпадение по слову \"{i}\"\n{matched_element}")

                result.append(matched_element)
                break
    print(result)

if __name__ == '__main__':
    print_hi('PyCharm')