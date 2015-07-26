#Killing the waitress process
waitressid=`ps aux | grep waitress |  awk -F ' ' '{print $2; exit;}'`
kill $waitressid

#Pulling changes
cd `pwd`
git pull
waitress-serve --port=80 webhooktest.wgsi:application