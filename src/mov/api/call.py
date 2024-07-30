import pandas as pd
import requests
import json
import os


def echo(yaho):
    return yaho

def apply_type2df(load_dt="20120101", path="~/tmp/test_parquet"):
    df = pd.read_parquet(f'{path}/load_dt={load_dt}')
    #df['rnum'] = pd.to_numeric(df['rnum'])
    #df['rank'] = pd.to_numeric(df['rank'])

    num_cols=['rnum', 'rank', 'rankInten', 'salesAmt',
            'audiCnt', 'audiAcc', 'scrnCnt', 'showCnt',
            'salesShare', 'salesInten', 'salesChange',
            'audiInten', 'audiChange']

    #for col_name in num_cols:
    #    df[col_name] = pd.to_numeric(df[col_name])

    df[num_cols] = df[num_cols].apply(pd.to_numeric) # for문 대신 to_numeric 전부 돌림

    return df
#파이썬에 타입 찍어보는법
#import pandas ad pd
#df = pd.read_parquet(f'~/tmp/test_parquet/load_dt=20120101')
#df['rnum'] = pd.to_numeric(df['rnum']) rnum은 영화사이트에서 제공
#df.dtype

def save2df(load_dt='20120101'):
    df = list2df(load_dt)
    # df에 load_dt 컬럼 추가 (조회 일자 YYYYYMMDD 형식)
    # 아래 파일 저장시 load_dt 기본으로 파티셔닝
    df['load_dt']= load_dt
    print(df.head(5))
    df.to_parquet('~/tmp/test_parquet',partition_cols=['load_dt'])
    return df

def list2df(load_dt='20120101'):
    l = req2df(load_dt)
    df = pd.DataFrame(l)
    return df

def req2df(load_dt='20120101') -> list:
    _, data = req(load_dt)
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

def req(load_dt="20120101"):
    #url = gen_url('20240720')
    url = gen_url(load_dt)
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

