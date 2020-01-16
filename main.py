# -*- coding:UTF-8 -*-
# Copyright (c) 2019 Xavier Carcelle
# See LICENSE for details.

#--------------Driver Library-----------------#
from time import sleep
import RPi.GPIO as GPIO
import OLED_Driver as OLED
#--------------Image Library---------------#
from PIL  import Image
from PIL import ImageDraw
from PIL import ImageFont
from PIL import ImageColor
#-------------Test Display Functions---------------#

def Test_Text():
    image = Image.new("RGB", (OLED.SSD1351_WIDTH, OLED.SSD1351_HEIGHT), "WHITE")
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("FreeMonoBold.ttf", 12, encoding="unic")
    # font = ImageFont.truetype('cambriab.ttf',24)
    draw.text((0, 0), 'IGREK', fill = "WHITE", font = font)
    OLED.Display_Image(image)


def Test_Pattern():
    image = Image.new("RGB", (OLED.SSD1351_WIDTH, OLED.SSD1351_HEIGHT), "WHITE")
    draw = ImageDraw.Draw(image)
    draw.line([(0,204),(127,204)],fill = "WHITE",  width = 16)
    draw.line([(0,104),(127,104)],fill = "WHITE",  width = 16)
    OLED.Display_Image(image)


def Test_Lines():
    image = Image.new("RGB", (OLED.SSD1351_WIDTH, OLED.SSD1351_HEIGHT), "BLACK")
    draw = ImageDraw.Draw(image)

    for x in range(0, int((OLED.SSD1351_WIDTH-1)/2), 6):
        draw.line([(0, 0), (x, OLED.SSD1351_HEIGHT - 1)], fill = "RED", width = 1)
        draw.line([(0, 0), ((OLED.SSD1351_WIDTH-1) - x, OLED.SSD1351_HEIGHT - 1)], fill = "RED", width = 1)
        draw.line([(0, 0), (OLED.SSD1351_WIDTH - 1, x)], fill = "RED", width = 1)
        draw.line([(0, 0), (OLED.SSD1351_WIDTH - 1, (OLED.SSD1351_HEIGHT-1) - x)], fill = "RED", width = 1)
        OLED.Display_Image(image)
    OLED.Delay(250)
    draw.rectangle([0, 0, OLED.SSD1351_WIDTH - 1, OLED.SSD1351_HEIGHT - 1], fill = "BLACK", outline = "BLACK")

    for x in range(0, int((OLED.SSD1351_WIDTH-1)/2), 6):
        draw.line([(OLED.SSD1351_WIDTH - 1, 0), (x, OLED.SSD1351_HEIGHT - 1)], fill = "YELLOW", width = 1)
        draw.line([(OLED.SSD1351_WIDTH - 1, 0), (x + int((OLED.SSD1351_WIDTH-1)/2), OLED.SSD1351_HEIGHT - 1)], fill = "YELLOW", width = 1)
        draw.line([(OLED.SSD1351_WIDTH - 1, 0), (0, x)], fill = "YELLOW", width = 1)
        draw.line([(OLED.SSD1351_WIDTH - 1, 0), (0, x + int((OLED.SSD1351_HEIGHT-1)/2))], fill = "YELLOW", width = 1)
        OLED.Display_Image(image)
    OLED.Delay(250)
    draw.rectangle([0, 0, OLED.SSD1351_WIDTH - 1, OLED.SSD1351_HEIGHT - 1], fill = "BLACK", outline = "BLACK")

    for x in range(0, int((OLED.SSD1351_WIDTH-1)/2), 6):
        draw.line([(0, OLED.SSD1351_HEIGHT - 1), (x, 0)], fill = "BLUE", width = 1)
        draw.line([(0, OLED.SSD1351_HEIGHT - 1), (x + int((OLED.SSD1351_WIDTH-1)/2), 0)], fill = "BLUE", width = 1)
        draw.line([(0, OLED.SSD1351_HEIGHT - 1), (OLED.SSD1351_WIDTH - 1, x)], fill = "BLUE", width = 1)
        draw.line([(0, OLED.SSD1351_HEIGHT - 1), (OLED.SSD1351_WIDTH - 1, x + (OLED.SSD1351_HEIGHT-1)/2)], fill = "BLUE", width = 1)
        OLED.Display_Image(image)
    draw.rectangle([0, 0, OLED.SSD1351_WIDTH - 1, OLED.SSD1351_HEIGHT - 1], fill = "BLACK", outline = "BLACK")
    OLED.Delay(250)
    
    for x in range(0, int((OLED.SSD1351_WIDTH-1)/2), 6):
        draw.line([(OLED.SSD1351_WIDTH - 1, OLED.SSD1351_HEIGHT - 1), (x, 0)], fill = "GREEN", width = 1)
        draw.line([(OLED.SSD1351_WIDTH - 1, OLED.SSD1351_HEIGHT - 1), (x + int((OLED.SSD1351_WIDTH-1)/2), 0)], fill = "GREEN", width = 1)
        draw.line([(OLED.SSD1351_WIDTH - 1, OLED.SSD1351_HEIGHT - 1), (0, x)], fill = "GREEN", width = 1)
        draw.line([(OLED.SSD1351_WIDTH - 1, OLED.SSD1351_HEIGHT - 1), (0, x + int((OLED.SSD1351_HEIGHT-1)/2))], fill = "GREEN", width = 1)
        OLED.Display_Image(image)
    draw.rectangle([0, 0, OLED.SSD1351_WIDTH - 1, OLED.SSD1351_HEIGHT - 1], fill = "BLACK")


def Test_HV_Lines():
    image = Image.new("RGB", (OLED.SSD1351_WIDTH, OLED.SSD1351_HEIGHT), "WHITE")
    draw = ImageDraw.Draw(image)
    
    for y in range(0, OLED.SSD1351_HEIGHT - 1, 5):
        draw.line([(0, y), (OLED.SSD1351_WIDTH - 1, y)], fill = "WHITE", width = 1)
    # OLED.Display_Image(image)
    OLED.Delay(250)
    for x in range(0, OLED.SSD1351_WIDTH - 1, 5):
        draw.line([(x, 0), (x, OLED.SSD1351_HEIGHT - 1)], fill = "WHITE", width = 1)
    OLED.Display_Image(image)



def Test_Rects():
    image = Image.new("RGB", (OLED.SSD1351_WIDTH, OLED.SSD1351_HEIGHT), "BLACK")
    draw = ImageDraw.Draw(image)
    
    for x in range(0, int((OLED.SSD1351_WIDTH-1)/2), 6):
        draw.rectangle([(x, x), (OLED.SSD1351_WIDTH- 1 - x, OLED.SSD1351_HEIGHT-1 - x)], fill = None, outline = "WHITE")
    OLED.Display_Image(image)


def Test_FillRects(): 
    image = Image.new("RGB", (OLED.SSD1351_WIDTH, OLED.SSD1351_HEIGHT), "BLACK")
    draw = ImageDraw.Draw(image)
    
    for x in range(OLED.SSD1351_HEIGHT-1, int((OLED.SSD1351_HEIGHT-1)/2), -6):
        draw.rectangle([(x, x), ((OLED.SSD1351_WIDTH-1) - x, (OLED.SSD1351_HEIGHT-1) - x)], fill = "BLUE", outline = "BLUE")
        draw.rectangle([(x, x), ((OLED.SSD1351_WIDTH-1) - x, (OLED.SSD1351_HEIGHT-1) - x)], fill = None, outline = "YELLOW")
    OLED.Display_Image(image)


def Test_Circles():
    image = Image.new("RGB", (OLED.SSD1351_WIDTH, OLED.SSD1351_HEIGHT), "BLACK")
    draw = ImageDraw.Draw(image)

    draw.ellipse([(0, 0), (OLED.SSD1351_WIDTH - 1, OLED.SSD1351_HEIGHT - 1)], fill = "WHITE", outline = "WHITE")
    OLED.Display_Image(image)
    OLED.Delay(3000)
    for r in range(0, int(OLED.SSD1351_WIDTH/2) + 4, 4):
        draw.ellipse([(r, r), ((OLED.SSD1351_WIDTH-1) - r, (OLED.SSD1351_HEIGHT-1) - r)], fill = None, outline = "WHITE")
    OLED.Display_Image(image)


def Test_Triangles():
    image = Image.new("RGB", (OLED.SSD1351_WIDTH, OLED.SSD1351_HEIGHT), "BLACK")
    draw = ImageDraw.Draw(image)
    
    for i in range(0, int(OLED.SSD1351_WIDTH/2), 4):
        draw.line([(i, OLED.SSD1351_HEIGHT - 1 - i), (OLED.SSD1351_WIDTH/2, i)], fill = (255 - i*4, i*4, 255 - i*4), width = 1)
        draw.line([(i, OLED.SSD1351_HEIGHT - 1 - i), (OLED.SSD1351_WIDTH - 1 - i, OLED.SSD1351_HEIGHT - 1 - i)], fill = (i*4, i*4 ,255 - i*4), width = 1)
        draw.line([(OLED.SSD1351_WIDTH - 1 - i, OLED.SSD1351_HEIGHT - 1 - i), (OLED.SSD1351_WIDTH/2, i)], fill = (i*4, 255 - i*4, i*4), width = 1)
        OLED.Display_Image(image)


def Display_Picture(File_Name):
    image = Image.new("RGB", (OLED.SSD1351_WIDTH, OLED.SSD1351_HEIGHT), "WHITE")
    draw = ImageDraw.Draw(image)
    image = Image.open(File_Name)
    # imageSize = imageClip.size
    # image.alpha_composite(imageClip, (0, 0))
    imageRGB = image.convert('RGB')
    OLED.Display_Image(image)

#----------------------MAIN-------------------------#
try:

    def main():
    
        #-------------OLED Init------------#
        OLED.Device_Init()
        OLED.Display_on()
    
        while True:
            # OLED.Clear_Screen()
            OLED.Fill_Color(OLED.BLACK)
            OLED.Delay(500)
            # OLED.Write_text(0xFFFF)
            # OLED.Delay(500)
            # Test_Circles()
            # Test_Lines()
            # Test_Rects()
            # Test_FillRects()
            # Test_Triangles()
            # Test_Text()
            # Test_HV_Lines()
            # Test_Pattern()
            Display_Picture("aux1.png")
            # OLED.Draw_FastVLine(20, 20, 100)
            # OLED.Draw_FastVLine(20, 20, 100)
            # OLED.Draw_Pixel(20, 20)
            # for i in range(50, 200):
            #    OLED.Draw_Pixel(0, i)
            # OLED.Delay(500)
            # OLED.Display_off()
            OLED.Delay(500)

        #-------------Draw Pictures------------#
        # OLED.Delay(8000)
        # print("hv lines")
        # Test_HV_Lines()
        # OLED.Delay(8000)
        # print("pattern")
        # Test_Pattern()
        # OLED.Delay(2000)
        # print("lines")
        # Test_Lines()
        # print("text")
        # Test_Text()
        # OLED.Delay(2000)
        # print("rects")
        # Test_Rects()
        # OLED.Delay(1000)
        # Test_FillRects() 
        # OLED.Delay(2000)
        # Test_Circles()
        # OLED.Delay(2000)
        # Test_Triangles()
        # OLED.Delay(2000)

        # while (True):
        #     Display_Picture("picture1.jpg")
        #     OLED.Delay(2000)
        #     Display_Picture("picture2.jpg")
        #     OLED.Delay(2000)
        #     Display_Picture("picture3.jpg")
        #     OLED.Delay(2000)


    if __name__ == '__main__':
        main()

except:
    print("\r\nEnd")
    OLED.Clear_Screen()
    GPIO.cleanup()


