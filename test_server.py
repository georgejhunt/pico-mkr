from micropyserver import MicroPyServer
from wifi_pico import WifiPico
import utils
## Quick start

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



if __name__ == "__main__":
    wfp = WifiPico()
    ip = wfp.connect_wifi()
    server = MicroPyServer(host=ip)
#     server = MicroPyServer(host=ip, port=8080)
    server.add_route("/", index)
    server.add_route("/stop", stop)
    server.add_route("/set_cookies", set_cookies)
    server.add_route("/get_cookies", get_cookies)
    server.start()

