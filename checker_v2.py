import os.path
import os
import sys

import config


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

# функция считает количество строк в файле
def check_len(file):
    with open(file) as f:
        test = f.read()
        line = test.count('\n') + 1
        return line


def check(service, old, new, new_file_name):
    name_log = '{}.log'.format(service)
    log = open(name_log, 'a', encoding='utf-8')

    if check_len(old) == check_len(new):
        fold = open(old)
        fnew = open(new)
        log = open(name_log, 'a', encoding='utf-8')
        while True:
            old_str = fold.readline()
            new_str = fnew.readline()
            if old_str == '' or new_str == '':
                log.write('{} PASS\n'.format(new_file_name))
                fold.close()
                fnew.close()
                log.close()
                os.remove(old)
                os.remove(new)
                break
            elif old_str == new_str:
                pass
            else:
                log.write('{} FAIL\n'.format(new_file_name))
                fold.close()
                fnew.close()
                log.close()
                os.remove(old)
                os.remove(new)
                break
    else:
        log.write('{} FAIL\n'.format(new_file_name))
        log.close()


if __name__ == '__main__':
    service_name = sys.argv[1]
    files = 'config.{}'.format(service_name)
    print(files)
    old_path, old_file = os.path.split(files['old'][1])
    new_path, new_file = os.path.split(files['new'][1])
    prepare('{}/{}'.format(old_path, old_file), 'oldcache.txt')
    prepare('{}/{}'.format(new_path, new_file), 'newcache.txt')
    check(service_name, 'oldcache.txt', 'newcache.txt', new_file)

    old_path, old_file = os.path.split(config.risk['old'][1])