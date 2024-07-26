import requests

def req(dt="20120101"):
    base_url = "http://www.kobis.or.kr/kobisopenapi/webservice/rest/boxoffice/searchDailyBoxOfficeList.json"
    key = "82d0fee233046d8dce1be7c27453df1b"
    url = f"{base_url}?key={key}&targetDt={dt}"

    return req

#req()
#req("8" * 8)
#req(dt="ABCDE")

def req():
    print("req")
