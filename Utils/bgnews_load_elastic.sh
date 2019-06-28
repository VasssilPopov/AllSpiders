#!/bin/bash

# Config
ELASTIC_INDEX="bgnews"
ELASTIC_AUTH="elastic:kx4dHm4HDf5eyoKaBkdgZIBb"
ELASTIC_HOST="https://3840179f313943c88f940d99436f39f0.us-east-1.aws.found.io:9243"
ALL_SPIDERS_DIR="/home/peio/dev/AllSpiders/"

cat BgNews.sites | while read line 

do 
 echo $line 
 sleep 3	

#  "AllSpiders/$line/Reports/*.json"
# echo  "AllSpiders/$line/Reports/*.json"

elasticsearch_loader --index $ELASTIC_INDEX  --http-auth $ELASTIC_AUTH --es-host $ELASTIC_HOST --type _doc json $ALL_SPIDERS_DIR/$line/Reports/*.json  --lines

# For the EP election month only:
# AllSpiders/Dnevnik/Reports/Dnevnik-2019-05-

#echo "Loading for May 2018 Only!"
#sleep 1
#elasticsearch_loader --index bgnews-may2019  --http-auth elastic:kx4dHm4HDf5eyoKaBkdgZIBb --es-host https://3840179f313943c88f940d99436f39f0.us-east-1.aws.found.io:9243 --type _doc json AllSpiders/$line/Reports/$line-2019-05-*.json  --lines



done

exit 0