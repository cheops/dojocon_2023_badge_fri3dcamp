"""
blinky pixels
"""
from time import sleep, sleep_ms

from machine import Pin
from neopixel import NeoPixel

NUM_LEDS = 5
LED_PIN = 2

neopixel_pin = Pin(LED_PIN, Pin.OUT)
np = NeoPixel(neopixel_pin, NUM_LEDS)


# set all pixels to (r, g, b)
def set_color(r, g, b, silent=False):
    if not silent: print(f"setting {NUM_LEDS} leds to {r=} {g=} {b=}")
    for i in range(NUM_LEDS):
        np[i] = (r, g, b)
    np.write()


# turn off all pixels
def clear():
    print("the show is over")
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)
        np.write()


def flash(r, g, b, wait, count):
    print(f"flash the leds {count} times")
    for i in range(count, 0, -1):
        print(i)
        set_color(r, g, b, True)
        sleep_ms(wait)
        set_color(0, 0, 0, True)
        sleep_ms(wait)


def bounce(r, g, b, wait):
    print("bounce a led to the off state")
    for i in range(2 * NUM_LEDS):
        for j in range(NUM_LEDS):
            np[j] = (r, g, b)
        if (i // NUM_LEDS) % 2 == 0:
            np[i % NUM_LEDS] = (0, 0, 0)
        else:
            np[NUM_LEDS - 1 - (i % NUM_LEDS)] = (0, 0, 0)
        np.write()
        sleep_ms(wait)


def cycle(r, g, b, wait, times):
    print(f"cycling around {times} times")
    for _ in range(times):
        for i in range(NUM_LEDS):
            np[i] = (r, g, b)
            np.write()
            sleep_ms(wait)
            np[i] = (0, 0, 0)
            np.write()


# function to go through all colors
def wheel(pos, max):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if pos < 0 or pos > 255:
        return (0, 0, 0)
    if pos < 85:
        return (int(max - pos * 3 * max / 255), int(pos * 3 * max / 255), 0)
    if pos < 170:
        pos -= 85
        return (0, int(max - pos * 3 * max / 255), int(pos * 3 * max / 255))
    pos -= 170
    return (int(pos * 3 * max / 255), 0, int(max - pos * 3 * max / 255))


# rainbow
def rainbow_cycle(wait):
    print('aaah, "rainbows, butterflies and unicorns"')
    brightness = 20
    for j in range(255):
        for i in range(NUM_LEDS):
            rc_index = (i * 256 // NUM_LEDS) + j
            np[i] = wheel(rc_index & 255, brightness)
        np.write()
        sleep_ms(wait)


def main():
    print("running main")
    
    #set_color(100, 0, 0)
    
    #flash(50, 50, 50, 30, 10)

    #bounce(0, 0, 50, 70)
    
    #for _ in range(10): bounce(0, 0, 50, 70)
    
    #cycle(0, 50, 0, 30, 5)

    #rainbow_cycle(20)

    print("sleeping, ZZzz...")
    sleep(3)
    clear()
    print("done")
    
    
if __name__ == "__main__":
    print("we need to run main")
    main()
