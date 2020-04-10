class Sth:
    _fields = {
        'str': 'CharField',
        'int': 'IntegerField'
    }

    def __init__(self, parametreler_key, parametreler_value):
        self.all_key = parametreler_key
        self.all_value = parametreler_value

    def call(self):
        sthmore = self._fields[self.all_value[0]]
        print(sthmore)
