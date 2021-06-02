from flask import Flask
from flask_sqlalchemy import SQLAlchemy


class Config(object):
    """项目的配置"""
    DEBUG=True

    # 为数据库 添加配置
    SQLALCHEMY_DATABASE_URI="mysql://root:yanpenggong@127.0.0.1:3306/information8"
    SQLALCHEMY_TRACK_MODIFICATIONS=False

app=Flask(__name__)
# 加载配置
app.config.from_object(Config)

# 初始化数据库
db=SQLAlchemy(app)

@app.route('/')
def index():
    return 'index333'

if __name__=='__main__':
    app.run(debug=True)