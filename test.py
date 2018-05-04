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

def isdirs(path, path_dir):
    for i in path:
        if isdir(i):
            path_dir.append(i)

def comparison(one, two):
    if one.sort() == two.sort():
        with open('check.log', 'a', encoding='utf-8') as log:
            log.write('Содержимое директории {} PASS \n'.format(os.path.split(two[0])))
            return True
    else:
        with open('check.log', 'a', encoding='utf-8') as log:
            log.write('Содержимое директории {} FAIL \n'.format(os.path.normpath(two[0])))
            return False

def check_listdir():

    a = os.listdir(OLDDIR)
    b = os.listdir(NEWDIR)

    a_dir = []
    b_dir = []

    isdirs(a, a_dir)
    isdirs(b, b_dir)

    if comparison(a, b):
        for i in range(len(a_dir)):
            comparison(os.listdir(a_dir[i]), os.listdir(b_dir[i]))




check_listdir()