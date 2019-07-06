# BgNews Index


### [DejaVu Chrome](https://chrome.google.com/webstore/detail/dejavu-elasticsearch-web/jopjeaiilkcibeohjdmejhoifenbnmlh)
https://elastic:kx4dHm4HDf5eyoKaBkdgZIBb@3840179f313943c88f940d99436f39f0.us-east-1.aws.found.io:9243

```
	# Dejavu Elastic UI
	# Source: https://hub.docker.com/r/appbaseio/dejavu/

	#http.port: 9200
	#http.cors.allow-origin: 'http://35.245.142.177:1358'
	http.cors.allow-origin: 'chrome-extension://jopjeaiilkcibeohjdmejhoifenbnmlh'
	http.cors.enabled: true
	http.cors.allow-headers: X-Requested-With,X-Auth-Token,Content-Type,Content-Length,Authorization
	http.cors.allow-credentials: true
```
## Medias

[GDocs](https://docs.google.com/document/d/1H7KxtLhsGuHj9_nk0eIij22IrjJWSnwd2Uj-r5Ery50/edit)

24chasa
Actualno
BgOnAir
Blitz
BNews
Classa
ClubZ
Dnes
Duma
Epicenter
Faktor
Mediapool
StandartNews 
Trud
Cross
Dnevnik
Focus
Monitor
News
Novinite
OffNews
PIK



###ETemplate request
elasticsearch_loader --index bgnews  --http-auth elastic:XXXXX --es-host https://XXXX.us-east-1.aws.found.io:9243 --type _doc json 24chasa-2019-05-31.json --lines

ls -file | % {elasticsearch_loader.exe --index bgnews  --http-auth elastic:ixli7UsFec9yQpAKCE8f5S2R --es-host https://c5f1d8c902a0404fb204ea95910b7811.us-east-1.aws.found.io:9243  --type json json $_.fullname --lines}


## Deployments passwords

### Prod
elasticsearch_loader --index bgnews  --http-auth elastic:kx4dHm4HDf5eyoKaBkdgZIBb --es-host https://3840179f313943c88f940d99436f39f0.us-east-1.aws.found.io:9243 --type _doc json 24chasa-2019-05-31.json --lines

https://3840179f313943c88f940d99436f39f0.us-east-1.aws.found.io:9243
elastic:kx4dHm4HDf5eyoKaBkdgZIBb

https://elastic:kx4dHm4HDf5eyoKaBkdgZIBb@3840179f313943c88f940d99436f39f0.us-east-1.aws.found.io:9243


## Kibana

.es("Бойко Борисов", index=bgnews, timefield=date),
.es(ГЕРБ, index=bgnews, timefield=date),
.es("Цветанов", index=bgnews, timefield=date)

.es("бежанци | мигранти", index=bgnews, timefield=date),

.es("джендър", index=bgnews, timefield=date),
.es("истанбулската конвенция", index=bgnews, timefield=date),
.es("семейни ценности", index=bgnews, timefield=date),

### Queries

```
put bgnews

DELETE bgnews

GET _search
{
  "query": {
    "match_all": {}
  }
}

GET /_search
{
    "query": {
        "match" : {
            "text" : "днес"
        }
    }
}

GET /_search
{
    "query": {
        "match" : {
            "text" : "стратегията за детето"
        }
    }
}

get bgnews/_mapping

get bgnews/_search?pretty


PUT bgnews 
{
  "mappings": {
    "properties": { 
      "title":    { "type": "text"  }, 
      "text":     { "type": "text"  }, 
      "url":      { "type": "text" },  
      "date":  {
        "type":   "date", 
        "format": "yyyy.MM.dd"
      }
    }
  }
}

GET  _search
{
    "query": {
        "range" : {
            "date" : {
                "gte" : "now-10d/d",
                "lt" :  "now/d"
            }
        }
    }
}

```

# Semantic Vectors Experiments

org.apache.lucene.analysis.bg.BulgarianAnalyzer

-minfrequency 3

Тематични гнезда: 

мигранти, бежанци, сирийци, афганистанци, нашественици

Пеевски

ГЕРБ

Аборт

джендър, социален пол, 

гей, лгбт

истанбулска конвенция, традиционни ценности

Русия, Путин

ЕС, НАТО, Европа, Русия, САЩ