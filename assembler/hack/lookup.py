"""
This module provides logic for the lookup table.
"""

class Lookup(object):
    """
    Dictionary with a pre-defined set of values based on hack specification.
    """

    def __init__(self):
        """
        Intializes lookup table with pre-defined values.
        """
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
        """
        Retrieves a value from the table.

        Parameters
        ----------
        name : str

        Returns
        -------
        value : int
        """
        return self._values.get(name)

    def add(self, name, value=None):
        """
        Adds a value to the lookup table.

        Parameters
        ----------
        name : str
        value : int, optional

        Returns
        -------
        value : int
        """
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
