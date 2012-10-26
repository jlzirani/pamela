sudo arp-scan -R -l | awk '{ print $2 }' | grep :.*: | sort | uniq | python /home/nginx/pamela/script/mac.py > /home/nginx/pamela/www/mac.json
