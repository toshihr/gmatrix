from itertools import chain


class Matrix:
    def __init__(self, data, dtype=float):
        '''Returns a matrix from a nested list, or from a string of data.

        Args:
          data (nested list or string): Same as numpy.matrix.
          dtype (int, float etc., optional): Data-type of the output matrix, defaults to float.

        '''
        self.dtype = dtype

        if isinstance(data, str):
            self.data = []
            for row in data.split(';'):
                self.data.append([dtype(v) for v in row.split(',')])
        elif isinstance(data, list):
            nrows, ncols = len(data), len(data[0])
            self.data = [[dtype(data[r][c]) for c in range(ncols)] for r in range(nrows)]
        else:
            raise ValueError('wrong structure')

    @property
    def shape(self):
        return (len(self.data), len(self.data[0]))

    @property
    def nrows(self):
        return self.shape[0]

    @property
    def ncols(self):
        return self.shape[1]

    def __repr__(self):
        _max = 0
        for line in self.data:
            for v in line:
                l = len(self.dtype.__str__(v))
                if l > _max:
                    _max = l
        f = '%%%ds' % (_max + 1)
        s = 'matrix([['
        for line in self.data:
            s = s + '\n'
            for v in line:
                s = s + (f % self.dtype.__str__(v))
        s = s + ']])'
        return s

    def __getitem__(self, ij):
        if isinstance(ij, tuple) and len(ij) == 2:
            (i, j) = ij
        else:
            raise ValueError('dimension mismatch')

        # convert i, j to slices
        def make_fullslice(s, len):
            if not isinstance(s, slice):
                return slice(s, s + 1, 1)
            else:
                return slice(s.start if s.start else 0,
                             s.stop if s.stop else len,
                             s.step if s.step else 1)
        i = make_fullslice(i, self.nrows)
        j = make_fullslice(j, self.ncols)

        # make return value
        res = []
        for r in range(i.start, i.stop, i.step):
            row = self.data[r][j]
            res.append(row)

        # return
        if (len(res), len(res[0])) == (1, 1):
            return res[0][0]
        else:
            return Matrix(data=res, dtype=self.dtype)

    def __setitem__(self, ij, value):
        if isinstance(ij, tuple) and len(ij) == 2:
            (i, j) = ij
        else:
            raise ValueError('dimension mismatch')

        assert isinstance(i, int) and isinstance(j, int), 'index should be integer.'

        self.data[i][j] = self.dtype(value)

    def __add__(self, other):
        self.__validate_structure(other)
        result = zeros(shape=(self.nrows, self.ncols), dtype=self.dtype)
        for i in range(self.nrows):
            for j in range(self.ncols):
                result[i, j] = self.dtype.__add__(self[i, j], other[i, j])
        return result

    def __sub__(self, other):
        self.__validate_structure(other)
        result = zeros(shape=(self.nrows, self.ncols), dtype=self.dtype)
        for i in range(self.nrows):
            for j in range(self.ncols):
                result[i, j] = self.dtype.__sub__(self[i, j], other[i, j])
        return result

    def __mul__(self, other):
        self.__validate_structure(other, inverse=True)
        result = zeros(shape=(self.nrows, other.ncols), dtype=self.dtype)
        for i in range(self.nrows):
            for j in range(other.ncols):
                iii = self[i, :].tolist()
                jjj = other[:, j].tolist()
                ii = list(chain.from_iterable(iii))
                jj = list(chain.from_iterable(jjj))
                result[i, j] = reduce(self.dtype.__add__, map(self.dtype.__mul__, ii, jj))
        if result.shape == (1, 1):
            return result[0, 0]
        else:
            return result

    # def __pow__(self, x):
    #     if not isinstance(x, int):
    #         raise TypeError('type mismatch')

    def tolist(self):
        '''Return the matrix as a nested list.'''
        return self.data

    def __validate_structure(self, other, dim_check=True, type_check=True, inverse=False):
        if dim_check and self.shape != (other.shape if not inverse else (other.ncols, other.nrows)):
            raise ValueError('dimension mismatch')
        if type_check and self.dtype != other.dtype:
            raise TypeError('type mismatch')


def zeros(shape, dtype=float):
    if len(shape) != 2:
        raise ValueError('dimension mismatch')
    return Matrix(data=[[dtype(0) for c in range(shape[1])] for r in range(shape[0])], dtype=dtype)
