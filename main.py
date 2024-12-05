def on_bluetooth_connected():
    basic.show_icon(IconNames.SMALL_SQUARE)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    basic.show_icon(IconNames.SQUARE)
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_button_pressed_a():
    bluetooth.uart_write_string("Hi")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_uart_data_received():
    basic.show_icon(IconNames.HEART)
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.NEW_LINE),
    on_uart_data_received)

bluetooth.start_uart_service()
basic.show_string("Tested with http://bit.ly/serial-bluetooth")
basic.show_icon(IconNames.SQUARE)