import os
import os.path
import glob

OLDDIR = '/home/addmin/PycharmProjects/check_version/gate1.1/test_conf.txt'
# a = os.listdir(OLDDIR)
# b = os.path.abspath(a[0])
s = os.path.split(OLDDIR)

# print('a = {}'.format(a))
# print('b = {}'.format(b))
print('s = {}'.format(s))
# print('s[0] = {}'.format(s[0]))
#
# print(glob.glob(a[0]))
# tree = os.walk(a[0])
# for i in tree:
#     print(i)

a = '{}.log'.format('test')
print(*a)