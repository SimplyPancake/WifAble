# install arpspoof (dsniff)
# I believe we wil not need this...
apt-get -y install dsniff

# install mitmproxy
apt-get -y install python3-dev python3-pip libffi-dev libssl-dev
pip3 install --user mitmproxy

# install BeautifulSoup
pip3 install beautifulsoup4
