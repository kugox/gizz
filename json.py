__author__ = 'Kugox'
import demjson

data = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]
js=demjson.encode(data)
print(js)
dd=demjson.decode(js)
print(dd)