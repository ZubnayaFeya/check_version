
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

# закрывает файлы
def close_file(*args):
    for i in args:
        i.close()

def check(service, old, new, new_file_name):
    name_log = '{}.log'.format(service)
    log = open(name_log, 'a', encoding='utf-8')
    fold = open(old)
    fnew = open(new)
    log = open(name_log, 'a', encoding='utf-8')
    while True:
        old_str = fold.readline()
        new_str = fnew.readline()
        if old_str == '' or new_str == '':
            log.write('PASS {}\n'.format(new_file_name))
            close_file(fold, fnew, log)
            os.remove(old)
            os.remove(new)
            break
        elif old_str == new_str:
            pass
        else:
            log.write('FAIL {}\n'.format(new_file_name))
            close_file(fold, fnew, log)
            os.remove(old)
            os.remove(new)
            break

if __name__ == '__main__':

    service_name = sys.argv[1]
    files = 'config.{}'.format(service_name)
    print(files)
    for i in range(len(eval(files)['old'])):
        old_path, old_file = os.path.split(eval(files)['old'][i+1])
        new_path, new_file = os.path.split(eval(files)['new'][i+1])
        prepare('{}/{}'.format(old_path, old_file), 'oldcache.txt')
        prepare('{}/{}'.format(new_path, new_file), 'newcache.txt')
        check(service_name, 'oldcache.txt', 'newcache.txt', new_file)
