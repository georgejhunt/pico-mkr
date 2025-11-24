from micropyserver import MicroPyServer
import utils
## Quick start
def connect_wifi():
    ### Typical Wi-Fi connection code for ESP board
    
    #import esp
    import network
    import time
    import ubinascii

    wlan_id = "piconet"
    wlan_pass = "2b2b2b2b2b"

    mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
    print("MAC: " + mac)

    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    while wlan.status() is network.STAT_CONNECTING:
        time.sleep(1)
    while not wlan.isconnected():
        wlan.connect(wlan_id, wlan_pass)
    print("Connected... IP: " + wlan.ifconfig()[0])  

    
server = MicroPyServer()


def index(request):
    server.send('OK')


def stop(request):
    server.stop()


def set_cookies(request):
    cookies_header = utils.create_cookie("name", "value", expires="Sat, 01-Jan-2030 00:00:00 GMT")
    utils.send_response(server, "OK", extend_headers=[cookies_header])


def get_cookies(request):
    cookies = utils.get_cookies(request)
    utils.send_response(server, str(cookies))


server.add_route("/", index)
server.add_route("/stop", stop)
server.add_route("/set_cookies", set_cookies)
server.add_route("/get_cookies", get_cookies)

connect_wifi()
server.start()
