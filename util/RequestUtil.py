#encoding: utf-8
import requests


def get(url,params):
    headers={
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'
    }
    resp = requests.get(url,data=params,headers=headers)
    return resp.text

def post(url,params):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:49.0) Gecko/20100101 Firefox/49.0'
    }
    resp = requests.post(url, data=params, headers=headers)
    return resp.text