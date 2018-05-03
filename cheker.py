import os
import sys


# функция убирает из файлов коментарии и пустые строки
def prepare(namefile, newfile):
    f = open(namefile)
    fn = open(newfile, 'w', encoding='utf-8')
    while True:
        string = f.readline()
        if string == '':
            break
        elif string[0] == '#' or string == '\n':
            continue
        else:
            fn.write(string)
    f.close()
    fn.close()


def check(old, new):
    fold = open(old)
    fnew = open(new)
    log = open('check.log', 'w', encoding='utf-8')
    point = 1
    while True:
        old_str = fold.readline()
        new_str = fnew.readline()
        if old_str == '' or new_str == '':
            break
        elif old_str == new_str:
            pass
        else:
            log.write('{} {}'.format(point, new_str))
        point += 1

if __name__ == '__main__':
    prepare('test_conf.txt', 'oldcache.txt')
    prepare('new_test_conf.txt', 'newcache.txt')
    check('oldcache.txt', 'newcache.txt')
