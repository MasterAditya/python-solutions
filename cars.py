import requests
from bs4 import BeautifulSoup

def scrape_olx_car_covers():
    url = "https://www.olx.in/items/q-car-cover"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Failed to fetch the page.")
        return

    soup = BeautifulSoup(response.content, "html.parser")

    results = []
    listings = soup.find_all("li", class_="css-19ucd76")

    for item in listings:
        link_tag = item.find("a", href=True)
        title_tag = item.find("h6")

        if link_tag and title_tag:
            title = title_tag.get_text(strip=True)
            link = "https://www.olx.in" + link_tag['href']
            results.append(f"{title}\n{link}\n")

    with open("olx_car_covers.txt", "w", encoding="utf-8") as file:
        file.writelines(results)

    print(f"✅ Saved {len(results)} listings to 'olx_car_covers.txt'.")

if __name__ == "__main__":
    scrape_olx_car_covers()
