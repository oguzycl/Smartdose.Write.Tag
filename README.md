sudo apt-get update
sudo apt-get upgrade
sudo apt install python3-pip
sudo pip install pn532pi
sudo pip install spidev
cd ~
git clone https://github.com/Gadgetoid/py-spidev.git
cd py-spidev
sudo python setup.py install
sudo python3 setup.py install
sudo raspi-config interface option -> spi -> enable
sudo reboot
git clone https://github.com/yongatek-industrial/Smartdose.Write.Tag.git
cd Smartdose.Write.Tag
python3 Write_nfc_tag.py

-- PIN CONNECTIONS --
pn532 sck -> RPI pin 23
pn532 miso -> RPI pin 21
pn532 mosi -> RPI pin 19
pn532 ss -> RPI pin 24
pn532 vcc -> RPI pin 1
pn532 gnd -> RPI pin 6

info: Enter the pill data into the pill_data.txt file. format: yymmddhhmmssiiii
yy -> year
mm -> month
dd -> day
hh -> hour
mm -> minute
ss -> section on grid
iiii -> id for pill

ex = day: 2022/12/10 hour: 15:45 section: 01 pill id: 0001
input must be 2212101545010001
each line must contain one pill data as it shown in the pill_data.txt

info: nfc tag type must be mifareultralight and reader pn532 nfc/rfid reader writer
