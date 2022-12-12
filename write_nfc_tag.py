import time
import binascii
from pn532pi import Pn532, pn532
from pn532pi import Pn532Spi
from pn532pi import Pn532I2c

# PN532_I2C = Pn532I2c(1)
# nfc = Pn532(PN532_I2C)

PN532_SPI = Pn532Spi(Pn532Spi.SS0_GPIO8)
nfc = Pn532(PN532_SPI)

def setup():
    nfc.begin()

    versiondata = nfc.getFirmwareVersion()
    if (not versiondata):
        print("Didn't find PN53x board")
        raise RuntimeError("Didn't find PN53x board")  # halt
    print("Found chip PN5 {:#x} Firmware ver. {:d}.{:d}".format((versiondata >> 24) & 0xFF, (versiondata >> 16) & 0xFF, (versiondata >> 8) & 0xFF))
    nfc.SAMConfig()
    print("Waiting for an ISO14443A Card ...")

def loop():
    success, uid = nfc.readPassiveTargetID(pn532.PN532_MIFARE_ISO14443A_106KBPS)

    if (success):
        print("Found an ISO14443A card")
        print("UID Length: {:d}".format(len(uid)))
        print("UID Value: {}".format(binascii.hexlify(uid)))
        index = 0

        if (len(uid) == 7):
            print("Mifare Ultralight Tag)")
            
            with open ('pill_data.txt','r') as r:
                i = 4
                for line in r:
                    line = line.strip("\n ")
                    if len(line) == 16:
                        encoded_string =line.encode()
                        byte_data=bytearray(encoded_string)
                        success = nfc.mifareultralight_WritePage(i, byte_data[0:4])
                        success = nfc.mifareultralight_WritePage(i+1, byte_data[4:8])
                        success = nfc.mifareultralight_WritePage(i+2, byte_data[8:12])
                        success = nfc.mifareultralight_WritePage(i+3, byte_data[12:16])
                        i += 4
            if (success):
                print("Writing pill data success")
                return True
            else:
                print("Ooops ... unable to read the requested page!?")

    return False

if __name__ == '__main__':
    setup()
    found = loop()
    while not found:
        found = loop()