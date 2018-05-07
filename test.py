# функция убирает из файлов коментарии и пустые строки


# with open('new_test_conf.txt') as f:
#     test = f.read()
#     print(test.count('\n') + 1)

import os
from os.path import isfile, isdir
import sys


OLDDIR = '/home/addmin/PycharmProjects/check_version/gate1.1'

NEWDIR = '/home/addmin/PycharmProjects/check_version/gate1.2'
# service_path = sys.argv[1]

# проверка является ли имя директорией и добавление директорий в список
def isdirs(path, path_dir):
    for i in path:
        if isdir(i):
            path_dir.append(i)

# сравнение содержимого директорий
def comparison(one, two, two_dir):
    if one.sort() == two.sort():
        with open('check.log', 'a', encoding='utf-8') as log:
            log.write('Содержимое директории {} PASS \n'.format(two_dir))
            return True
    else:
        with open('check.log', 'a', encoding='utf-8') as log:
            log.write('Содержимое директории {} FAIL \n'.format(two_dir))
            return False

def path_dir(dir):
    return '{}/{}'.format(NEWDIR, dir)

def len_dir(one, two):
    if len(one) > len(two):
        pass
    elif len(one) < len(two):
        pass
    else:
        return True


# основной цикл
def check_listdir():

    a = os.listdir(OLDDIR)
    b = os.listdir(NEWDIR)

    a_dir = []
    b_dir = []

    isdirs(a, a_dir)
    isdirs(b, b_dir)

    if comparison(a, b, NEWDIR):
        for i in range(len(a_dir)):
            comparison(os.listdir(a_dir[i]), os.listdir(b_dir[i]), path_dir(b_dir[i]))
    else:
        if le





check_listdir()