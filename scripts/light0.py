from gpiozero import LED

led = LED(21)


def turn_on():
    led.on()


def turn_off():
    led.off()
