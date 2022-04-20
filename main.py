def on_button_pressed_a():
    pins.digital_write_pin(DigitalPin.P13, 0)
    pins.digital_write_pin(DigitalPin.P14, 1)
    pins.digital_write_pin(DigitalPin.P15, 0)
    pins.digital_write_pin(DigitalPin.P16, 1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    pins.digital_write_pin(DigitalPin.P13, 0)
    pins.digital_write_pin(DigitalPin.P14, 0)
    pins.digital_write_pin(DigitalPin.P15, 0)
    pins.digital_write_pin(DigitalPin.P16, 0)
input.on_button_pressed(Button.B, on_button_pressed_b)

basic.show_leds("""
    . . # . .
        . . # . .
        . . # . .
        . . . . .
        . . # . .
""")
basic.pause(1000)
led.enable(False)

def on_forever():
    pass
basic.forever(on_forever)
