import bluetooth
import struct
import time
import pixels
from ble_advertising import decode_man_spec_data, decode_name

from micropython import const
_IRQ_SCAN_RESULT = const(5)
_IRQ_SCAN_DONE = const(6)

_ADV_IND = const(0x00)
_ADV_DIRECT_IND = const(0x01)
_ADV_SCAN_IND = const(0x02)
_ADV_NONCONN_IND = const(0x03)
_ADV_SCAN_RSP = const(0x04)

_OUR_COMPANY_ID = const(b'\xff\xff')

class BLESimpleCentral:
    def __init__(self, ble, wanted_name):
        self._ble = ble
        self._ble.active(True)
        self._ble.irq(self._irq)
        self._wanted_name = wanted_name
        self._scan_callback = None
        self._stop_scanning = False

    def _irq(self, event, data):
        if event == _IRQ_SCAN_RESULT:
            addr_type, addr, adv_type, rssi, adv_data = data
            #print("addr_type=", addr_type, ", addr=", bytes(addr), ", adv_type=", adv_type, ", rssi=", rssi, "adv_data=", bytes(adv_data))
            #print("name: ", decode_name(bytes(adv_data)))
            if adv_type == _ADV_SCAN_IND:
                if self._wanted_name == decode_name(adv_data):
                    c_id, man_spec_data = decode_man_spec_data(adv_data)
                    if _OUR_COMPANY_ID == c_id:
                        # Found the required broadcast message, call our callback
                        if self._scan_callback:
                            self._scan_callback(bytes(man_spec_data))

        elif event == _IRQ_SCAN_DONE:
            # scanning finished, restart it if needed
            if not self._stop_scanning:
                self._ble.gap_scan(2_000, 120_000, 30_000, False)  # scan during 2 seconds, every 120ms for 30ms

    def scan(self, callback=None):
        self._scan_callback = callback
        self._ble.gap_scan(2_000, 120_000, 30_000, False)  # scan during 2 seconds, every 120ms for 30ms
    
    def stop_scanning(self):
        print("we will soon stop scanning")
        self._stop_scanning = True


def central():
    ble = bluetooth.BLE()
    central = BLESimpleCentral(ble, "ex3_ble")
    
    last_data = b''

    def on_scan(data):
        nonlocal last_data
        if data != last_data:
            last_data = data
            color = struct.unpack('<BBB', data)
            print("received: ", color)
            pixels.set_color(*color)

    central.scan(callback=on_scan)
    
    time.sleep(100)
    
    central.stop_scanning()

def main():
    print("running main")
    
    central()


if __name__ == "__main__":
    print("we need to run main")
    main()

