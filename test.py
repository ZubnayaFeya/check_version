# функция убирает из файлов коментарии и пустые строки


# with open('new_test_conf.txt') as f:
#     test = f.read()
#     print(test.count('\n') + 1)

import os
import sys


service_path = sys.argv[1]
