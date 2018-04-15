class Lookup(object):
    def __init__(self):
        self._next_value = 16
        self._values = {
            'SP': 0,
            'LCL': 1,
            'ARG': 2,
            'THIS': 3,
            'THAT': 4,
            'SCREEN': 16384,
            'KBD': 24576
        }

        for i in range(15):
            self._values['R' + str(i)] = i

    def get(self, name):
        return self._values.get(name)

    def add(self, name, value=None):
        if value:
            self._values[name] = value
        else:
            self._values[name] = self._next_value
            self._next_value += 1

    def __repr__(self):
        result = ''
        for symbol, value in self._values.iteritems():
            result += '{}: {}\n'.format(symbol, value)

        return 'Lookup Table:\n{}'.format(result)
