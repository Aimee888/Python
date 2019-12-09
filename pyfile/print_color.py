"""
Product: print_color.py
Author: @zihan
Date: 2019/12/09
Current ver: 0.0.0.1

History:
    v0.0.0.1    1. 添加显示方式：高亮
                2. 添加背景色：黑色（black），红色（red），绿色（green），黄色（yellow），蓝色（blue），
                洋红（pink），青色（cyan），白色（white）
                3. 添加前景色：黑色（black），红色（red），绿色（green），黄色（yellow），蓝色（blue），
                洋红（pink），青色（cyan），白色（white）
                4. 使用方法：print_red_back_black(str) 使用黑色背景红色字体打印字符串str
"""
"""
数值表示的参数含义：
显示方式：0（默认值），1（高亮），22（非粗体），4（下划线），5（闪烁），25（非闪烁），7（反显），27（非反显）
前景色：30（黑色），31（红色），32（绿色），33（黄色），34（蓝色），35（洋红），36（青色），37（白色）
背景色：40（黑色），41（红色），42（绿色），43（黄色），44（蓝色），45（洋红），46（青色），47（白色）

常见开头格式：
\033[0m         默认字体正常显示，不高亮
\033[31;0m      红色字体正常显示
\033[1;32;40m   显示方式：高亮     字体前景色：绿色       背景色：黑色
\033[0,31;46m   显示方式：正常     字体前景色：红色       背景色：青色
\033[1;31m      显示方式：高亮     字体前景色：红色       背景色：无
"""
# 如果在pycharm里面显示颜色，就注释下面两句，如果在控制台输出显示颜色，就不注释下面两句
# from colorama import init
# init(autoreset=True)


# ******************************* 高亮 *******************************
# 黑背景
def print_black_back_black(str_black_back_black):
    print('\033[1;30;40m' + str_black_back_black + '\033[0m')  # <!--1-高亮显示 30-前景色黑色  40-背景色黑色-->


def print_red_back_black(str_red_back_black):
    print('\033[1;31;40m' + str_red_back_black + '\033[0m')  # <!--1-高亮显示 31-前景色红色  40-背景色黑色-->


def print_green_back_black(str_green_back_black):
    print('\033[1;32;40m' + str_green_back_black + '\033[0m')  # <!--1-高亮显示 32-前景色绿色  40-背景色黑色-->


def print_yellow_back_black(str_yellow_back_black):
    print('\033[1;33;40m' + str_yellow_back_black + '\033[0m')  # <!--1-高亮显示 33-前景色黄色  40-背景色黑色-->


def print_blue_back_black(str_blue_back_black):
    print('\033[1;34;40m' + str_blue_back_black + '\033[0m')  # <!--1-高亮显示 34-前景色蓝色  40-背景色黑色-->


def print_pink_back_black(str_pink_back_black):
    print('\033[1;35;40m' + str_pink_back_black + '\033[0m')  # <!--1-高亮显示 35-前景色洋红色  40-背景色黑色-->


def print_cyan_back_black(str_cyan_back_black):
    print('\033[1;36;40m' + str_cyan_back_black + '\033[0m')  # <!--1-高亮显示 36-前景色青色  40-背景色黑色-->


def print_white_back_black(str_white_back_black):
    print('\033[1;37;40m' + str_white_back_black + '\033[0m')  # <!--1-高亮显示 37-前景色白色 40-背景色黑色-->


# 红背景
def print_black_back_red(str_black_back_red):
    print('\033[1;30;41m' + str_black_back_red + '\033[0m')  # <!--1-高亮显示 30-前景色黑色  41-背景色红色-->


def print_red_back_red(str_red_back_red):
    print('\033[1;31;41m' + str_red_back_red + '\033[0m')  # <!--1-高亮显示 31-前景色红色  41-背景色红色-->


def print_green_back_red(str_green_back_red):
    print('\033[1;32;41m' + str_green_back_red + '\033[0m')  # <!--1-高亮显示 32-前景色绿色  41-背景色红色-->


def print_yellow_back_red(str_yellow_back_red):
    print('\033[1;33;41m' + str_yellow_back_red + '\033[0m')  # <!--1-高亮显示 33-前景色黄色  41-背景色红色-->


def print_blue_back_red(str_blue_back_red):
    print('\033[1;34;41m' + str_blue_back_red + '\033[0m')  # <!--1-高亮显示 34-前景色蓝色  41-背景色红色-->


def print_pink_back_red(str_pink_back_red):
    print('\033[1;35;41m' + str_pink_back_red + '\033[0m')  # <!--1-高亮显示 35-前景色洋红色  41-背景色红色-->


def print_cyan_back_red(str_cyan_back_red):
    print('\033[1;36;41m' + str_cyan_back_red + '\033[0m')  # <!--1-高亮显示 36-前景色青色  41-背景色红色-->


def print_white_back_red(str_white_back_red):
    print('\033[1;37;41m' + str_white_back_red + '\033[0m')  # <!--1-高亮显示 37-前景色白色 41-背景色红色-->


# 绿背景
def print_black_back_green(str_black_back_green):
    print('\033[1;30;42m' + str_black_back_green + '\033[0m')  # <!--1-高亮显示 30-前景色黑色  42-背景色绿色-->


def print_red_back_green(str_red_back_green):
    print('\033[1;31;42m' + str_red_back_green + '\033[0m')  # <!--1-高亮显示 31-前景色红色  42-背景色绿色-->


def print_green_back_green(str_green_back_green):
    print('\033[1;32;42m' + str_green_back_green + '\033[0m')  # <!--1-高亮显示 32-前景色绿色  42-背景色绿色-->


def print_yellow_back_green(str_yellow_back_green):
    print('\033[1;33;42m' + str_yellow_back_green + '\033[0m')  # <!--1-高亮显示 33-前景色黄色  42-背景色绿色-->


def print_blue_back_green(str_blue_back_green):
    print('\033[1;34;42m' + str_blue_back_green + '\033[0m')  # <!--1-高亮显示 34-前景色蓝色  42-背景色绿色-->


def print_pink_back_green(str_pink_back_green):
    print('\033[1;35;42m' + str_pink_back_green + '\033[0m')  # <!--1-高亮显示 35-前景色洋红色  42-背景色绿色-->


def print_cyan_back_green(str_cyan_back_green):
    print('\033[1;36;42m' + str_cyan_back_green + '\033[0m')  # <!--1-高亮显示 36-前景色青色  42-背景色绿色-->


def print_white_back_green(str_white_back_green):
    print('\033[1;37;42m' + str_white_back_green + '\033[0m')  # <!--1-高亮显示 37-前景色白色 42-背景色绿色-->


# 黄背景
def print_black_back_yellow(str_black_back_yellow):
    print('\033[1;30;43m' + str_black_back_yellow + '\033[0m')  # <!--1-高亮显示 30-前景色黑色  43-背景色黄色-->


def print_red_back_yellow(str_red_back_yellow):
    print('\033[1;31;43m' + str_red_back_yellow + '\033[0m')  # <!--1-高亮显示 31-前景色红色  43-背景色黄色-->


def print_green_back_yellow(str_green_back_yellow):
    print('\033[1;32;43m' + str_green_back_yellow + '\033[0m')  # <!--1-高亮显示 32-前景色绿色  43-背景色黄色-->


def print_yellow_back_yellow(str_yellow_back_yellow):
    print('\033[1;33;43m' + str_yellow_back_yellow + '\033[0m')  # <!--1-高亮显示 33-前景色黄色  43-背景色黄色-->


def print_blue_back_yellow(str_blue_back_yellow):
    print('\033[1;34;43m' + str_blue_back_yellow + '\033[0m')  # <!--1-高亮显示 34-前景色蓝色  43-背景色黄色-->


def print_pink_back_yellow(str_pink_back_yellow):
    print('\033[1;35;43m' + str_pink_back_yellow + '\033[0m')  # <!--1-高亮显示 35-前景色洋红色  43-背景色黄色-->


def print_cyan_back_yellow(str_cyan_back_yellow):
    print('\033[1;36;43m' + str_cyan_back_yellow + '\033[0m')  # <!--1-高亮显示 36-前景色青色  43-背景色黄色-->


def print_white_back_yellow(str_white_back_yellow):
    print('\033[1;37;43m' + str_white_back_yellow + '\033[0m')  # <!--1-高亮显示 37-前景色白色 43-背景色黄色-->


# 蓝背景
def print_black_back_blue(str_black_back_blue):
    print('\033[1;30;44m' + str_black_back_blue + '\033[0m')  # <!--1-高亮显示 30-前景色黑色  44-背景色蓝色-->


def print_red_back_blue(str_red_back_blue):
    print('\033[1;31;44m' + str_red_back_blue + '\033[0m')  # <!--1-高亮显示 31-前景色红色  44-背景色蓝色-->


def print_green_back_blue(str_green_back_blue):
    print('\033[1;32;44m' + str_green_back_blue + '\033[0m')  # <!--1-高亮显示 32-前景色绿色  44-背景色蓝色-->


def print_yellow_back_blue(str_yellow_back_blue):
    print('\033[1;33;44m' + str_yellow_back_blue + '\033[0m')  # <!--1-高亮显示 33-前景色黄色  44-背景色蓝色-->


def print_blue_back_blue(str_blue_back_blue):
    print('\033[1;34;44m' + str_blue_back_blue + '\033[0m')  # <!--1-高亮显示 34-前景色蓝色  44-背景色蓝色-->


def print_pink_back_blue(str_pink_back_blue):
    print('\033[1;35;44m' + str_pink_back_blue + '\033[0m')  # <!--1-高亮显示 35-前景色洋红色  44-背景色蓝色-->


def print_cyan_back_blue(str_cyan_back_blue):
    print('\033[1;36;44m' + str_cyan_back_blue + '\033[0m')  # <!--1-高亮显示 36-前景色青色  44-背景色蓝色-->


def print_white_back_blue(str_white_back_blue):
    print('\033[1;37;44m' + str_white_back_blue + '\033[0m')  # <!--1-高亮显示 37-前景色白色 44-背景色蓝色-->


# 洋红背景
def print_black_back_pink(str_black_back_pink):
    print('\033[1;30;45m' + str_black_back_pink + '\033[0m')  # <!--1-高亮显示 30-前景色黑色  45-背景色洋红色-->


def print_red_back_pink(str_red_back_pink):
    print('\033[1;31;45m' + str_red_back_pink + '\033[0m')  # <!--1-高亮显示 31-前景色红色  45-背景色洋红色-->


def print_green_back_pink(str_green_back_pink):
    print('\033[1;32;45m' + str_green_back_pink + '\033[0m')  # <!--1-高亮显示 32-前景色绿色  45-背景色洋红色-->


def print_yellow_back_pink(str_yellow_back_pink):
    print('\033[1;33;45m' + str_yellow_back_pink + '\033[0m')  # <!--1-高亮显示 33-前景色黄色  45-背景色洋红色-->


def print_blue_back_pink(str_blue_back_pink):
    print('\033[1;34;45m' + str_blue_back_pink + '\033[0m')  # <!--1-高亮显示 34-前景色蓝色  45-背景色洋红色-->


def print_pink_back_pink(str_pink_back_pink):
    print('\033[1;35;45m' + str_pink_back_pink + '\033[0m')  # <!--1-高亮显示 35-前景色洋红色  45-背景色洋红色-->


def print_cyan_back_pink(str_cyan_back_pink):
    print('\033[1;36;45m' + str_cyan_back_pink + '\033[0m')  # <!--1-高亮显示 36-前景色青色  45-背景色洋红色-->


def print_white_back_pink(str_white_back_pink):
    print('\033[1;37;45m' + str_white_back_pink + '\033[0m')  # <!--1-高亮显示 37-前景色白色 45-背景色洋红色-->


# 青背景
def print_black_back_cyan(str_black_back_cyan):
    print('\033[1;30;46m' + str_black_back_cyan + '\033[0m')  # <!--1-高亮显示 30-前景色黑色  46-背景色青色-->


def print_red_back_cyan(str_red_back_cyan):
    print('\033[1;31;46m' + str_red_back_cyan + '\033[0m')  # <!--1-高亮显示 31-前景色红色  46-背景色青色-->


def print_green_back_cyan(str_green_back_cyan):
    print('\033[1;32;46m' + str_green_back_cyan + '\033[0m')  # <!--1-高亮显示 32-前景色绿色  46-背景色青色-->


def print_yellow_back_cyan(str_yellow_back_cyan):
    print('\033[1;33;46m' + str_yellow_back_cyan + '\033[0m')  # <!--1-高亮显示 33-前景色黄色  46-背景色青色-->


def print_blue_back_cyan(str_blue_back_cyan):
    print('\033[1;34;46m' + str_blue_back_cyan + '\033[0m')  # <!--1-高亮显示 34-前景色蓝色  46-背景色青色-->


def print_pink_back_cyan(str_pink_back_cyan):
    print('\033[1;35;46m' + str_pink_back_cyan + '\033[0m')  # <!--1-高亮显示 35-前景色洋红色  46-背景色青色-->


def print_cyan_back_cyan(str_cyan_back_cyan):
    print('\033[1;36;46m' + str_cyan_back_cyan + '\033[0m')  # <!--1-高亮显示 36-前景色青色  46-背景色青色-->


def print_white_back_cyan(str_white_back_cyan):
    print('\033[1;37;46m' + str_white_back_cyan + '\033[0m')  # <!--1-高亮显示 37-前景色白色 46-背景色青色-->


# 白背景
def print_black_back_white(str_black_back_white):
    print('\033[1;30;47m' + str_black_back_white + '\033[0m')  # <!--1-高亮显示 30-前景色黑色  47-背景色白色-->


def print_red_back_white(str_red_back_white):
    print('\033[1;31;47m' + str_red_back_white + '\033[0m')  # <!--1-高亮显示 31-前景色红色  47-背景色白色-->


def print_green_back_white(str_green_back_white):
    print('\033[1;32;47m' + str_green_back_white + '\033[0m')  # <!--1-高亮显示 32-前景色绿色  47-背景色白色-->


def print_yellow_back_white(str_yellow_back_white):
    print('\033[1;33;47m' + str_yellow_back_white + '\033[0m')  # <!--1-高亮显示 33-前景色黄色  47-背景色白色-->


def print_blue_back_white(str_blue_back_white):
    print('\033[1;34;47m' + str_blue_back_white + '\033[0m')  # <!--1-高亮显示 34-前景色蓝色  47-背景色白色-->


def print_pink_back_white(str_pink_back_white):
    print('\033[1;35;47m' + str_pink_back_white + '\033[0m')  # <!--1-高亮显示 35-前景色洋红色  47-背景色白色-->


def print_cyan_back_white(str_cyan_back_white):
    print('\033[1;36;47m' + str_cyan_back_white + '\033[0m')  # <!--1-高亮显示 36-前景色青色  47-背景色白色-->


def print_white_back_white(str_white_back_white):
    print('\033[1;37;47m' + str_white_back_white + '\033[0m')  # <!--1-高亮显示 37-前景色白色 47-背景色白色-->


def print_black(str_black):
    print('\033[1;31m' + str_black + '\033[0m')  # <!--1-高亮显示 31-前景色黑色-->


def print_red(str_red):
    print('\033[1;31m' + str_red + '\033[0m')  # <!--1-高亮显示 31-前景色红色-->


def print_green(str_green):
    print('\033[1;32m' + str_green + '\033[0m')  # <!--1-高亮显示 32-前景色绿色-->


def print_yellow(str_yellow):
    print('\033[1;33m' + str_yellow + '\033[0m')  # <!--1-高亮显示 33-前景色黄色-->


def print_blue(str_blue):
    print('\033[1;34m' + str_blue + '\033[0m')  # <!--1-高亮显示 34-前景色蓝色-->


def print_pink(str_pink):
    print('\033[1;35m' + str_pink + '\033[0m')  # <!--1-高亮显示 35-前景色洋红色-->


def print_cyan(str_cyan):
    print('\033[1;36m' + str_cyan + '\033[0m')  # <!--1-高亮显示 36-前景色青色-->


def print_white(str_white):
    print('\033[1;37m' + str_white + '\033[0m')  # <!--1-高亮显示 37-前景色白色-->


if __name__ == "__main__":
    # 黑背景
    print_black_back_black("黑字黑背景")
    print_red_back_black("红字黑背景")
    print_green_back_black("绿字黑背景")
    print_yellow_back_black("黄字黑背景")
    print_blue_back_black("蓝字黑背景")
    print_pink_back_black("洋红字黑背景")
    print_cyan_back_black("青字黑背景")
    print_white_back_black("白字黑背景")

    # 红背景
    print_black_back_red("黑字红背景")
    print_red_back_red("红字红背景")
    print_green_back_red("绿字红背景")
    print_yellow_back_red("黄字红背景")
    print_blue_back_red("蓝字红背景")
    print_pink_back_red("洋红字红背景")
    print_cyan_back_red("青字红背景")
    print_white_back_red("白字红背景")

    # 绿背景
    print_black_back_green("黑字绿背景")
    print_red_back_green("红字绿背景")
    print_green_back_green("绿字绿背景")
    print_yellow_back_green("黄字绿背景")
    print_blue_back_green("蓝字绿背景")
    print_pink_back_green("洋红字绿背景")
    print_cyan_back_green("青字绿背景")
    print_white_back_green("白字绿背景")

    # 黄背景
    print_black_back_yellow("黑字黄背景")
    print_red_back_yellow("红字黄背景")
    print_green_back_yellow("绿字黄背景")
    print_yellow_back_yellow("黄字黄背景")
    print_blue_back_yellow("蓝字黄背景")
    print_pink_back_yellow("洋红字黄背景")
    print_cyan_back_yellow("青字黄背景")
    print_white_back_yellow("白字黄背景")

    # 蓝背景
    print_black_back_blue("黑字蓝背景")
    print_red_back_blue("红字蓝背景")
    print_green_back_blue("绿字蓝背景")
    print_yellow_back_blue("黄字蓝背景")
    print_blue_back_blue("蓝字蓝背景")
    print_pink_back_blue("洋红字蓝背景")
    print_cyan_back_blue("青字蓝背景")
    print_white_back_blue("白字蓝背景")

    # 洋红背景
    print_black_back_pink("黑字洋红背景")
    print_red_back_pink("红字洋红背景")
    print_green_back_pink("绿字洋红背景")
    print_yellow_back_pink("黄字洋红背景")
    print_blue_back_pink("蓝字洋红背景")
    print_pink_back_pink("洋红字洋红背景")
    print_cyan_back_pink("青字洋红背景")
    print_white_back_pink("白字洋红背景")

    # 青背景
    print_black_back_cyan("黑字青背景")
    print_red_back_cyan("红字青背景")
    print_green_back_cyan("绿字青背景")
    print_yellow_back_cyan("黄字青背景")
    print_blue_back_cyan("蓝字青背景")
    print_pink_back_cyan("洋红字青背景")
    print_cyan_back_cyan("青字青背景")
    print_white_back_cyan("白字青背景")

    # 白背景
    print_black_back_white("黑字白背景")
    print_red_back_white("红字白背景")
    print_green_back_white("绿字白背景")
    print_yellow_back_white("黄字白背景")
    print_blue_back_white("蓝字白背景")
    print_pink_back_white("洋红字白背景")
    print_cyan_back_white("青字白背景")
    print_white_back_white("白字白背景")

    # 无背景
    print_black("黑字")
    print_red("红字")
    print_green("绿字")
    print_yellow("黄字")
    print_blue("蓝字")
    print_pink("洋红字")
    print_cyan("青字")
    print_white("白字")
