
import requests
headers = {
    'Content-Type': 'text/plain; charset=UTF-8',
    'Origin': 'https://maoyan.com',
    'Referer': 'https://maoyan.com/board/4',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'
}


def get_one_page(url, headers):
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestsException:
        return None
def main():
	 url = "https://maoyan.com/board/4"
	 html = get_one_page(url, headers)
	 print(html)

if __name__ == '__main__':
      main()

