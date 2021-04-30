from gpiozero import LED

led = LED(21)


def turn_on():
    led.on()


def turn_off():
    led.off()


def switch():
    if led.is_active:
        turn_off()
    else:
        turn_on()