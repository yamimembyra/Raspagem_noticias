#!/usr/bin/env python
# coding: utf-8

# In[28]:


import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

urls = ['https://noticias.iob.com.br',
        'https://www.jota.info/tributos-e-empresas/tributario',
        'https://economia.uol.com.br/guia-de-economia/',
        'https://www.legisweb.com.br/legislacao_ultimas/?data=6&abr=federal&acao=Filtrar#resultado']

for url in urls:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find_all('a')

    if 'iob' in url:
        containers = soup.find_all('h3')
        headlines = [container.find('a') for container in containers]
    elif 'jota' in url:
        containers = soup.find_all('h2')
        headlines = [container.find('a') for container in containers]
    elif 'uol' in url:
        containers = soup.find_all('div', class_='thumbnails-wrapper')
        headlines = [container.find('a') for container in containers]
    else:  # LegisWeb
        containers = soup.find_all('h4')
        headlines = [container.find('a') for container in containers]

    print(f'Headlines from {url}:')
    for headline in headlines:
        if headline is not None:
            print(headline.get_text().strip())
            link = headline.get('href')
            if link:
                print(urljoin(url, link))
            print('\n')  # Print a newline to separate headlines from different sites

    input("Pressione qualquer tecla para continuar...")


# In[ ]:





# In[ ]:




