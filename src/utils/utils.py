import re
import json

from typing import Dict, Any


def search_data(string: str) -> dict:
    string = re.sub(r'\. #\d+ bit(?:s)?', '', string)  # remove substring .D bit/bits

    pattern = re.compile(r"(Lock detect|Detected value|force|val)")
    cleaned_text = pattern.sub("", string)
    arr_strings = cleaned_text.split(', ')

    data = []
    for string_ in arr_strings:
        if "Reserved" in string_:
            continue
        data.append(string_.strip().split(' - '))

    result = {}

    for item in data:
        key = item[1] if len(item) >= 2 else "RANGE"
        value = item[0].strip()
        if '-' in value:
            min_val, max_val = map(int, value.split('-'))
            value = {"min": min_val, "max": max_val}
        elif 'MHz' in key:
            max_val, units = key.split(" ")
            min_val, max_val = int(value), int(max_val)
            value = {"min": min_val, "max": max_val}
            key = "RANGE"
        else:
            value = int(value)

        result[key] = value

    if 'Off/On' in result:
        result['RANGE'] = result.pop('Off/On')
    if "OUT SW" in result:
        result['RANGE'] = result.pop("OUT SW")
    if "ATT" in result:
        result['RANGE'] = result.pop("ATT")
    if "AUTO Mode" in result:
        result['AUTO'] = result.pop("AUTO Mode")

    return result


def parse_file(path: str) -> dict:
    d = {}

    with open(path, 'r+') as file:
        content = file.read()

        sections = re.findall(r"## (.+?)\n(.+?)(?=\n\n## |\Z)", content, re.DOTALL)
        for section_name, section_content in sections:

            parameters = re.findall(r"(\d+\. .+?): (.+?)\n|Byte\s+(\d+)", section_content)
            section_data = []

            current_value, byte_, type_ = 0, None, None
            offset_bits, size = 0, 0

            for param_name, description, bytes_ in parameters:
                param_name = re.sub(r'\d+\.', '', param_name).strip()
                match = re.search(r'(\d+) bits?', description)

                if bytes_ != "":
                    prev = current_value
                    current_value = int(bytes_)

                    if prev != current_value:
                        offset_bits = 0

                if bytes_ == "":
                    byte_ = current_value

                    size = int(match.group(1)) if match is not None else 8
                    if size == 8 and byte_ in range(4, 13, 2) and param_name not in ['CMP_TH_LOW', 'VDET_RX_MAXPWR', 'ATT_IN_COM']:
                        offset_bits = 16

                    if size == 1:
                        type_ = 'checkbutton'
                    elif size in range(2, 5):
                        type_ = 'radiobutton'
                    else:
                        type_ = 'text'

                    param_info = {
                        "name": param_name,
                        "id": param_name.lower().replace(" ", "_"),
                        "size": size,
                        "offset_bytes": byte_,
                        "offset_bits": offset_bits,
                        "type": type_,
                        "params": [],
                    }

                    offset_bits += size
                    found_data = search_data(description)

                    param_info["params"] = found_data
                    section_data.append(param_info)

                d[section_name.lower().replace(" ", "_")] = section_data
    return d


def to_json(fpath: str, jpath: str, mode: str = "w+") -> Dict[str, Any]:
    parse_data = parse_file(fpath)

    json_data = json.dumps(parse_data, indent=4)

    with open(jpath, mode) as data:
        data.write(json_data)

    print("Данные успешно записаны в файл parse_data.json.")
    return json.loads(json_data)
