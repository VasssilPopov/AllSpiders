# http://www.bulgaria.utre.bg/2018/01/07/471726-slunchev_kalendar_ponedelnik_8_yanuari_2018

def urlGetDate(url):
    pubDate=url.split('.bg/')[1][0:10].replace('/','.')
    return pubDate

def urlGetID(url):
    id=url.split('.bg/')[1][11:20].split('-')[0]
    return id

sURL='http://www.pleven.utre.bg/2018/01/08/471748-ot_dnes_zapochva_izplashtaneto_na_pensiite'

print urlGetDate(sURL)
print urlGetID(sURL)
