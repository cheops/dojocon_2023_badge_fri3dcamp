"""
screen micropython driver used is https://github.com/russhughes/st7789_mpy
more documentation about it's methods https://github.com/devbis/st7789_mpy
"""
from machine import Pin, SPI
import gc
import st7789

def init_screen():
    global screen
    print("init the screen")
    spi = SPI(2, baudrate=40000000, polarity=1)
    pcs = Pin(5, Pin.OUT)
    pdc = Pin(33, Pin.OUT)

    gc.collect()  # Precaution before instantiating framebuffer

    screen = st7789.ST7789(
        spi=spi,
        width=240,
        height=240,
        cs=pcs,
        dc=pdc,
        buffer_size=240 * 240 * 2)
    screen.init()
    screen.fill(st7789.WHITE)

def logo_coderdojo():
    import logo_coderdojo
    screen.bitmap(logo_coderdojo, 0, 0)
    print("drawing logo coderdojo")

def logo_coderdojo_smooth():
    import logo_coderdojo_smooth
    screen.bitmap(logo_coderdojo_smooth, 0, 0)
    print("drawing logo coderdojo smooth")

def logo_fri3d():
    import logo_fri3d
    screen.bitmap(logo_fri3d, 0, 0)
    print("drawing logo fri3d")

def logo_fri3d_green_circles():
    import logo_fri3d_green_circles
    screen.bitmap(logo_fri3d_green_circles, 0, 0)
    print("drawing logo fri3d green circles")

def main():
    print("running main")
    init_screen()
    
    logo_coderdojo()
    #logo_coderdojo_smooth()
    #logo_fri3d()
    #logo_fri3d_green_circles()


if __name__ == "__main__":
    print("we need to run main")
    main()
