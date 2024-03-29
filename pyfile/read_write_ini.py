"""
Product: read_write_ini.py
Author: @zihan
Date: 2019/12/09
Current ver: 0.0.0.1

History:
    v0.0.0.1    1. is_ini_exist：判断INI文件是否存在，返回值：True -- 存在，False -- 不存在
                2. get_sections：传入INI文件路径，获取INI文件的sections列表，返回值：list。
                                如果列表长度为0，则说明INI文件中没有section
                3. get_keys_ini：传入参数INI文件路径，section的名字，获取下面所有的键值。返回值：None/list。
                                如果返回值为None，说明section不存在
                4. get_value_ini：传入参数INI文件路径，section的名字，key的名字，获取对应的value值。返回值：None/list。
                                如果返回值为None，可能section错误，也可能key错误，看它的打印消息是什么
"""

import configparser
import os
# from print_color import *


def is_ini_exist(ini_path):
    ini_exist = os.path.exists(ini_path)
    if not ini_exist:
        return False
    return True


def is_section_exist(ini_path, section):
    sections = get_sections(ini_path)
    section_exist = False
    for section_data in sections:
        if section_data == section:
            section_exist = True
    return section_exist


def is_key_exist(ini_path, sec_name, key_name):
    options = get_keys(ini_path, sec_name)
    key_exist = False
    for option in options:
        if option.lower() == key_name.lower():
            key_exist = True
    return key_exist


def get_sections(ini_path):
    conf = configparser.ConfigParser()
    conf.read(ini_path)
    sections = conf.sections()
    return sections


def get_keys(ini_path, sec_name):
    conf = configparser.ConfigParser()
    conf.read(ini_path)
    options = conf.options(sec_name)
    return options


def get_value(ini_path, sec_name, key_name):
    conf = configparser.ConfigParser()
    conf.read(ini_path)
    value = conf.get(sec_name, key_name)
    return value


def get_key_value_dic(ini_path, sec_name):
    conf = configparser.ConfigParser()
    conf.read(ini_path)
    items = conf.items(sec_name)
    return items


def get_keys_ini(ini_path, section):
    keys = None
    if not is_section_exist(ini_path, section):
        # print_red("%s section is not exist in %s" % (section, ini_path))
        return keys
    else:
        keys = get_keys(ini_path, section)
        return keys


# 知道ini文件路径，section, key，得到value的值
def get_value_ini(ini_path, section, key):
    value = None
    if not is_ini_exist(ini_path):
        # print_red("ERROR!!! %s is not exsit" % ini_path)
        return value
    else:
        if not is_section_exist(ini_path, section):
            # print_red("ERROR!!! %s not exsit section %s" % (ini_path, section))
            return value
        else:
            if not is_key_exist(ini_path, section, key):
                # print_red("ERROR!!! In %s, %s section not exist %s key" %
                #           (ini_path, section, key))
                return value
            else:
                value = get_value(ini_path, section, key)
    return value


def get_key_value_dic_ini(ini_path, section):
    keys_values = None
    if not is_section_exist(ini_path, section):
        # print_red("%s section is not exist in %s" % (section, ini_path))
        return keys_values
    else:
        keys_values = get_key_value_dic(ini_path, section)
        return keys_values


if __name__ == "__main__":
    path_test = "./test.ini"

    # 获取ini文件中的section列表
    section_list = get_sections(path_test)
    if len(section_list) == 0:
        print("%s has no section" % path_test)
    else:
        print(section_list)

    # 获取APPLE section下面的key列表
    section_apple = "APPLE"
    key_list = get_keys_ini(path_test, section_apple)
    if key_list is None:
        print("Something wrong!!! Func: %s" % "get_keys_ini")
    else:
        print(key_list)

    # 获取APPLE section下面的键值对
    keys_values_list = get_key_value_dic_ini(path_test, section_apple)
    if keys_values_list is None:
        print("Something wrong!!! Func: %s" % "get_key_value_dic_ini")
    else:
        print(keys_values_list)

    # 获取APPLE section里面的num key的值
    key_num = "num"
    # 获取value值
    value_num = get_value_ini(path_test, section_apple, key_num)
    if value_num is None:
        print("Something wrong!!! Func: %s" % "get_value_ini")
    else:
        print(value_num)



