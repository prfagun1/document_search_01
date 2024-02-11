# Guia de Uso do da pesquisa de documentos da Azure com o AI Search

Este é um guia para utilizar o script de pesquisa de documentos da Azure com o AI Search.

## Descrição do Processo

O processo de pesquisa de documentos da Azure envolve as seguintes etapas:

1. **Preparação do Ambiente:**
   - O ambiente foi criado seguindo os passos do - [Tutorial de Integração com Serviço de Busca de IA da Azure](https://microsoftlearning.github.io/mslearn-ai-fundamentals/Instructions/Labs/11-ai-search.html) no Microsoft Learn.

2. **Configuração das Variáveis de Ambiente:**
   - Antes de executar o processo, você precisa configurar duas variáveis de ambiente:
     - `service_endpoint`: O URL da API da Azure.
     - `index_name`: O nome do indice criado.
     - `api_key`: Sua chave de API.


3. **Execução do Processo:**
   - Execute o script fornecido para realizar a pesquisa.

4. **Análise dos Resultados:**
   - Ao iniciar o script será solicitado o termo a ser pesquisado e ele retornará o resultado da pesquisa.

## Configuração das Variáveis de Ambiente

Para configurar as variáveis de ambiente no seu sistema:

### No Windows:

Abra o Prompt de Comando e execute os seguintes comandos, substituindo os dados pelas suas informações:

```cmd
set service_endpoint=sua_url_aqui
set index_name=seu_indice_aqui
set api_key=sua_chave_de_api_aqui
```

### No Linux:

Abra o terminal e execute os seguintes comandos, substituindo os dados pelas suas informações:
```
export service_endpoint=sua_url_aqui
export index_name=seu_indice_aqui
export api_key=sua_chave_de_api_aqui
```


