def on_bluetooth_connected():
    basic.show_icon(IconNames.SMALL_SQUARE)
bluetooth.on_bluetooth_connected(on_bluetooth_connected)

def on_bluetooth_disconnected():
    global connected
    basic.show_icon(IconNames.SQUARE)
    connected = 1
bluetooth.on_bluetooth_disconnected(on_bluetooth_disconnected)

def on_button_pressed_a():
    if connected == 1:
        bluetooth.uart_write_string("Ciao da " + control.device_name())
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_uart_data_received():
    global uartDataReceived
    if connected == 1:
        uartDataReceived = bluetooth.uart_read_until(serial.delimiters(Delimiters.NEW_LINE))
        basic.clear_screen()
        basic.show_arrow(ArrowNames.EAST)
        basic.pause(2000)
        basic.show_string(uartDataReceived)
bluetooth.on_uart_data_received(serial.delimiters(Delimiters.NEW_LINE),
    on_uart_data_received)

uartDataReceived = ""
connected = 0
bluetooth.start_uart_service()
basic.show_string("UART")
basic.show_icon(IconNames.SQUARE)