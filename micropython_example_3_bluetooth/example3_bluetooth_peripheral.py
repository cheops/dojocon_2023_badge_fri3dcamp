import bluetooth
import struct
import time
import pixels
from ble_advertising import advertising_payload

from micropython import const

_OUR_COMPANY_ID = const(b'\xff\xff')


class BLESimplePeripheral:
    def __init__(self, ble, name="ble_peripheral"):
        self._ble = ble
        self._ble.active(True)
        self._name = name
        self.man_spec_data()

    def man_spec_data(self, man_spec_data=b''):
        self._payload = advertising_payload(name=self._name, company_id=_OUR_COMPANY_ID, man_spec_data=man_spec_data)
        
    def advertise(self, interval_us=40000):
        self._ble.gap_advertise(interval_us, adv_data=self._payload, connectable=False)


def peripheral():
    ble = bluetooth.BLE()
    p = BLESimplePeripheral(ble, "ex3_ble")
    print("start advertising")
    
    for _ in range(0,10):
        for i in range(0, 255, 5):
            color = pixels.wheel(i, 255)
            print("broadcasting: ", color)
            pixels.set_color(*color)
            p.man_spec_data(struct.pack('<BBB', *color))
            p.advertise()
            time.sleep_ms(200)
    pixels.clear()

def main():
    print("running main")
    
    peripheral()


if __name__ == "__main__":
    print("we need to run main")
    main()
