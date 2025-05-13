from mov.api.call import gen_url
import os

def test_gen_url():
    url = gen_url()
    key = os.getenv("MOVIE_API_KEY")
    print("MOVIE_API_KEY", key) #디버기용
    assert url == f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json?key={key}&targetDt=20120101"
