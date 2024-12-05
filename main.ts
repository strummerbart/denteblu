bluetooth.onBluetoothConnected(function () {
    basic.showIcon(IconNames.SmallSquare)
})
bluetooth.onBluetoothDisconnected(function () {
    basic.showIcon(IconNames.Square)
})
input.onButtonPressed(Button.A, function () {
    bluetooth.uartWriteString("Hi")
})
bluetooth.onUartDataReceived(serial.delimiters(Delimiters.NewLine), function () {
    basic.showIcon(IconNames.Heart)
})
bluetooth.startUartService()
basic.showString("Tested with http://bit.ly/serial-bluetooth")
basic.showIcon(IconNames.Square)
