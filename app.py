from flask import Flask
from datetime import datetime  # 导入datetime模块

app = Flask(__name__)

@app.route("/")
def index():
    current_time = datetime.now()  # 获取当前时间
    return current_time.strftime('%Y-%m-%d %H:%M:%S')  # 格式化时间并返回
if __name__ == "__main__":
    app.run(debug=True)  # 添加这一行来启动Flask应用