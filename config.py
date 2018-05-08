import pickle, os, os.path

ce = {
    'old': {
        1: '/home/addmin/PycharmProjects/check_version/gate1.1/test_conf.txt',
        2: '/home/addmin/PycharmProjects/check_version/gate1.1/test_dir/config.yaml',
        3: '/home/addmin/PycharmProjects/check_version/gate1.1/test_dir/links.yaml'
            },
    'new': {
        1: '/home/addmin/PycharmProjects/check_version/gate1.2/test_conf.txt',
        2: '/home/addmin/PycharmProjects/check_version/gate1.2/test_dir/config.yaml',
        3: '/home/addmin/PycharmProjects/check_version/gate1.2/test_dir/links.yaml'
            }
    }
risk = {
    'old': {
        1: '/home/addmin/PycharmProjects/check_version/gate1.1/app.yaml',
        2: '/home/addmin/PycharmProjects/check_version/gate1.1/config.yaml',
        3: '/home/addmin/PycharmProjects/check_version/gate1.1/links.yaml',
        4: '/home/addmin/PycharmProjects/check_version/gate1.1/setup.yaml'
            },
    'new': {
        1: '/home/addmin/PycharmProjects/check_version/gate1.1/app.yaml',
        2: '/home/addmin/PycharmProjects/check_version/gate1.1/config.yaml',
        3: '/home/addmin/PycharmProjects/check_version/gate1.1/links.yaml',
        4: '/home/addmin/PycharmProjects/check_version/gate1.1/setup.yaml'
            }
    }
logic = {
    'old': {
        1: '/home/addmin/PycharmProjects/check_version/gate1.1/test_conf.txt',
        2: '/home/addmin/PycharmProjects/check_version/gate1.1/test_dir/config.yaml',
        3: '/home/addmin/PycharmProjects/check_version/gate1.1/test_dir/links.yaml'
            },
    'new': {
        1: '/home/addmin/PycharmProjects/check_version/gate1.2/test_conf.txt',
        2: '/home/addmin/PycharmProjects/check_version/gate1.2/test_dir/config.yaml',
        3: '/home/addmin/PycharmProjects/check_version/gate1.2/test_dir/links.yaml'
            }
    }

'''
with open('conf.txt', 'wb') as db:
    pickle.dump(risk, db)


old /home/tester/old_configs
new /etc/rts

os.listdir


'''