import json
import threading

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
print(f"Available ports: {available_ports}")

test_ports.append(available_ports)
print(f"Test ports: {test_ports}")

import struct


def packet_sender(data: dict):
    # Формат для упаковки данных: каждая строка представляется как null-терминированная строка (строка, заканчивающаяся нулем)
    fmt = ''
    byte_data = bytearray()
    for key, value in data.items():
        if isinstance(value, str):
            # Кодирование строки в байты и добавление нулевого байта в конце
            value_bytes = value.encode() + b'\x00'
            fmt += f'{len(value_bytes)}s'  # Длина строки в байтах
            byte_data += value_bytes
        elif isinstance(value, bool):
            # Преобразование булевого значения в байт
            byte_data += struct.pack('?', value)
            fmt += '?'
        elif isinstance(value, int):
            # Преобразование целого числа в байт
            byte_data += struct.pack('i', value)
            fmt += 'i'
        else:
            print(f"Unsupported data type for key '{key}': {type(value)}")

    # Добавление заголовка с длиной данных
    header = struct.pack('i', len(byte_data))
    packet = header + byte_data

    print(packet)


# Пример вызова функции с вашим словарем данных
d = {
    "plainTextEdit_2": "0",
    "plainTextEdit_3": "500",
    "plainTextEdit_7": "500",
    "plainTextEdit_8": "500",
    "plainTextEdit_9": "500",
    "plainTextEdit_12": "0",
    "plainTextEdit_13": "0",
    "plainTextEdit_15": "",
    "plainTextEdit_16": "",
    "plainTextEdit_17": "",
    "plainTextEdit_19": "",
    "plainTextEdit_20": "",
    "plainTextEdit_21": "",
    "plainTextEdit_22": "",
    "radioButton_19": "AUTO",
    "radioButton_22": "AUTO",
    "radioButton_27": "AUTO",
    "radioButton_32": "AUTO",
    "radioButton_37": "AUTO",
    "radioButton_42": "AUTO",
    "radioButton_47": "AUTO",
    "radioButton_52": "AUTO",
    "radioButton_57": "AUTO",
    "radioButton_62": "AUTO",
    "radioButton_65": "AUTO",
    "radioButton_68": "AUTO",
    "radioButton_71": "AUTO",
    "radioButton_74": "AUTO",
    "checkBox": False,
    "checkBox_2": False,
    "plainTextEdit": "0",
    "plainTextEdit_18": "",
    "checkBox_17": False,
    "checkBox_18": False,
    "checkBox_19": False,
    "checkBox_24": False,
    "checkBox_26": False,
    "checkBox_28": False,
    "checkBox_5": False,
    "checkBox_3": False,
    "checkBox_21": False,
    "checkBox_22": False,
    "checkBox_20": False,
    "checkBox_23": False,
    "checkBox_25": False,
    "checkBox_27": False,
    "checkBox_4": False
}


def serial_receiver(_ser: serial.Serial, queue: queue.Queue):
    try:
        while True:
            data = _ser.read()
            print(data)
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

    _serial_receiver = threading.Thread(target=serial_receiver, args=(_ser, data_queue)).start()  # запускаю поток
    _serial_transmitter = threading.Thread(target=serial_transmitter, args=(_ser, data_queue)).start()


if __name__ == "__main__":
    port = '/dev/tty.wlan-debug'  # Замените на нужный порт
    ser = serial.Serial(port, baudrate=115200, bytesize=8, timeout=0.1)
    serial_init(ser)
    packet_sender(d)
