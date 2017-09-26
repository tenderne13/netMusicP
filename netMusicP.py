# encoding: utf-8
from flask import Flask, render_template, request

from api.Api import api

app = Flask(__name__)

#引入api路由
app.register_blueprint(api)


@app.route('/')
def index():
    return render_template('index/playList.html')

@app.route('/route/orderList')
def orderList():
    id = request.args.get('id')
    return render_template('index/orderList.html',id=id)


if __name__ == '__main__':
    app.debug = True
    app.run()
