import re
import json


def search_data(string: str) -> dict:
    string = re.sub(r'\. #\d+ bit(?:s)?', '', string)  # remove substring .D bit/bits

    pattern = re.compile(r"(Lock detect|Detected value|force|val)")
    cleaned_text = pattern.sub("", string)
    arr_strings = cleaned_text.split(', ')

    data = []
    for string_ in arr_strings:
        data.append(string_.strip().split(' - '))

    result = {}

    for item in data:
        key = item[1] if len(item) >= 2 else "INT"
        value = item[0].strip()

        if '-' in value:
            min_val, max_val = map(int, value.split('-'))
            value = {"min": min_val, "max": max_val}
        elif 'MHz' in key:
            max_val, units = key.split(" ")
            min_val, max_value = int(value), int(max_val)
            value = {"min": min_val, "max": max_val, "units": units}
            key = "frequency"
        else:
            value = int(value)

        result[key] = value

    if 'Off/On' in result:
        result['State'] = result.pop('Off/On')

    return result


def parse_file(path: str) -> dict:
    data = {}

    with open(path, 'r') as file:
        content = file.read()

        sections = re.findall(r"## (.+?)\n(.+?)(?=\n\n## |\Z)", content, re.DOTALL)
        for section_name, section_content in sections:

            parameters = re.findall(r"(\d+\. .+?): (.+?)\n|Byte\s+(\d+)", section_content)
            section_data = []

            current_value, byte_, type_ = None, None, None

            for param_name, description, bytes_ in parameters:
                param_name = re.sub(r'\d+\.', '', param_name).strip()
                match = re.search(r'(\d+) bits?', description)

                if bytes_ != "":
                    current_value = int(bytes_)

                if bytes_ == "":
                    byte_ = current_value

                    size = int(match.group(1)) if match is not None else 0
                    offset_bits = size

                    param_info = {
                        "name": param_name,
                        "id": param_name.lower().replace(" ", "_"),
                        "size": size,
                        "offset_bytes": byte_,
                        "offset_bits": offset_bits,
                        "params": [],
                    }

                    found_data = search_data(description)

                    param_info["params"] = found_data
                    section_data.append(param_info)

                data[section_name.lower().replace(" ", "_")] = section_data
    return data


FILE_PATH = "../../ASK_IF_PROTO.MD"
parse_data = parse_file(FILE_PATH)

JSON_FILE_PATH = "../parsed_data.json"
with open(JSON_FILE_PATH, "w") as data:
    json.dump(parse_data, data, indent=4)

print("Данные успешно записаны в файл parse_data.json.")
