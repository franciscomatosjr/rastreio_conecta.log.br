# 📦 Rastreamento de Objetos com BeautifulSoup no site 'https://conecta.log.br'

Este projeto utiliza Python e BeautifulSoup para extrair informações de rastreamento de objetos a partir de um retorno HTML bruto. O objetivo é converter o conteúdo HTML em um dicionário estruturado para facilitar o processamento e visualização.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.x** - Linguagem de programação
- **BeautifulSoup** - Para parsing e extração de dados do HTML
- **JSON** - Para formatação e visualização estruturada dos dados

---

## 📥 Instalação

Certifique-se de ter o Python e o gerenciador de pacotes `pip` instalados no seu ambiente.

1. Clone o repositório:
   ```bash
   git clone https://github.com/rairojr/rastreamento-objetos.git
   cd rastreamento-objetos

2. Crie um ambiente virtual (opcional, mas recomendado):
   ```bash
    python3 -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows

4. Instale as dependências:
pip install beautifulsoup4

## 📝 Uso

1. Coloque o conteúdo HTML que deseja processar na variável html_content.

2. Execute o script:
   ```bash
   python rastreamento.py
   ```
  
3. O retorno será um dicionário em formato JSON com os dados estruturados.

💻 Exemplo de Código
```bash
    import requests
    from bs4 import BeautifulSoup
    import json
    
    base_url = "https://conecta.log.br/view/jsRastreio.php"
    
    codigo_rastreio = "AA0076890578"
    
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
```


📝 Exemplo de Saída
```bash
      
         {
           "objeto": "OBJETO R05134A00063137BR",
           "codigo": "AA0072345235334234",
           "fornecedor": "ECONOPACK",
           "destinatario": "FULANO DE TAL",
           "endereco": "RUA ESTRADA MUITO ENGRAÇA, NÃO TINHA TETO, NÃO TINHA NADA",
           "eventos": [
               {
                   "status": "OBJETO CRIADO",
                   "location": "",
                   "timestamp": "24/03/2025 14:05"
               },
               {
                   "status": "TRANSFERIDO PARA CENTRO DE DISTRIBUIÇÃO",
                   "location": "",
                   "timestamp": "24/03/2025 15:02"
               },
               {
                   "status": "ENTRADA NO CENTRO DE DISTRIBUIÇÃO",
                   "location": "",
                   "timestamp": "24/03/2025 16:52"
               },
               {
                   "status": "OBJETO POSTADO APÓS O HORÁRIO LIMITE DA UNIDADE",
                   "location": "",
                   "timestamp": "24/03/2025 20:40"
               },
               {
                   "status": "OBJETO EM TRANSFERÊNCIA",
                   "location": "CAJAMAR - SP",
                   "timestamp": "25/03/2025 09:08"
               },
               {
                   "status": "OBJETO EM TRANSFERÊNCIA",
                   "location": "BELO HORIZONTE - MG",
                   "timestamp": "25/03/2025 13:35"
               }
           ]
         }
```
🧪 Testes
Para testar o script, basta executar:
```bash
   python rastreamento.py
```
    
🚀 Funcionalidades
- Extrai informações principais como:
  - Código do objeto
  - Fornecedor
  - Destinatário
  - Endereço
  - Eventos de rastreamento
- Converte o HTML para um dicionário estruturado em JSON.

📝 Licença
Este projeto está licenciado sob a Licença MIT - consulte o arquivo LICENSE para obter mais detalhes.

📫 Contribuição
Contribuições são sempre bem-vindas! Siga os passos abaixo para contribuir:

1. Faça um fork do projeto.
2. Crie uma nova branch: git checkout -b minha-nova-funcionalidade.
3. Faça as alterações e commit: git commit -m "Adicionar nova funcionalidade".
4. Faça um push para a branch: git push origin minha-nova-funcionalidade.
5. Envie um Pull Request.

Feito com ❤️ por Francisco Matos - GitHub


