CONST = 3

def connect(host, dbname, dbuser, passwd, port=5432):
    print(host, port, dbname, dbuser, passwd)

    if port==5432:
        return 1, 'ok'

    return 0, {2:[3,3]}, None, True
    print('asdasd')
    print('asdasd')
    print('asdasd')
    print('asdasd')

def test(*args, **kwargs):
    print(args)
    print(kwargs)

if __name__=='__main__':
    print('in module')
