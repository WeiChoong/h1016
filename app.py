from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 模擬資料庫，用 list 存放文章
posts = [
    {"title": "我的第一篇文章", "author": "小明", "content": "這是第一篇文章的內容！"},
    {"title": "Flask 教學", "author": "管理員", "content": "今天我們來學 Flask 基礎。"}
]

@app.route('/')
def index():
    # 顯示所有文章
    return render_template('index.html', posts=posts)

@app.route('/new', methods=['GET', 'POST'])
def new_post():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        content = request.form['content']

        # 新增文章到列表
        posts.append({"title": title, "author": author, "content": content})
        return redirect(url_for('index'))

    return render_template('new_post.html')

if __name__ == '__main__':
    app.run(debug=True)
