from machine import Pin
from neopixel import NeoPixel

NUM_LEDS = 5
LED_PIN = 2

neopixel_pin = Pin(LED_PIN, Pin.OUT)
np = NeoPixel(neopixel_pin, NUM_LEDS)

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

# set all pixels to (r, g, b)
def set_color(r, g, b, silent=True):
    if not silent: print(f"setting {NUM_LEDS} leds to {r=} {g=} {b=}")
    for i in range(NUM_LEDS):
        np[i] = (r, g, b)
    np.write()

# turn off all pixels
def clear(silent=True):
    if not silent: print("the show is over")
    for i in range(NUM_LEDS):
        np[i] = (0, 0, 0)
        np.write()


def main():
    print("running main")


if __name__ == "__main__":
    print("we need to run main")
    main()

