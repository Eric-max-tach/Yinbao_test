import csv

def parse_csv(file, startline=1):
    """
    :param file: 文件名
    :param startline: 开始行数，默认值为1，即从文件的第二行开始读取，因为一般文件第一行为标题行
    :return:
    """

    mylist = []
    with open(file, "r", encoding="utf8") as f:
        data = csv.reader(f)
        for value in data:
            mylist.append(value)
        if startline == 1:
            del mylist[0]  # 删除标题行数据
        else:
            pass
        return mylist

# if __name__ == '__main__':
#     data = parse_csv("test_1_1_login.csv", 1)
#     print(*data)
#     print(data)