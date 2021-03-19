class NotEqualLengthError(Exception):
    pass

class Table():
    '''This class expects the data to be in the 2 Dimention.
    Hence the length of your list / tuple will be the total
    rows or entries and the length of each record will be the
    length of columns.
    
    >>> Table( [[10, 20, 30],
                [40, 50, 60],
                [70, 80, 90]] )
    
    >>> +----+----+----+
        | 10 | 20 | 30 |
        | 40 | 50 | 60 |
        | 70 | 80 | 90 |
        +----+----+----+'''

    def __init__(self, tensor, headers= None):
        init_length = len(tensor[0])
        self._max_width = [ 0 for i in range(init_length) ]

        for entry in tensor:
            if init_length != len(entry):
                raise NotEqualLengthError("The length of all entries must be the same!")
            else:
                for i, elem in enumerate(entry):
                    if len(str(elem)) > self._max_width[i]:
                        self._max_width[i] = len(str(elem))
        
        if headers:
            if len(headers) != init_length:
                raise NotEqualLengthError("The header length is not matching with the data provided.")
            else:
                for i, header in enumerate(headers):
                    if self._max_width[i] < len(header): self._max_width[i] = len(header)

        self._rows = len(tensor)
        self._columns = len(tensor[0])
        self._tensor = tensor
        self._header = headers

    def _header_footer(self):
        params = {'sep':'', 'end':''}
        print(' + ', **params)
        for width in self._max_width:
            print('-' * (width + 2), **params)
            print(' + ', **params)
        print()
        
    def construct(self):
        params = {'sep':'', 'end':''}
        
        if self._header:
            self._header_footer()
            if self._header:
                print(' | ', **params)
                for i, header in enumerate(self._header):
                    print(header.center(self._max_width[i] + 2), **params)
                    print(' | ', **params)
                print()
        
        self._header_footer()
        
        for entry in self._tensor:
            print(' | ', **params)
            for i, elem in enumerate(entry):
                print(str(elem).rjust(self._max_width[i] + 2), **params)
                print(' | ', **params)
            print()

        self._header_footer()

    def __repr__(self):
        return f'''
        Rows x Cols: {self._rows} x {self._columns}
        Max_width: {self._max_width}'''


if __name__ == '__main__':
    print("Hey! Please use this module as 'Module' - Don't run it! ∞ Aayush Shah")
