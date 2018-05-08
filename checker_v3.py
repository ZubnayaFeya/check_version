import os.path
import os
import sys
import pickle
import hashlib
import datetime, time


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

def check(service, old, new, new_file_name, name_log):
    log = open(name_log, 'a', encoding='utf-8')
    if file_hash(old) == file_hash(new):
        log.write('PASS {}\n'.format(new_file_name))
    else:
        log.write('FAIL {}\n'.format(new_file_name))
        count = False
    log.close()

def file_hash(filename):
  h = hashlib.sha256()
  with open(filename, 'rb', buffering=0) as f:
    for b in iter(lambda : f.read(128*1024), b''):
      h.update(b)
  return h.hexdigest()

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

def check_installed(service_name, logname):
    with open('conf.txt', 'rb') as db:
        data = pickle.load(db)
    for file in data[service_name]:
        prepare('{}{}'.format(etalon_path, file), 'oldcache.txt')
        prepare('{}/{}'.format(install_path, file), 'newcache.txt')
        check(service_name, 'oldcache.txt', 'newcache.txt', file, logname)

        os.remove('oldcache.txt')
        os.remove('newcache.txt')

def rename_log(log):
    if count:
        os.rename(log, '[PASS]{}'.format(log))
    else:
        os.rename(log, '[FAIL]{}'.format(log))

if __name__ == '__main__':

    service_name = sys.argv[1]
    count = True
    etalon_path = '/home/addmin/PycharmProjects/check_version/gate1.1/'
    install_path = '/home/addmin/PycharmProjects/check_version/gate1.2/'
    log_path = '/home/tester/share/trade_system/testing/testresults/{}'.format(service_name)
    ts = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    log_name = '[{}]-[InstallTest].log'.format(ts)
    check_installed(service_name, '{}{}'.format(log_path, log_name))
    rename_log(log_name)