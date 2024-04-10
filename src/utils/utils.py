import re
import json


def parse_file(path: str):
    data = {}

    with open(path, 'r') as file:
        content = file.read()

        sections = re.findall(r"## (.+?)\n(.+?)(?=\n\n## |\Z)", content, re.DOTALL)
        for section_name, section_content in sections:
            parameters = re.findall(r"\d+\. (.+?): (.+?)\n", section_content)
            section_data = []

            for param_name, description in parameters:
                match = re.search(r'(\d+) bits?', description)

                param_info = {
                    "name": param_name,
                    "id": param_name.lower().replace(" ", "_"),
                    "size": int(match.group(1)) if match is not None else None,
                    "offset_bytes": None,  # Пока не указано
                    "offset_bits": None,  # Пока не указано
                    "params": []
                }
                bit_values = re.findall(r'(\d+) - (.+?)\b', description)
                for bit_value, bit_description in bit_values:
                    param_info["params"].append({bit_value: bit_description})

                section_data.append(param_info)

            data[section_name.lower().replace(" ", "_")] = section_data

    return data


FILE_PATH = "../../ASK_IF_PROTO.MD"
parse_data = parse_file(FILE_PATH)
print(parse_data)

JSON_FILE_PATH = "../parsed_data.json"
with open(JSON_FILE_PATH, "w") as data:
    json.dump(parse_data, data, indent=4)

print("Данные успешно записаны в файл parse_data.json.")
