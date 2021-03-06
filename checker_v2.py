import os.path
import os
import sys
import pickle

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

# def dump_all_data():
#     data = {
#     'rts-gate': ['config.yaml', 'app.yaml', 'setup.yaml', 'links.yaml']
#     }
#     with open('conf.txt', 'wb') as db:
#         pickle.dump(data, db)


# def check_installed(service_name):
#     with open('conf.txt', 'rb') as db:
#         data = pickle.load(db)
#     for file in data[service_name]:
#         print('etalon file: {0} и {1}'.format(etalon_path, file))
#         print('check file: {0} и {1}'.format(install_path, file))



if __name__ == '__main__':

    def check_installed(service_name):
        with open('conf.txt', 'rb') as db:
            data = pickle.load(db)
        for file in data[service_name]:
            prepare('{}{}'.format(etalon_path, file), 'oldcache.txt')
            prepare('{}/{}'.format(install_path, file), 'newcache.txt')
            check(service_name, 'oldcache.txt', 'newcache.txt', file)

            print('etalon file: {0} и {1}'.format(etalon_path, file))
            print('check file: {0} и {1}'.format(install_path, file))

    service_name = sys.argv[1]
    etalon_path = '/home/addmin/PycharmProjects/check_version/gate1.1/'
    install_path = '/home/addmin/PycharmProjects/check_version/gate1.2/'

    check_installed(service_name)