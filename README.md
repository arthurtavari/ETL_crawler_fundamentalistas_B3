![img](https://raw.githubusercontent.com/arthurtavari/portfolio_data_science/master/img/layout.jpg)
# Projeto:

## Coletando dados de empresas listadas na B3
O objetivo deste projeto é extrair indicadores fundamentalistas de todas as empresas listadas na bolsa de valores (B3). <br>
Utilizei o site [fundamentus](https://www.fundamentus.com.br/) como base para extração dos dados. 

### Dicionário das tabelas:  
Criei um script ([web_crawler_fundamentals.py](https://github.com/arthurtavari/ETL_crawler_dados_b3/blob/main/web_crawler_fundamentals.py)) que faz todo o processo de raspagem das informações relevantes do site e também todas as transformações e carregamento em um arquivo parquet. 

**O script é separado em 4 etapas:** <br>
1. Coleta todas as empresas listadas na B3;   <br> 
2. Através do nome do Papel é criada uma estrutura de repetição onde é extraído os dados individuais; <br>
3. Utilizando as variáveis das duas "raspagens" é criado uma base de dados em parquet; <br>
4. Os dados são replicados e disponibilizados em nuvem através de um bucket S3 na AWS.   