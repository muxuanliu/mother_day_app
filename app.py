from flask import Flask, send_from_directory, abort,render_template
from datetime import datetime  # 导入datetime模块


app = Flask(__name__)

@app.route("/")
def text():
    return render_template('example.html')  # 假设你的 HTML 文件叫
def index():
    current_time = datetime.now()  # 获取当前时间
    image_dir = ''
    return current_time.strftime('%Y-%m-%d %H:%M:%S')  # 格式化时间并返回
# @app.route('/show-image/<path:filename>')
# def show_image(filename):
#     image_dir = 'D:\Desktop\备份'  # 替换为你的图片目录路径
#     if not filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
#         abort(404)
#     return send_from_directory(image_dir, filename)
if __name__ == "__main__":
    app.run(debug=True)  # 添加这一行来启动Flask应用