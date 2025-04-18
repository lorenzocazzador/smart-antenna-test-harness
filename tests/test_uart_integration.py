import serial
import time
import pytest

def uart_command_test(port):
    baudrate = 9600
    try:
        with serial.Serial(port, baudrate, timeout=2) as ser:
            ser.flush()
            ser.write(b"STATUS\n")
            time.sleep(0.5)
            response = ser.readline().decode().strip()
            assert "OK" in response or "INIT" in response
    except serial.SerialException as e:
        assert False, f"UART test failed: {e}"  # ← Lines 17–18 (will now be covered)

@pytest.mark.hardware
def test_uart_valid_port():
    uart_command_test('/tmp/ttyV0')  # Or your real working port

@pytest.mark.hardware
def test_uart_exception_trap():
    with pytest.raises(AssertionError):
        uart_command_test('/dev/INVALID_PORT')  # Triggers your try-except block
