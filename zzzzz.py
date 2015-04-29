import json
import urllib
import re

class losowanie(object):
    def __init__(self, name, Lotto, Ekstra_Pensja, Mini_Lotto, Multi_multi):
        self.name = name
        self.Lotto = Lotto
        self.Ekstra_Pensja = Ekstra_Pensja
        self.Mini_Lotto = Mini_Lotto
        self.Multi_multi = Multi_multi
        self.out = {'name': self.name, 'children': [{'name': self.Lotto},{'name': self.Ekstra_Pensja},{'name': self.Mini_Lotto},{'name': self.Multi_multi}]}

def html(link):
    req = (link)
    resp = urllib.urlopen(req)
    respData = resp.read()
    return respData

def lotto(respData):
    parsedData = re.findall(r'wynik_lotto">\d{1,2}',str(respData))
    replacedData = [date.replace('wynik_lotto">','') for date in parsedData]
    print "Lotto"
    return replacedData

def ekstrapensja(respData):
    parsedData2 = re.findall(r'wynik_ekstra-pensja">\d{1,2}',str(respData))
    replacedData2 = [date.replace('wynik_ekstra-pensja">','') for date in parsedData2]
    print "Ekstra Pensja"
    return replacedData2

def minilotto(respData):
    parsedData3 = re.findall(r'mini-lotto">\d{1,2}',str(respData))
    replacedData3 = [date.replace('mini-lotto">','') for date in parsedData3]
    print "Mini Lotto"
    return replacedData3

def multimulti(respData):
    parsedData4 = re.findall(r'wynik_multi-multi">\d{1,2}',str(respData))
    replacedData4 = [date.replace('wynik_multi-multi">','') for date in parsedData4]
    print "Multi multi"
    return replacedData4


respData = html("http://www.lotto.pl")
a = lotto(respData)
b = ekstrapensja(respData)
c = minilotto(respData)
d= multimulti(respData)



me = losowanie('Losowanie', a, b, c, d).out

with open('flare.json', 'w') as output:
	json.dump(me, output)