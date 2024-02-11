from azure.core.credentials import AzureKeyCredential
from azure.search.documents import SearchClient
import json
import os

# Substitua as informações abaixo com suas credenciais e detalhes do serviço de "AI Search"
service_endpoint = os.environ.get('service_endpoint')
index_name = os.environ.get('index_name')
api_key = os.environ.get('api_key')

# Crie um cliente para o serviço de "AI Search"
credential = AzureKeyCredential(api_key)

client = SearchClient(service_endpoint, index_name, credential)

# Defina suas palavras-chave de pesquisa
palavras_chave = input("Digite as palavras-chave para a pesquisa: ")

# Faça a consulta ao índice
resultado = client.search(search_text=palavras_chave)

# Converta os resultados para JSON formatado e imprima
resultados_formatados = [json.dumps(x, indent=4) for x in resultado]
print("\n".join(resultados_formatados))