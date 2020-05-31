#from ..user_interface.settings import MEDIA_URL, MEDIA_ROOT


def print_ok(record: object) -> object:
    if record =='Daulet malenkii durachok':
        return 1
    elif record =='':
        return ''
    else:
        return 2


def read_file(filename):
    with open('{path}/{filename}'.format(path='media/media', filename=filename), 'r') as inp:
        text = inp.read()
    return text