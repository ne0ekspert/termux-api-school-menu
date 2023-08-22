#!/usr/bin/env python3
import requests
import datetime
import os, sys
import dotenv

dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

now = datetime.datetime.now()
formattedDate = now.strftime("%Y%m%d")

url = "https://open.neis.go.kr/hub/mealServiceDietInfo"
params = {
        'KEY': os.environ['API_KEY'],
        'Type': "json",
        'pIndex': 1,
        'pSize': 5,
        'ATPT_OFCDC_SC_CODE': os.environ['ATPT_OFCDC_SC_CODE'], # 시도교육청코드
        'SD_SCHUL_CODE': os.environ['SD_SCHUL_CODE'], # 표준학교코드
        'MLSV_YMD': formattedDate
}

res = requests.get(url, params=params)

print(formattedDate)

data: dict = res.json()['mealServiceDietInfo']
head: list = data[0]['head']
rows: list = data[1]['row']

print(rows)

for row in rows:
    if row['MMEAL_SC_NM'] == sys.argv[1]:
        data = row['DDISH_NM'].replace('<br/>', '\n')
        os.system(f'termux-notification -t 급식 -c "{data}" --icon restaurant')
        break
