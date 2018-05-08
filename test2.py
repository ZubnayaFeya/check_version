import pickle, sys

def dump_all_data():
    data = {
    'rts-gate': ['config.yaml', 'app.yaml', 'setup.yaml', 'links.yaml']
    }
    with open('conf.txt', 'wb') as db:
        pickle.dump(data, db)


def check_installed(service_name):
    with open('conf.txt', 'rb') as db:
        data = pickle.load(db)
    for file in data[service_name]:
        print('etalon file: {0} и {1}'.format(etalon_path, file))
        print('check file: {0} и {1}'.format(install_path, file))



if __name__ == '__main__':
    dump_all_data()
    etalon_path = '/home/addmin/PycharmProjects/check_version/gate1.1/'
    install_path = '/home/addmin/PycharmProjects/check_version/gate1.2/'
    check_installed(sys.argv[1])

import hashlib

def file_hash(filename):
  h = hashlib.sha256()
  with open(filename, 'rb', buffering=0) as f:
    for b in iter(lambda : f.read(128*1024), b''):
      h.update(b)
  return h.hexdigest()


#
# пример названия лога
# [FAIL][2018-05-08_15-12-40]-[Test_issues-162_5]-[Part_1].log
[FAIL][2018-05-08_15-12-40]-[InstallTest].log

'/home/tester/share/trade_system/testing/testresults/{0}/[{1}][{2}]-[InstallTest].log'.format(service_name, res, ts)

# import time, datetime
# ts = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')

# res - это совокупный результат всех проверок
# вместо self.name - имя проверяемого сервиса