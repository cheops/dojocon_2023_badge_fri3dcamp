// Arduino settings
// Board: "ESP32 Dev Module"

/**
 * Dojocon Belgium 2023 workshop Badge Fri3dcamp
 * Arduino example 2 tft
 * draw the fri3d camp logo on the badge
 * change the color of the logo (more rainbows)
 * rainbow inspiration from https://github.com/Bodmer/TFT_eFEX/blob/master/examples/Rainbow_Luminance/Rainbow_Luminance.ino
 */

#include <Badge2020_TFT.h>
#include "fri3d_logo.h"

Badge2020_TFT tft;

byte red = 31;
byte green = 0;
byte blue = 0;
byte state = 0;
uint16_t colour = red << 11; // Colour order is RGB 5+6+5 bits each, so shift 6+5=11

void setup() {
  tft.init(240, 240);
  tft.setRotation( 2 );
  tft.fillScreen(ST77XX_BLACK);

  draw_white_logo();
}

void loop() {
  //draw_rainbow_logo();
}

void draw_white_logo()
{
  tft.drawBitmap(0, 0, fri3d_logo, 240, 240, ST77XX_WHITE);
}

void draw_rainbow_logo()
{
  for (uint16_t i = 0; i <= 159; i++) {
    colour = rainbowColor(i);
    tft.drawBitmap(0, 0, fri3d_logo, 240, 240, colour);
    delay(10);
  }
}


// https://github.com/Bodmer/TFT_eFEX/blob/master/TFT_eFEX.cpp#L581
/***************************************************************************************
** Function name:           rainbowColor
** Description:             Return a 16 bit rainbow colour
***************************************************************************************/

  // If 'spectrum' is in the range 0-159 it is converted to a spectrum colour
  // from 0 = red through to 127 = blue to 159 = violet
  // Extending the range to 0-191 adds a further violet to red band
 
uint16_t rainbowColor(uint8_t spectrum)
{
  spectrum = spectrum%192;
  
  uint8_t red   = 0; // Red is the top 5 bits of a 16 bit colour spectrum
  uint8_t green = 0; // Green is the middle 6 bits, but only top 5 bits used here
  uint8_t blue  = 0; // Blue is the bottom 5 bits

  uint8_t sector = spectrum >> 5;
  uint8_t amplit = spectrum & 0x1F;

  switch (sector)
  {
    case 0:
      red   = 0x1F;
      green = amplit; // Green ramps up
      blue  = 0;
      break;
    case 1:
      red   = 0x1F - amplit; // Red ramps down
      green = 0x1F;
      blue  = 0;
      break;
    case 2:
      red   = 0;
      green = 0x1F;
      blue  = amplit; // Blue ramps up
      break;
    case 3:
      red   = 0;
      green = 0x1F - amplit; // Green ramps down
      blue  = 0x1F;
      break;
    case 4:
      red   = amplit; // Red ramps up
      green = 0;
      blue  = 0x1F;
      break;
    case 5:
      red   = 0x1F;
      green = 0;
      blue  = 0x1F - amplit; // Blue ramps down
      break;
  }

  return red << 11 | green << 6 | blue;
}


// https://github.com/Bodmer/TFT_eFEX/blob/master/TFT_eFEX.cpp#L548
/***************************************************************************************
** Function name:           luminance
** Description:             return a 16 bit colour with reduced luminance
***************************************************************************************/
uint16_t luminance(uint16_t color, uint8_t luminance)
{
  // Extract rgb colours and stretch range to 0 - 255
  uint16_t r = (color & 0xF800) >> 8; r |= (r >> 5);
  uint16_t g = (color & 0x07E0) >> 3; g |= (g >> 6);
  uint16_t b = (color & 0x001F) << 3; b |= (b >> 5);

  b = ((b * (uint16_t)luminance + 255) >> 8) & 0x00F8;
  g = ((g * (uint16_t)luminance + 255) >> 8) & 0x00FC;
  r = ((r * (uint16_t)luminance + 255) >> 8) & 0x00F8;

  return (r << 8) | (g << 3) | (b >> 3);
}

