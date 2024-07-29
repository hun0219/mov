from mov.api.call import gen_url, req, get_key, req2df, list2df, save2df
import pandas as pd


def test_save2df():
    df = save2df()
    assert isinstance(df, pd.DataFrame)
    assert 'load_dt' in df.columns


def test_list2df():
    df = list2df()
    #print(df)
    assert isinstance(df, pd.DataFrame)
    assert 'rnum' in df.columns
    assert 'openDt' in df.columns
    assert 'salesAmt' in df.columns
    assert 'scrnCnt' in df.columns

def test_req2df():
    l = req2df()
    #print(l) #리스트
    assert len(l) > 0
    v = l[0]
    assert 'rnum' in v.keys()
    assert v['rnum'] == '1'
    #l = type('boxOfficeResult')

def test_비밀키숨기기():
    key = get_key()
    assert key

def test_gen_url():
    url = gen_url()
    #assert True
    assert "http" in url
    assert "kobis" in url

#    ulr = gen_url('20241231')
#    assert '20241231' in url

def test_req():
    code, data = req()
    assert code == 200

    #assert req('20240710') == 200
    
    code, data = req('20230101')
    assert code == 200
