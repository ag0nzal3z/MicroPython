# Conjunto de clases y funciones para la gestion
# de la conexion wifi en la esp32

def wifi_connect(SSDI, KEY):
    import network
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        print('connecting to network...')
        wlan.connect(SSDI, KEY)
        while not wlan.isconnected():
            pass
    print('network config:', wlan.ifconfig())

