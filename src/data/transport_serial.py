import threading
import queue
import json

import serial

from src.data.config import serial_ports


test_ports = [
    "/dev/tty23",
    "/dev/tty39",
    "/dev/tty54",
]

available_ports = serial_ports()
print(available_ports)

test_ports.append(available_ports)
print(test_ports)


# Пример вызова функции с вашим словарем данных
d = {
    "da28_control": "AUTO",
    "da23_control": "AUTO",
    "att_in_iq": "0",
    "hmc_freq_0": "500",
    "hmc_freq_1": "500",
    "hmc_freq_2": "500",
    "hmc_freq_3": "500",
    "cmp_th_low": "0",
    "cmp_th_high": "0",
    "da4_control": "AUTO",
    "da7_control": "AUTO",
    "da3_control": "AUTO",
    "da2_control": "AUTO",
    "en_iqmd": "AUTO",
    "en_iqdmd": "AUTO",
    "en_lo_33": "AUTO",
    "en_lo_5": "AUTO",
    "en_iqdmd_pwr": "AUTO",
    "en_lo_amp": "AUTO",
    "en_rx_amp": "AUTO",
    "hmc_enable": "AUTO",
    "ask_if_power_mode": "false",
    "force_update": "false",
    "att_in_com": "0",
}

tx_buff = bytearray(16)
print(tx_buff)
template_tx = None
with open('../parsed_data.json') as f:
    template_tx = json.load(f)["ask_rf_->_ask_if___(rx_section)"]

for field in template_tx:
    field_id = field["id"]
    value_d = d[field_id]
    params = field["params"]
    if value_d in params:
        binary_value = params[value_d]
    else:
        binary_value = int(value_d)
        if "RANGE" in params:
            _min = params["RANGE"]["min"]
            _max = params["RANGE"]["max"]
            if binary_value < _min:
                binary_value = _min
            if binary_value > _max:
                binary_value = _max

    # print(binary_value)
    size = field["size"]
    # print(size)
    offset_bytes = field["offset_bytes"]
    offset_bits = field["offset_bits"]

    if size <= 8:
        cell = tx_buff[offset_bytes]
        cell = cell | (binary_value << offset_bits)
        print(size, field["id"], tx_buff[offset_bytes], cell)
        tx_buff[offset_bytes] = cell
    elif size == 16:

        high = binary_value // 256
        low = binary_value % 256
        tx_buff[offset_bytes] = low
        tx_buff[offset_bytes+1] = high
print()
for byte_ in tx_buff:
    print(byte_, hex(byte_))

print(tx_buff.hex())
# cell = tx_queue[]
# data = tx_queue.get()  # Получаем данные


def serial_receiver(_ser: serial.Serial, tx_queue: queue.Queue):
    try:
        while True:
            data = _ser.read()
            print(data)
            tx_queue.put(data)  # Помещаем полученные данные в очередь
    except serial.SerialException as e:
        print("Ошибка при подключении или чтении данных:", e)


def serial_transmitter(_ser: serial.Serial, tx_queue: queue.Queue):
    # add tx_buff to tx_queue
    while True:
        if not tx_queue.empty():
            data = tx_queue.get()  # Получаем данные
            print("Получены данные из порта:", data)


def serial_init(_ser: serial.Serial):
    data_queue = queue.Queue()

    _serial_receiver = threading.Thread(target=serial_receiver, args=(_ser, data_queue)).start()
    _serial_transmitter = threading.Thread(target=serial_transmitter, args=(_ser, data_queue))


if __name__ == "__main__":
    port = '/dev/tty.wlan-debug'  # Замените на нужный порт
    ser = serial.Serial(available_ports[0], baudrate=115200, bytesize=8, timeout=0.1)
    serial_init(ser)
    # packet_sender(d)
