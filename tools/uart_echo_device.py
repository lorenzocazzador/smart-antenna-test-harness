import serial
import time

port = '/tmp/ttyV1'  # Should match what pyserial test uses

with serial.Serial(port, 9600, timeout=1) as ser:
    print(f"[UART Simulator] Listening on {port}")
    while True:
        if ser.in_waiting > 0:
            cmd = ser.readline().decode().strip()
            print(f"[UART Simulator] Received: {cmd}")
            if cmd == "STATUS":
                ser.write(b"OK: Antenna Ready\n")
            elif cmd == "ALIGN":
                ser.write(b"OK: Alignment in Progress\n")
            else:
                ser.write(b"ERR: Unknown Command\n")
        time.sleep(0.1)
