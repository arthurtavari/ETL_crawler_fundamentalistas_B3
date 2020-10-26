# IMPORTING LIBRARIES
from credentials.pw import aws_access_key_id, aws_secret_access_key, sheet_id
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import boto3

s3 = boto3.client('s3', aws_access_key_id = aws_access_key_id, aws_secret_access_key = aws_secret_access_key)

# VARIABLE
url = 'https://www.fundamentus.com.br/resultado.php'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}

# CONNECTION SUCCESS
try:
    # VARIABLE FOR CONNECTION
    req = Request(url, headers = headers)
    response = urlopen(req)
    html = response.read()
    html = html.decode('ISO-8859-1')
    def clear_dataset(input):
        return " ".join(input.split()).replace('> <', '><')
    html = clear_dataset(html)
    soup_crawler = BeautifulSoup(html, 'html.parser')
    table = soup_crawler.find(id= 'resultado').find('tbody')
    table_2 = table.findAll('tr')

    print('CONNECTION SUCCESSFUL')
    
    # VARIABLE LIST
    papel = []
    ultima_cotacao = []
    pl = []
    p_vp = []
    psr = []
    div_yeld = []
    p_ativo = []
    p_cap_giro = []
    p_ebit = []
    p_ativo_circ_liq = []
    ev_ebit = []
    ev_ebitda = []
    mrg_ebit = []
    mrg_liq = []
    liq_corr = []
    roic = []
    roe = []
    liq_2_meses = []
    patrim_liq = []
    div_brut_patrim = []
    cresc_rec_5a = []

    date_info = datetime.now().strftime("%d/%m/%Y %H:%M")
    print('STARTING PROCESS FUNDAMENTALS - ', date_info)

    # DATA EXTRACTION PROCESS: FUNDAMENTALS
    for i in table_2:
        ticker_name = 0 + len(papel)
        papel.append(table.findAll('tr')[ticker_name].td.getText())
        ultima_cotacao.append(table.findAll('tr')[ticker_name].td.next_sibling.getText())
        pl.append(table.findAll('tr')[ticker_name].td.next_sibling.next_sibling.getText())
        p_vp.append(table.findAll('tr')[ticker_name].td.next_sibling.next_sibling.next_sibling.getText())
        psr.append(table.findAll('tr')[ticker_name].td.next_sibling.next_sibling.next_sibling.next_sibling.getText())
        div_yeld.append(table.findAll('tr')[ticker_name].td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.getText())

        p_ativo.append(table.findAll('tr')[ticker_name].td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                       next_sibling.getText())

        p_cap_giro.append(table.findAll('tr')[ticker_name].td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                          next_sibling.next_sibling.getText())

        p_ebit.append(table.findAll('tr')[ticker_name].td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                      next_sibling.next_sibling.next_sibling.getText())

        p_ativo_circ_liq.append(table.findAll('tr')[ticker_name].td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                                next_sibling.next_sibling.next_sibling.next_sibling.getText())

        ev_ebit.append(table.findAll('tr')[ticker_name].td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                       next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.getText())

        ev_ebitda.append(table.findAll('tr')[ticker_name].td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                         next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                         next_sibling.getText())

        mrg_ebit.append(table.findAll('tr')[ticker_name].td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                        next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                        next_sibling.next_sibling.getText())

        mrg_liq.append(table.findAll('tr')[ticker_name].td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                       next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                       next_sibling.next_sibling.next_sibling.getText())

        liq_corr.append(table.findAll('tr')[ticker_name].td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                       next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                       next_sibling.next_sibling.next_sibling.next_sibling.getText())

        roic.append(table.findAll('tr')[ticker_name].td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                       next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                       next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.getText())

        roe.append(table.findAll('tr')[ticker_name].td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                   next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                   next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                   next_sibling.getText())

        liq_2_meses.append(table.findAll('tr')[ticker_name].td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                           next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                           next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                           next_sibling.next_sibling.getText())

        patrim_liq.append(table.findAll('tr')[ticker_name].td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                       next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                         next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                   next_sibling.next_sibling.next_sibling.getText())

        div_brut_patrim.append(table.findAll('tr')[ticker_name].td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                               next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                               next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                               next_sibling.next_sibling.next_sibling.next_sibling.getText())

        cresc_rec_5a.append(table.findAll('tr')[ticker_name].td.next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                            next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                            next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.
                            next_sibling.next_sibling.next_sibling.next_sibling.next_sibling.getText())

    date_info = datetime.now().strftime("%d/%m/%Y %H:%M")
    print('PROCESS EXTRACT FINALIZED - ', date_info)
    
    date_info = datetime.now().strftime("%d/%m/%Y %H:%M")
    print('STARTING PROCESS DETAILS - ', date_info)

    # VARIABLE LIST
    papel_crawler = []
    tipo = []
    empresa = []
    setor = []
    sub_setor = []
    valor_de_mercado = []
    valor_da_firma = []
    ultimo_balanco = []
    numero_de_acoes = []
    
    # DATA EXTRACTION PROCESS: DETAILS
    for i in papel:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'}
        url_fundamentals = 'https://www.fundamentus.com.br/detalhes.php?papel=' + i
        req = Request(url_fundamentals, headers = headers)
        response = urlopen(req)
        html = response.read()
        html = html.decode('ISO-8859-1')
        html = clear_dataset(html)
        soup = BeautifulSoup(html, 'html.parser')
        table_data = soup.find('table', class_="w728")

        if table_data != None: 
            papel_crawler.append(table_data.find('tr').find('td').next_sibling.getText())
            tipo.append(table_data.find('tr').next_sibling.find('td').next_sibling.getText())
            empresa.append(table_data.find('tr').next_sibling.next_sibling.find('td').next_sibling.getText())
            setor.append(table_data.find('tr').next_sibling.next_sibling.next_sibling.find('td').next_sibling.getText())
            sub_setor.append(table_data.find('tr').next_sibling.next_sibling.next_sibling.next_sibling.find('td').next_sibling.getText())
            valor_de_mercado.append(table_data.next_sibling.find('tr').find('td').next_sibling.getText())
            valor_da_firma.append(table_data.next_sibling.find('tr').next_sibling.find('td').next_sibling.getText())
            ultimo_balanco.append(table_data.next_sibling.find('tr').find('td').next_sibling.next_sibling.next_sibling.getText())
            numero_de_acoes.append(table_data.next_sibling.find('tr').next_sibling.find('td').next_sibling.next_sibling.next_sibling.getText())
            
    # CREATING DATABASE
    columns_scraping = ['papel','tipo','empresa','setor','sub_setor','valor_de_mercado','valor_da_firma','ultimo_balanco','numero_de_acoes',
                        'ultima_cotacao','pl','p_vp','psr','div_yeld','p_ativo','p_cap_giro','p_ebit','p_ativo_circ_liq',
                        'ev_ebit','ev_ebitda','mrg_ebit','mrg_liq','liq_corr','roic','roe','liq_2_meses','patrim_liq','div_brut_patrim','cresc_rec_5a']


    database_company = pd.DataFrame(list(zip(papel,tipo,empresa,setor,sub_setor,valor_de_mercado,valor_da_firma,ultimo_balanco,numero_de_acoes,
                                             ultima_cotacao,pl,p_vp,psr,div_yeld,p_ativo,p_cap_giro,p_ebit,p_ativo_circ_liq,
                                             ev_ebit,ev_ebitda,mrg_ebit,mrg_liq,liq_corr,roic,roe,liq_2_meses,patrim_liq,div_brut_patrim,cresc_rec_5a)), columns = columns_scraping)

    database_company.to_csv('database/company_detail.csv', index=False)
    s3.upload_file( 'database/company_detail.csv', 'tavarilab-finance-project', 'datahub/row/company_detail.csv')

    date_info = datetime.now().strftime("%d/%m/%Y %H:%M")
    print('PROCESS CONCLUDED - ', date_info)
    
# ERROR CONNECTION IN HTTP
except HTTPError as e:
    print('ERROR IN HTTML', 'STATUS: ', e.status, 'REASON: ', e.reason)
    
# ERROR CONNECTION IN URL
except URLError as e:
    print('ERROR IN URL', 'REASON: ', e.reason)
