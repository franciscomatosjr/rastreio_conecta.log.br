import requests
from bs4 import BeautifulSoup
import json

base_url = "https://conecta.log.br/view/jsRastreio.php"

codigo_rastreio = "AA0076893434343"

payload = {
    "origem": "form_rastreio_encomendas",
    "txtObjetos": codigo_rastreio,
    "txtR1RastreioEncomendas": "",
}

response = requests.post(base_url, payload)
json_response = response.json()
soup = BeautifulSoup(json_response.get('html'), 'html.parser')

if response.status_code == 200:
    print(response)
    retorno = response.json()

    # Extraindo as informações principais
    objeto = soup.find("div", class_="text-sm").get_text()
    codigo = soup.find("h3", class_="mb-2").get_text()
    fornecedor = soup.find("div", class_="col-5 col-sm-3 text-right").get_text(strip=True)
    destinatario = soup.find("p", class_="mb-0").find("strong").get_text()
    endereco = soup.find("p", class_="mb-0 text-muted").get_text()

    # Extraindo os eventos de rastreamento
    rastreio_items = soup.find_all("div", class_="d-flex align-items-center rastreio-item py-2")
    eventos = []
    for item in rastreio_items:
        status = item.find("span", class_="position-relative").get_text()
        location_tag = item.find("span", class_="text-sm")
        location = location_tag.get_text() if location_tag else ""
        timestamp = item.get_text().replace(status, "").strip()
        eventos.append({"status": status, "location": location, "timestamp": timestamp})

    # Montando o dicionário final
    resultado = {
        "objeto": objeto,
        "codigo": codigo,
        "fornecedor": fornecedor,
        "destinatario": destinatario,
        "endereco": endereco,
        "eventos": eventos
    }

    # Convertendo o dicionário para JSON para visualização
    print(json.dumps(resultado, indent=4, ensure_ascii=False))


else:
    print(response.status_code)
