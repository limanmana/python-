import urllib.request

def get_proxy():
    resp = urllib.request.urlopen('http://192.168.221.221:5010')