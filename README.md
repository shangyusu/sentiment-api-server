# Sentiment API server
A super simple Chinese text sentiment analysis server based on snownlp and Flask.

* Usage

```
$ pip install flask snownlp
$ python server.py

GET http://<your-server-path>/sentiment/<text-to-analysis>

ex: http://0.0.0.0:5000/sentiment/我好開心
// 0.8373312661534721
```
