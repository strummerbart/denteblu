bluetooth.onBluetoothConnected(function on_bluetooth_connected() {
    basic.showIcon(IconNames.SmallSquare)
})
bluetooth.onBluetoothDisconnected(function on_bluetooth_disconnected() {
    
    basic.showIcon(IconNames.Square)
    connected = 1
})
input.onButtonPressed(Button.A, function on_button_pressed_a() {
    if (connected == 1) {
        bluetooth.uartWriteString("Ciao da " + control.deviceName())
        basic.clearScreen()
        basic.showIcon(IconNames.SmallSquare)
    }
    
})
bluetooth.onUartDataReceived(serial.delimiters(Delimiters.NewLine), function on_uart_data_received() {
    
    if (connected == 1) {
        uartDataReceived = bluetooth.uartReadUntil(serial.delimiters(Delimiters.NewLine))
        basic.clearScreen()
        basic.showArrow(ArrowNames.East)
        basic.pause(2000)
        basic.clearScreen()
        basic.showString(uartDataReceived)
    }
    
})
let uartDataReceived = ""
let connected = 0
bluetooth.startUartService()
basic.showString("UART")
basic.showIcon(IconNames.Square)
