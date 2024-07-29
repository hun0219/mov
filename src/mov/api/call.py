import pandas as pd
import requests
import json
import os

def list2df():
    l = req2df()
    df = pd.DataFrame(l)
    return df

def req2df() -> list:
    _, data = req()
    #data.get('').get('')
    l = data['boxOfficeResult']['dailyBoxOfficeList']
#    l = [
#            {'rnum': '1', 'rank': '1'},
#            {'rnum': '2', 'rank': '2'}
#        ]
#    df = pd.DataFrame(l)
    
    return l


def get_key():
    """영화진흥위원회 가입 및 API 키 생성 후 환경변수 선언 필요"""
    key = os.getenv('MOVIE_API_KEY')
    return key

def req(dt="20120101"):
    #url = gen_url('20240720')
    url = gen_url(dt)
    r = requests.get(url)
    code = r.status_code
    data = r.json()
    print(data)
    return code, data

def gen_url(dt="20120101"):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = get_key()
    url = f"{base_url}?key={key}&targetDt={dt}"

    return url

