#encoding: utf-8
import mimetypes

import requests
from flask import Flask, request, Blueprint, make_response
from requests.packages.urllib3 import response

from util import RequestUtil
from util.Aes import getAllParams
import json

app = Flask(__name__)

#定义基础url
URL="http://music.163.com/discover/playlist/"
song_url="http://music.163.com/weapi/song/enhance/player/url?csrf_token="
order_url="http://music.163.com/playlist?id="

api = Blueprint('api',__name__,template_folder='templates')

#首页api
@api.route('/api/playList')
def playList():
    order = request.args.get('order')
    offset = request.args.get('offset')
    if (None == order or '' == order):
        order = 'hot'
    if (offset == None or ''== order):
        offset = 35
    target_url = URL + "?order=" + order + "&offset=" + offset
    text = RequestUtil.get(target_url, {})
    return text

#获取某个歌单的数据s
@api.route('/api/orderList')
def orderList():
    id = request.args.get('id')
    target_url=order_url+id
    return RequestUtil.get(target_url,{})


#获取歌曲api
@api.route('/api/getSongUrl')
def getSongUrl():
    song_id = request.args.get('song_id')
    if (None == song_id or ''==song_id):
        return 'error'
    params = getAllParams(song_id)
    resp = RequestUtil.post(song_url,params)
    #获取json中的url
    #jsonObj = json.loads(json_string)
    jsonObj=json.loads(resp)
    data = jsonObj['data'][0]
    if(None==data):
        return 'error'
    try:
        url = data['url']
        res={
            'url':url,
            'msg':'success'
        }
        return json.dumps(res)
    except BaseException:
        print '获取url参数异常'
        return 'error'

#下载歌曲方法
@api.route('/api/download')
def download():
    song_id=request.args.get('song_id')
    songName=request.args.get('songName')+'.mp3'
    if (None == song_id or ''==song_id):
        return 'error'
    params = getAllParams(song_id)
    resp = RequestUtil.post(song_url,params)
    #获取json中的url
    jsonObj=json.loads(resp)
    data = jsonObj['data'][0]
    if (None == data):
        return 'error'
    try:
        url = data['url']
        r=requests.get(url)
        if r.status_code !=200:
            raise Exception('超时-----')
        response = make_response(r.content)
        response.headers['Content-Type']='audio/x-mpeg;charset=utf-8'
        response.headers['Content-Disposition'] = 'attachment; filename='+songName.encode();
        return response
    except Exception as e:
        print '获取url参数异常'
        print str(e)
        return 'error'



if __name__ == '__main__':
    s = json.loads(u'{"data":[{"id":404783205,"url":"http://m10.music.126.net/20170926091916/25e9f024f5c21fd3815279edcf202675/ymusic/f650/d398/1e45/3323a9cb30d27e9f3f8c90816914546e.mp3","br":128000,"size":3433160,"md5":"3323a9cb30d27e9f3f8c90816914546e","code":200,"expi":1200,"type":"mp3","gain":-0.7799,"fee":8,"uf":null,"payed":0,"flag":0,"canExtend":false}],"code":200}')
    print s
    print s.keys()
    print s['data'][0]['url']

