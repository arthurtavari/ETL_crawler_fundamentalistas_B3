![img](https://raw.githubusercontent.com/arthurtavari/portfolio_data_science/master/img/layout.jpg)
# Projeto:
## Coletando dados de empresas listadas na B3
O objetivo deste projeto é extrair indicadores fundamentalistas de todas as empresas listadas na bolsa de valores (B3).

Utilizei o site [fundamentus](https://www.fundamentus.com.br/) como base para extração dos dados e através dos scritps criados é feito a coleta e armazenamento dos dados em um *Bucket S3 na AWS*: 

O script [crawler_fundamentals.py](https://github.com/arthurtavari/ETL_crawler_fundamentalistas_B3/blob/main/crawler_fundamentals.py) é responsável por todo o processo de raspagem dos dados referente as empresas listadas na B3 e KPIs fundamentalistas. 

***Resumo do Script:***
1. Coleta todas as empresas listadas na B3; 
2. Através do nome do Papel é criada uma estrutura de repetição onde é extraído os dados individuais;
3. Utilizando as variáveis das duas "raspagens" é criado uma base de dados em CSV e salvo localmente;
4. Os dados são replicados e disponibilizados em nuvem através de um bucket S3 na AWS.   

Já o script [extraction_sheets_wallet.py](https://github.com/arthurtavari/ETL_crawler_fundamentalistas_B3/blob/main/extraction_sheets_wallet.py) é responsável por integrar com uma API do Google Sheets e coletar  dados (*fictícios*) sobre a minha carteira de investimento na B3. 

***Resumo do Script:***
1. Faz conexão com API do Google;
2. Coleta os dados da planilha; 
3. Utilizando os dados coletados é criado uma base de dados em CSV e salvo localmente;
4. Os dados são replicados e disponibilizados em nuvem através de um bucket S3 na AWS. 