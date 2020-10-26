# IMPORTING LIBRARIES
from credentials.pw import aws_access_key_id, aws_secret_access_key, sheet_id
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import boto3
from datetime import datetime

s3 = boto3.client('s3', aws_access_key_id = aws_access_key_id, aws_secret_access_key = aws_secret_access_key)

date_info = datetime.now().strftime("%d/%m/%Y %H:%M")
print("STARTING PROCESS -", date_info)

# VARIABLE CONNECTION API GOOGLE
scope = ['https://spreadsheets.google.com/feeds']
credentials = ServiceAccountCredentials.from_json_keyfile_name('credentials/credentials.json', scope)
gc = gspread.authorize(credentials)
wks = gc.open_by_key(sheet_id)

# VARIABLE
worksheet = wks.get_worksheet(0)
name = worksheet.col_values(1)
ticker = worksheet.col_values(2)
quantity = worksheet.col_values(3)
investment = worksheet.col_values(4)
price_avg = worksheet.col_values(5)

# CREATING DATABASE
date_info = datetime.now().strftime("%d/%m/%Y %H:%M")
print("CREATING DATABASE -", date_info)
database_wallet = pd.DataFrame(list(zip(name,ticker,quantity,investment,price_avg)), columns=['name','ticker','quantity','investment','price_avg']).drop([0])
database_wallet.to_csv('database/wallet.csv', index=False)
s3.upload_file( 'database/wallet.csv', 'tavarilab-finance-project', 'datahub/row/wallet.csv')

date_info = datetime.now().strftime("%d/%m/%Y %H:%M")
print("PROCESS COMPLETED -", date_info) 