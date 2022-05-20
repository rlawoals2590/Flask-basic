### Reference
[tistory_blog](https://smcjaemin0820.tistory.com/)

## Install Python

#### Download Python URL (www.python.org/downloads)
#### Downlaod Python on VSC
![images](https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2FbRnd8D%2FbtqHEFItlyR%2FAjw0xeaX7v6FMZPcQtQFDk%2Fimg.jpg)

## How to install Flask on VSC

#Install Flask using this command

First, Create a new terminal this key
'Ctrl + Shift + ` '
```
pip install flask
```

## If pip's version is low
```
pip install --upgrade pip
python -m pip install --upgrade pip
```
## Install other module
```
pip install module_name
```

### Run app.py
app.py's contents 
```
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_World():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```
#Run app.py using this command
```
python app.py
```


