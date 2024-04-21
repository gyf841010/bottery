# Z LOTTERY

## Python Env Setup

* Run the following command to install the required python libraries - 

```python3.8
pip install -r requirements.txt
```

## 服务跑起来：
cp config.example.py config.py 
修改config.py的dir为实际本机save文件夹所在地址

cp static/js/lottery/config.js.example static/js/lottery/config.js
修改config.js为：
var get_url = 'http://bottery.silksci.com/calc/gen'

python sever.py -port=20005

访问url：127.0.0.1:20005