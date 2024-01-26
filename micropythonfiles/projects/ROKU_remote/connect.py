import network
import webrepl

def wlan_connect(ssid='Lee', password='Peachdr.4308'):
    wlan = network.WLAN(network.STA_IF)
    if not wlan.active() or not wlan.isconnected():
        wlan.active(True)
        print('Connecting to:', ssid)
        wlan.connect(ssid, password)
        while not wlan.isconnected():
            pass
        print('Network config:', wlan.ifconfig())
wlan_connect()
webrepl.start()
