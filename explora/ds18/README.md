# DS18B20 OneWire
## Configuration
Activer le support du protocole 1-Wire (sudo raspi-config). GPIO 4 ?
Ajouter les modules suivants dans _/etc/modules_:
* w1-gpio pullup=1 (sudo modprobe w1-gpio)
* w1-therm (sudo modprobe w1-therm)
Ajouter la ligne suivante dans _/boot/config.txt_
* dtoverlay=w1-gpio
## Récupération température
cd /sys/bus/w1/devices/28-xxxx  
cat temperature (ou cat w1_slave) ==> A diviser par 1000
