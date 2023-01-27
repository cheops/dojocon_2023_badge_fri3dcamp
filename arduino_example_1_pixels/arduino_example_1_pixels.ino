// Arduino settings
// Board: "ESP32 Dev Module"

/**
 * Dojocon Belgium 2023 workshop Badge Fri3dcamp
 * Arduino example 1 pixels
 * control the 5 neopixels on the badge
 * cycle through rainbow colors
 */

// 
// #include <Badge2020_TFT.h>

#include <Adafruit_NeoPixel.h>

static const uint8_t LED_PIN = 2;

// How many NeoPixels are attached to the Arduino?
static const uint8_t LED_COUNT = 5;

// Declare our NeoPixel strip object:
Adafruit_NeoPixel strip(LED_COUNT, LED_PIN, NEO_GRB + NEO_KHZ800);
// Argument 1 = Number of pixels in NeoPixel strip
// Argument 2 = Arduino pin number (most are valid)
// Argument 3 = Pixel type flags, add together as needed:
//   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
//   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)

void setup() {
  strip.begin();
  strip.clear();
  strip.show();
}

uint16_t hue = 0;
uint8_t saturation = 255;
uint8_t brightness = 100;
uint32_t rgbcolor = 0;

void loop() {
  manual_rainbow();
  
  //manual_rainbow_with_gamma();
  
  //adafruit_neopixel_rainbow();

  delay(10);
}

void manual_rainbow() {
  // https://learn.adafruit.com/adafruit-neopixel-uberguide/arduino-library-use#hsv-hue-saturation-value-colors-dot-dot-dot-3024464
  brightness = 75;
  rgbcolor = strip.ColorHSV(hue, saturation, brightness);
  strip.fill(rgbcolor);
  strip.show();
  hue += 65535/500; // next color from the rainbow
}

void manual_rainbow_with_gamma() {
  // https://learn.adafruit.com/adafruit-neopixel-uberguide/arduino-library-use#hsv-hue-saturation-value-colors-dot-dot-dot-3024464
  // gamma corrected rainbow
  brightness = 150;
  rgbcolor = strip.gamma32(strip.ColorHSV(hue, saturation, brightness));
  strip.fill(rgbcolor);
  strip.show();
  hue += 65535/500; // next color from the rainbow
}

void adafruit_neopixel_rainbow() {
  // https://github.com/adafruit/Adafruit_NeoPixel/blob/master/Adafruit_NeoPixel.cpp#L3415
  int8_t reps = 1;
  bool gammify = true;

  strip.rainbow(hue, reps, saturation, brightness, gammify);
  strip.show();
  hue += 65535/5/100;
}
