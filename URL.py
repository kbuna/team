from flask import Flask, render_template, request, redirect, url_for
import json

import codecs  # 追加

app = Flask(__name__)



# JSONファイルのパス
json_file_path = 'urls.json'

def load_urls():
    try:
        with codecs.open(json_file_path, 'r', 'utf-8') as f:
            data = json.load(f)
            return data.get('assets', [])
    except FileNotFoundError:
        return []

def save_urls(urls):
    data = {'assets': urls}
    with open(json_file_path, 'w') as f:
        json.dump(data, f, indent=2)

@app.route('/')
def index():
    # JSONファイルからURLリストを取得
    url_list = load_urls()
    return render_template('index.html', url_list=url_list)

@app.route('/add_url', methods=['POST'])
def add_url():
    title = request.form.get('name')
    url = request.form.get('url')
    
    # JSONファイルから既存のURLリストを取得
    url_list = load_urls()
    
    # 新しいURLを追加
    url_list.append({"name": title, "url": url})
    
    # URLリストを保存
    save_urls(url_list)
    
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)