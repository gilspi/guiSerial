import serial
import queue

from src.data.config import serial_ports
import serial

from src.data.config import serial_ports

test_ports = [
    "/dev/tty23",
    "/dev/tty39",
    "/dev/tty54",
]

available_ports = serial_ports()
print(available_ports)

# test_ports.append(available_ports)
# print(test_ports)


def serial_receiver(_ser: serial.Serial, queue: queue.Queue):
    try:
        while True:
            data = _ser.read()
            queue.put(data)  # Помещаем полученные данные в очередь
    except serial.SerialException as e:
        print("Ошибка при подключении или чтении данных:", e)


def serial_transmitter(_ser: serial.Serial, queue: queue.Queue):
    while True:
        if not queue.empty():
            data = queue.get()  # Получаем данные
            print("Получены данные из порта:", data)


def serial_init(_ser: serial.Serial):
    data_queue = queue.Queue()

    # _serial_receiver = multiprocessing.Process(target=serial_receiver, args=(_ser, data_queue))
    # _serial_transmitter = multiprocessing.Process(target=serial_transmitter, args=(_ser, data_queue))
    # _serial_receiver.start()
    # _serial_transmitter.start()
    # _serial_receiver.join()
    # _serial_transmitter.join()


if __name__ == "__main__":
    port = 'COM1'  # Замените на нужный порт
    ser = serial.Serial(port, baudrate=115200, bytesize=8, timeout=0.1)
    serial_init(ser)
