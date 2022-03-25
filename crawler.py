import requests
import json
from bs4 import BeautifulSoup

#paginas alvo

urls = ["https://www.vultr.com/pricing/#optimized-cloud-compute",
            "https://www.digitalocean.com/pricing"
            ]

for i in urls:

    response = requests.get(i)
    soup = BeautifulSoup(response.text, 'html.parser')
    print(response)
    print(soup.prettify())
