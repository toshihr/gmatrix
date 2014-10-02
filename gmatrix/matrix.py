class Matrix:
    def __init__(self, data, dtype=float):

        self.dtype = dtype

        self.nrows, self.ncols = len(data), len(data[0])

        self.data = [[dtype(data[r][c]) for c in range(self.ncols)] for r in range(self.nrows)]

    def __repr__(self):
        _max = 0
        for r in self.data:
            for c in r:
                l = len(self.dtype.__str__(c))
                if l > _max:
                    _max = l
        f = '%%%ds' % (_max + 1)
        s = 'matrix([['
        for r in self.data:
            s = s + '\n'
            for c in r:
                s = s + (f % self.dtype.__str__(c))
        s = s + ']])'
        s = s + '\n' + 'shape=({0},{1})'.format(self.nrows, self.ncols)
        return s

    def __getitem__(self, ij):
        if isinstance(ij, tuple) and len(ij) == 2:
            (i, j) = ij
        else:
            raise ValueError('dimension mismatch')

        if not isinstance(i, slice):
            i = slice(i, i + 1)
        if not isinstance(j, slice):
            j = slice(j, j + 1)

        res = []

        for r in range(i.start if i.start else 0,
                       i.stop if i.stop else self.nrows,
                       i.step if i.step else 1):
            row = self.data[r][j]
            res.append(row)

        return Matrix(data=res, dtype=self.dtype)

    def __mul__(self, other):
        if self.ncols != other.nrows:
            raise ValueError('dimension mismatch')
        if self.dtype != other.dtype:
            raise TypeError('type mismatch')

        result = zeros(shape=(self.nrows, self.ncols), dtype=self.dtype)

        for i in range(self.nrows):
            for j in range(other.ncols):
                result[i, j] = reduce(self.dtype.__add__,
                                      list(map(self.dtype.__mul__, self.data[i, j], other[:, j])))

        return result


def zeros(shape, dtype=float):
    return Matrix(data=[[dtype(0) for c in range(shape[1])] for r in range(shape[0])], dtype=dtype)
