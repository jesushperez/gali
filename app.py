from flask import Flask, render_template, json
import config
import requests

app = Flask(__name__, static_folder="static")

@app.route('/')
def hello_world():
  #url = config.news_url + config.news_key
  #news = requests.get(url).json()

  with open('test.json', encoding='utf8') as f:
    data = json.load(f)
  articles = data['articles']

  return render_template('index.html', articles=articles)

if __name__ == '__main__':
  app.run(debug=True)