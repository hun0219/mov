from mov.api.call import gen_url

def test_gen_url():
    url = gen_url()
    assert True
    assert "http" in url
    assert "kobis" in url
