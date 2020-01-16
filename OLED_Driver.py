# -*- coding:UTF-8 -*-
# Copyright (c) 2019 Xavier Carcelle
# See LICENSE for details.

import spidev
import RPi.GPIO as GPIO
import time

#SSD1362
SSD1351_WIDTH               = 256
SSD1351_HEIGHT              = 64
SSD1351_CMD_SETCOLUMN       = 0x15
SSD1351_CMD_SETROW          = 0x75

SSD1351_CMD_WRITERAM        = 0x5C
SSD1351_CMD_READRAM         = 0x5D

SSD1351_CMD_SETREMAP        = 0xA0
SSD1351_CMD_STARTLINE       = 0xA1
SSD1351_CMD_DISPLAYOFFSET   = 0xA2
SSD1351_CMD_VERTICAL_SCROLL_AREA   = 0xA3
SSD1351_CMD_DISPLAYALLOFF   = 0xA6
SSD1351_CMD_DISPLAYALLON    = 0xA5
SSD1351_CMD_NORMALDISPLAY   = 0xA4
SSD1351_CMD_INVERTDISPLAY   = 0xA7
SSD1351_CMD_MULTIPLEX_RATIO = 0xA8
SSD1351_CMD_FUNCTIONSELECT  = 0xAB
SSD1351_CMD_IREF_SELECTION  = 0xAD
SSD1351_CMD_DISPLAYOFF      = 0xAE
SSD1351_CMD_DISPLAYON       = 0xAF
SSD1351_CMD_PRECHARGE       = 0xB1
SSD1351_CMD_DISPLAYENHANCE  = 0xB2
SSD1351_CMD_CLOCKDIV        = 0xB3
SSD1351_CMD_SETVSL          = 0xB4
SSD1351_CMD_SETGPIO         = 0xB5
SSD1351_CMD_PRECHARGE2      = 0xB6
SSD1351_CMD_SETGRAY         = 0xB8
SSD1351_CMD_USELUT          = 0xB9
SSD1351_CMD_PRECHARGELEVEL  = 0xBC
SSD1351_CMD_VCOMH           = 0xBE

SSD1351_CMD_CONTRASTABC     = 0xC1
SSD1351_CMD_CONTRASTMASTER  = 0xC7
SSD1351_CMD_MUXRATIO        = 0xCA
SSD1351_CMD_COMMANDLOCK     = 0xFD
SSD1351_CMD_HORIZSCROLL     = 0x96
SSD1351_CMD_STOPSCROLL      = 0x9E
SSD1351_CMD_STARTSCROLL     = 0x9F

#color
BLACK   = 0x0000
BLUE    = 0x001F
RED     = 0xF800
GREEN   = 0x07E0
CYAN    = 0x07FF
MAGENTA = 0xF81F
YELLOW  = 0xFFE0
WHITE   = 0xFFFF
#buffer
color_byte = [0x00, 0x00]
color_fill_byte = [0x00, 0x00]*(SSD1351_WIDTH)

#GPIO Set
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
OLED_RST_PIN = 25
OLED_DC_PIN  = 24
OLED_CS_PIN  = 8
GPIO.setup(OLED_RST_PIN, GPIO.OUT)
GPIO.setup(OLED_DC_PIN, GPIO.OUT)
GPIO.setup(OLED_CS_PIN, GPIO.OUT)
#GPIO init
GPIO.setwarnings(False)
GPIO.setup(OLED_RST_PIN, GPIO.OUT)
GPIO.setup(OLED_DC_PIN, GPIO.OUT)
GPIO.setup(OLED_CS_PIN, GPIO.OUT)
#SPI init
SPI = spidev.SpiDev(0, 1)
SPI.max_speed_hz = 1000000
SPI.mode = 0b00

#################################################

def Delay(x):
    time.sleep(x / 1000.0)

def SPI_WriteByte(byte):
    SPI.writebytes(byte)

def OLED_RST(x):
    if x == 1:
        GPIO.output(OLED_RST_PIN,GPIO.HIGH)
    elif x == 0:
        GPIO.output(OLED_RST_PIN,GPIO.LOW)

def OLED_DC(x):
    if x == 1:
        GPIO.output(OLED_DC_PIN,GPIO.HIGH)
    elif x == 0:
        GPIO.output(OLED_DC_PIN,GPIO.LOW)

def OLED_CS(x):
    if x == 1:
        GPIO.output(OLED_CS_PIN,GPIO.HIGH)
    elif x == 0:
        GPIO.output(OLED_CS_PIN,GPIO.LOW)

def Write_Command(cmd):
    OLED_CS(0)
    OLED_DC(0)
    SPI_WriteByte([cmd])
    OLED_CS(1)

def Write_Data(dat):
    OLED_CS(0)
    OLED_DC(1)
    SPI_WriteByte([dat])
    OLED_CS(1)

def Write_Datas(data):
    OLED_CS(0)
    OLED_DC(1)
    SPI_WriteByte(data)
    OLED_CS(1)

def RAM_Address():
    Write_Command(0x15)
    # ?
    Write_Command(0x00)
    Write_Command(0x7f)
    # 
    Write_Command(0x75)
    # ?
    Write_Command(0x00)
    Write_Command(0x3f)

#################################################
def Invert(v):
    if(v):
        Write_Command(SSD1351_CMD_INVERTDISPLAY)
    else:
        Write_Command(SSD1351_CMD_NORMALDISPLAY)

def Clear_Screen():
    RAM_Address()
    Write_Command(0x5c)
    color_fill_byte = [0x00, 0x00]*SSD1351_WIDTH
    OLED_CS(0)
    OLED_DC(1)
    for i in range(0,SSD1351_HEIGHT):
        SPI_WriteByte(color_fill_byte)
    OLED_CS(1)

def Set_Color(color):
    color_byte[0] = (color >> 8) & 0xff
    color_byte[1] = color & 0xff

def Fill_Color(color):
    RAM_Address()
    Write_Command(0x5c)
    Set_Color(color)
    color_fill_byte = color_byte*SSD1351_WIDTH
    OLED_CS(0)
    OLED_DC(1)
    for i in range(0,SSD1351_HEIGHT):
        SPI_WriteByte(color_fill_byte)
    OLED_CS(1)

#################################################

def Set_Coordinate(x, y):
    if((x >= SSD1351_WIDTH) or (y >= SSD1351_HEIGHT)):
        return
    # Set x and y coordinate
    # column
    Write_Command(SSD1351_CMD_SETCOLUMN)
    Write_Command(x)
    Write_Command(SSD1351_WIDTH-1)
    # row
    Write_Command(SSD1351_CMD_SETROW)
    Write_Command(y)
    Write_Command(SSD1351_HEIGHT-1)
    Write_Command(SSD1351_CMD_WRITERAM)


def Set_Address(column, row):
    # RAM_Address()
    # Write_Command(0x5c)
    # column
    Write_Command(SSD1351_CMD_SETCOLUMN)
    # Write_Command(0x15)  
    Write_Data(column)  #X start 
    Write_Data(column)  #X end 
    # row
    Write_Command(SSD1351_CMD_SETROW)
    # Write_Command(0x75)
    Write_Data(row)     #Y start 
    # Write_Data(row+7)   #Y end 
    Write_Data(row+7)   #Y end 
    Write_Command(SSD1351_CMD_WRITERAM)

#################################################

def Write_text(dat):
    for i in range(0,8):
        if(dat & 0x01):
            Write_Datas(color_byte)
        else:
            Write_Datas([0x00,0x00])
        dat = dat >> 1


def Draw_Pixel(x, y):
    # Bounds check.
    if((x >= SSD1351_WIDTH) or (y >= SSD1351_HEIGHT)):
        return
    if((x < 0) or (y < 0)):
        return
    Set_Address(x, y)
    # transfer data
    Write_Datas(color_byte)


def Display_Image(Image):
    if(Image == None):
        return
    
    Set_Coordinate(0,0)
    buffer1 = Image.load()
    # for j in range(0, SSD1351_WIDTH):
    for j in range(0, 63):
        # for i in range(0, SSD1351_HEIGHT):
        for i in range(0, 31):
        # for i in range(0, 253):
            color_fill_byte[i*2] = ((buffer1[i,j][0] & 0xF8)|(buffer1[i,j][1] >> 5))
            color_fill_byte[i*2+1] = (((buffer1[i,j][1] << 3) & 0xE0)|(buffer1[i,j][2] >> 3))
            # print("before Write_Datas", j, i)
        Write_Datas(color_fill_byte)

#################################################

# Draw a horizontal line ignoring any screen rotation.
def Draw_FastHLine(x, y, length):
    # Bounds check
    if((x >= SSD1351_WIDTH) or (y >= SSD1351_HEIGHT)):
        return
    # X bounds check
    if((x+length) > SSD1351_WIDTH):
        length = SSD1351_WIDTH - x - 1
    if(length < 0):
        return
    # set location
    Write_Command(SSD1351_CMD_SETCOLUMN)
    Write_Data(x)
    Write_Data(x+length-1)
    Write_Command(SSD1351_CMD_SETROW)
    Write_Data(y)
    Write_Data(y)
    # fill!
    Write_Command(SSD1351_CMD_WRITERAM)
    
    for i in range(0,length):
       Write_Datas(color_byte)


def Draw_FastVLine(x, y, length):
    # Bounds check
    if((x >= SSD1351_WIDTH) or (y >= SSD1351_HEIGHT)):
        return
    # X bounds check
    if(y+length > SSD1351_HEIGHT):
        length = SSD1351_HEIGHT - y - 1
    if(length < 0):
        return
    # set location
    Write_Command(SSD1351_CMD_SETCOLUMN)
    Write_Data(x)
    Write_Data(x)
    Write_Command(SSD1351_CMD_SETROW)
    Write_Data(y)
    Write_Data(y+length-1)
    # fill!
    Write_Command(SSD1351_CMD_WRITERAM)

    for i in range(0,length):
        Write_Datas(color_byte)


#################################################

def Display_on():
    print("all on")
    Write_Command(0x15)    # Set Segment Remap
    Write_Command(0x00)    # Set Segment Remap
    Write_Command(0x7F)    # 4fSet Segment Remap
    Write_Command(0x75)    # Set Segment Remap
    Write_Command(0x00)    # Set Segment Remap
    Write_Command(0x3f)    # 1fSet Segment Remap
    for i in range(0, 64):
        for j in range(0,32):
            Write_Data(0xFF)
            Write_Data(0xFF)
            Write_Data(0xFF)
            Write_Data(0xFF)


def Display_off():
    print("all off")
    Write_Command(0x15)    # Set Segment Remap
    Write_Command(0x00)    # Set Segment Remap
    Write_Command(0x7F)    # 4fSet Segment Remap
    Write_Command(0x75)    # Set Segment Remap
    Write_Command(0x00)    # Set Segment Remap
    Write_Command(0x3f)    # 1fSet Segment Remap
    for i in range(0, 64):
        for j in range(0,32):
            Write_Data(0x00)
            Write_Data(0x00)
            Write_Data(0x00)
            Write_Data(0x00)

##################################################

def Device_Init():
    # OLED_CS(0)
    print("start init")

    Delay(300)
    OLED_RST(0)
    Delay(300)
    OLED_RST(1)
    Delay(300)

    # Delay(6000)

    OLED_CS(1)
    Delay(300)
    OLED_CS(0)
    Delay(300)
    
    Write_Command(0xae)	# display off

    Write_Command(0xab)	# Function select
    Write_Command(0x01)

    Write_Command(0xad)	# IREF selection
    Write_Command(0x9e)
    
    Write_Command(0x15)	# set column address
    Write_Command(0x00)    # column address start 00
    Write_Command(0x7f)    # column address end 95

    Write_Command(0x75)	# set row address
    Write_Command(0x00)    # row address start 00
    Write_Command(0x3f)    # row address end 63	
    
    Write_Command(0x81) # master contrast
    Write_Command(0x87)

    Write_Command(0xa0) # Remap
    Write_Command(0x53)
    
    Write_Command(0xa1) # Display start line
    Write_Command(0x00)

    Write_Command(0xa2) # Display offset
    Write_Command(0x00)

    # Set Display Mode
    # a4=normal a5=entire display a6=off a7=inverse display
    Write_Command(0xa4)	# Set display mode
    
    Write_Command(0xa8)	# set multiplex ratio
    Write_Command(0x3f)    # 
    
    Write_Command(0xb1)	# 
    Write_Command(0x11)
    
    Write_Command(0xb3)
    Write_Command(0xf0)
    
    Write_Command(0xb9)
    
    Write_Command(0xbc)
    Write_Command(0x04)
    
    Write_Command(0xbe)
    Write_Command(0x05)
    
    Clear_Screen()
    Write_Command(0xaf)

    print("end init")
