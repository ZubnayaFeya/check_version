import os
import os.path


'''
def gen_etalon(service, dir):
    list_file = []
    dir = '{}{}'.format(dir, service)
    for i in os.listdir(dir):
        if i[0] == '.' or i[0] == '_':
            continue
        else:
            path_dir = '{}/{}'.format(dir, i)
            if os.path.isfile(path_dir):
                list_file.append(path_dir)
            elif os.path.isdir(path_dir):
                files = gen_etalon('', path_dir)
                for j in files:
                    list_file.append(j)
    return list_file


dir = '/home/addmin/PycharmProjects/check_version/'
service = 'gate1.1'
ful_dir = '{}{}/'.format(dir, service)
data = {}

dirs = gen_etalon(service, dir)
etalon = []
for i in dirs:
    if i.startswith(ful_dir):
        etalon.append(i.replace(ful_dir, ''))
    elif i.startswith(dir):
        etalon.append(i.replace(dir, ''))
    else:
        etalon.append(i)
data[service] = etalon

print(data)
'''

dir = '/home/addmin/PycharmProjects/check_version/'
service = 'gate1.1'
data = {}

#'''
def gen_etalon(service, dir):
    list_file = []
    ful_dir = '{}{}'.format(dir, service)
    for path, _, file in os.walk(ful_dir):
        if path == ful_dir:
            for s in file:
                list_file.append(s)
        else:
            print(path)
            print(min_path)
            for s in file:
                list_file.append('{}/{}'.format(path.replace(ful_dir, ''), s))
        return list_file

data[service] = gen_etalon(service, dir)
print(data)
'''
def gen_etalon(service, dir):
    list_file = []
    ful_dir = os.path.join(dir, service)
    for path, _, file in os.walk(ful_dir):
        for s in file:
            list_file.append(os.path.join(path.replace(ful_dir, ''), s))
    return list_file
data[service] = gen_etalon(service, dir)
print(data)
'''
'''
def gen_etalon(self):
  file_list = []
  for path, _, files in os.walk(self.etalon_path):
   for file in files:
    file_list.append(os.path.join(path.replace(self.etalon_path, ''), file))
  self.add_service(file_list)
'''