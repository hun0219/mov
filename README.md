# mov

### Install
```bash
# main
$ pip install git+https://github.com/hun0219/mov.git

# branch
$ pip install git+https://github.com/hun0219/mov.git@<branch_name>
```

### Start dev
```bash
$ git clone <URL>
$ cd <DIR>
$ source .venv/bin/activate
$ pdm install
$ pytest

# optin
$ pdm venv create
```
## setting env
```bash
cat ~/.zshrc | tail -n 3

# MY_ENV
export MOVIE_API_KEY="<KEY>"
```

## 트러블슈팅
{'faultInfo': {'message': '유효하지않은 키값입니다.', 'errorCode': '320010'}}
