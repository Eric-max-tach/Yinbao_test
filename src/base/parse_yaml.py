import yaml

def parse_yaml(file, section, key=None):
    """
    :param file: 文件名
    :param section: 段落名
    :param key: 键名，如果不传递key，则返回整个字典，如果传递key，则返回单个key
    :return:
    """

    with open(file, 'r', encoding="utf8") as f:
        data = yaml.load(f, Loader=yaml.FullLoader)
        if key:
            return data[section][key]
        else:
            return data[section]

# if __name__ == '__main__':
#     print(parse_yaml("my_yaml.yml", "yinbao"))