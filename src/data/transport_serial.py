import time
import multiprocessing
from queue import Empty

import serial

from src.data.config import serial_ports


test_ports = [
    "/dev/tty23",
    "/dev/tty39",
    "/dev/tty54",
]

available_ports = serial_ports()

test_ports.append(available_ports)
print(test_ports)


def connect(queue: multiprocessing.Queue, port: str = '/dev/tty.wlan-debug', baudrate: int = 115200, bytesize: int = 8, timeout: float = 0.1):
    try:
        ser = serial.Serial(port=port, baudrate=baudrate, bytesize=bytesize, timeout=timeout)
        while True:
            data = ser.read()
            queue.put(data)  # Помещаем полученные данные в очередь
    except serial.SerialException as e:
        print("Ошибка при подключении или чтении данных:", e)


def update(queue: multiprocessing.Queue):
    while True:
        if not queue.empty():
            data = queue.get()  # Получаем данные
            print("Получены данные из порта:", data)


def main():
    port = "/dev/tty.wlan-debug"  # Замените на нужный порт
    data_queue = multiprocessing.Queue()

    connect_process = multiprocessing.Process(target=connect, args=(data_queue, port))
    gui_process = multiprocessing.Process(target=update, args=(data_queue,))
    connect_process.start()
    gui_process.start()
    connect_process.join()
    gui_process.join()


if __name__ == "__main__":
    main()
