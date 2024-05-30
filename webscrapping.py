from bs4 import BeautifulSoup
import requests

def scrape_matches(url):
    resp = requests.get(url)
    resp = resp.text
    soup = BeautifulSoup(resp, 'lxml')

    matches = soup.find_all('div', class_='accordion__pane')

    last_date = None
    scraped_data = []

    for match in matches:
        span_elements = match.find_all('span', {'class': 'text-xs flex'})
        current_date = None

        for span in span_elements:
            parent_div = span.find_parent('div')
            if parent_div:
                current_date = parent_div.get_text(strip=True)
                scraped_data.append(f"Fecha: {current_date}")

        if current_date is None and last_date:
            scraped_data.append(f"Fecha: {last_date}")
        elif current_date:
            last_date = current_date

        title = match.find('div', class_='w-full xl:leading-3 my-auto text-lg')
        if title:
            scraped_data.append(title.get_text().strip())

        scraped_data.append(match.find('span', class_='font-base text-right w-40 xl:text-md text-xs').get_text().strip())
        scraped_data.append(match.find('span', class_='text-center text-white xl:text-lg text-xs leading-3').get_text().strip())
        scraped_data.append(match.find('span', class_='font-base text-left w-40 xl:text-md text-xs').get_text().strip())
        scraped_data.append(f"Estadio: {match.find('span', class_='my-auto w-64 leading-3').get_text().strip()}")

        scraped_data.append("-" * 50)

    return scraped_data

urls = [
    'https://campeonatochileno.cl/programacion/1/segunda-la-liga-2d',
    'https://campeonatochileno.cl/programacion/2/segunda-la-liga-2d',
    'https://campeonatochileno.cl/programacion/3/segunda-la-liga-2d',
    'https://campeonatochileno.cl/programacion/4/segunda-la-liga-2d',
    'https://campeonatochileno.cl/programacion/5/segunda-la-liga-2d',
    'https://campeonatochileno.cl/programacion/6/segunda-la-liga-2d',
    'https://campeonatochileno.cl/programacion/7/segunda-la-liga-2d',
    'https://campeonatochileno.cl/programacion/8/segunda-la-liga-2d',
    'https://campeonatochileno.cl/programacion/9/segunda-la-liga-2d',
    'https://campeonatochileno.cl/programacion/10/segunda-la-liga-2d',
    'https://campeonatochileno.cl/programacion/11/segunda-la-liga-2d',
    'https://campeonatochileno.cl/programacion/12/segunda-la-liga-2d'
]

output_file = 'partidos_scrapeados.txt'

for url in urls:
    print(f"Scrapeando URL: {url}")
    data = scrape_matches(url)

    with open(output_file, 'a', encoding='utf-8') as file:
        for item in data:
            file.write(item + "\n")
        file.write("\n" + "=" * 50 + "\n\n")

print(f"Los datos scrapeados han sido guardados en el archivo: {output_file}")
