from mov.api.call import gen_url, req, get_key, req2dataframe

def test_req2dataframe():
    l = req2dataframe()
    print(l) #리스트
    assert len(1) > 0
    v = l[0]
    assert 'rnum' in v.keys()
    assert v['rnum'] == '1'

def test_비밀키숨기기():
    key = get_key()
    assert key

def test_gen_url():
    url = gen_url()
    #assert True
    assert "http" in url
    assert "kobis" in url

def test_req():
    code, data = req()
    assert code == 200

    #assert req('20240710') == 200
    
    code, data = req('20230101')
    assert code == 200
