from board import SCL, SDA
import busio

#informaçes da API
#

# Import the SSD1306 module.
import adafruit_ssd1306


# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)

display = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c)

def displayText(msg,size = 1):
    display.fill(0) #apaga tudo
    nlines = len(msg)//20 + 1
    msg = msg + " "*(20-len(msg)%20)
    for line in range(nlines):
        display.text(msg[line*20:line*20 + 20], 0, 8*line, 'y', font_name='font5x8.bin', size=1)
        display.show()


#Exemples
display.fill(0) #apaga tudo
#display.show()
#pixel
# display.pixel(64, 16, 1)
# display.show()
#circulo
#display.circle(16,64,20,'r') # xc,yc,raio,cor
# display.show()
#display.text('Victor', 16, 64, 'y', font_name='font5x8.bin', size=1)
#display.show()
#display.image('imagem_mode2.jpeg')display.show()