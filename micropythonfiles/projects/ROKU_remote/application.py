import urequests
import network

WIFI_SSID = "Lee"
WIFI_PASSWORD = "Peachdr.4308"
ROKU_IP = "192.168.1.235"

def connect_to_wifi(ssid, password):
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        print("Connecting to WiFi...")
        sta_if.active(True)
        sta_if.connect(ssid, password)
        while not sta_if.isconnected():
            pass
        print("Connected to WiFi:", sta_if.ifconfig())

def send_roku_command(command):
    url = "http://" + ROKU_IP + ":8060/keypress/" + command
    response = urequests.post(url)
    print("Command sent:", command)
    print("Response:", response.text)
    response.close()

connect_to_wifi(WIFI_SSID, WIFI_PASSWORD)

# Example: Send the "Home" button command
send_roku_command("Home")
