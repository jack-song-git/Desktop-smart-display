import machine
import ssd1306

i2c = machine.I2C(1, sda=machine.Pin(26), scl=machine.Pin(27), freq=400000)
print("I2C设备号：" + str(i2c.scan()[0]))
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

oled.text("Raspberry Pi", 0, 0)
oled.text("Pico", 0, 8)
oled.text("MicroPython", 0, 16)
oled.text("OLED(ssd1306)", 0, 24)
oled.show()
