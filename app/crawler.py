from bs4 import BeautifulSoup
import sqlite3
import time
import requests

accords = {
    '芳香': 'aromatic',
    # '木質調': 'woody',
    # '花香調': 'floral',
    # '柑橘調': 'citrus',
    # '海洋調': 'aquatic',
    # '果香調': 'fruity',
    # '綠香調': 'green',
}
# requests = "SELECT name, brand, accord FROM perfume WHERE accord='木質調'";

conn = sqlite3.connect('perfume.db')
c = conn.cursor()
c.execute('''
CREATE TABLE IF NOT EXISTS perfume (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    brand TEXT,
    accord TEXT,
    popularity INTEGER,
    image_url TEXT,
    product_url TEXT
)
''')

headers = {
    "User-Agent": "Mozilla/5.0"
}

for zh_accord, en_accord in accords.items():
    url = f"https://www.fragrantica.com/groups/{en_accord}.html"
    resp = requests.get(url, headers=headers)
    print(resp.text)
    soup = BeautifulSoup(resp.text, 'html.parser')
    break 
    perfumes = soup.select('.popular-perfumes .card')[:15]
    for idx, card in enumerate(perfumes, 1):
        name = card.select_one('.card-title').get_text(strip=True)
        brand = card.select_one('.card-subtitle').get_text(strip=True)
        img = card.select_one('img')['src']
        link = "https://www.fragrantica.com" + card.select_one('a')['href']
        print(f"抓取 {zh_accord} {idx} {name} {brand} {img} {link}")
        c.execute('''
            INSERT INTO perfume (name, brand, accord, popularity, image_url, product_url)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, brand, zh_accord, idx, img, link))
    print(f"{zh_accord} 完成")
    time.sleep(2)  # 避免被封鎖

conn.commit()
conn.close()