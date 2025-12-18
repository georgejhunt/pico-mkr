import secrets

class WifiPico():
    def connect_wifi(self):
        ### Typical Wi-Fi connection code for ESP board
        
        #import esp
        import network
        import time
        import ubinascii
        #++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++-
        mac = ubinascii.hexlify(network.WLAN().config('mac'),':').decode()
        print("MAC: " + mac)
        # --- AP Configuration ---
        ssid = 'Pico2-w' # Your network name
        password = '2b2b2b2b2b' # Your network password (min 8 chars)

        # --- Setup AP ---
        ap = network.WLAN(network.AP_IF) # Access Point Interface
        ap.active(True) # Turn on the AP
        ap.config(essid=ssid, password=password) # Configure SSID and password

        # Wait for AP to be active
        while not ap.active():
            time.sleep(0.1)
            pass
        
        print("Connected... IP: %s" %(str(ap.ifconfig())),)
        #print("Channel : %s"%(wlan.config("channel")))
        return ap.ifconfig()[0]
    
if __name__ == "__main__":
    wfp = WifiPico()
    wfp.connect_wifi()