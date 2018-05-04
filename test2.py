import os
import os.path

OLDDIR = '/home/addmin/PycharmProjects/check_version/gate1.1'
a = os.listdir(OLDDIR)
b = os.path.abspath(a[0])
s = os.path.split(b)
print('a = {}'.format(a))
print('b = {}'.format(b))
print('s = {}'.format(s))
print('s[0] = {}'.format(s[0]))