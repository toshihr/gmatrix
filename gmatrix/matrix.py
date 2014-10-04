class Matrix:
    def __init__(self, data, dtype=float):

        self.dtype = dtype

        self.shape = (nrows, ncols) = (len(data), len(data[0]))

        self.data = [[dtype(data[r][c]) for c in range(ncols)] for r in range(nrows)]

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
        s = s + '\n' + 'shape=({0},{1})'.format(self.shape[0], self.shape[1])
        return s

    def __getitem__(self, ij):
        assert isinstance(ij, tuple) and len(ij) == 2, 'dimension mismatch'

        (i, j) = ij

        # convert i, j to slices
        def make_fullslice(s, len):
            if not isinstance(s, slice):
                return slice(s, s + 1, 1)
            else:
                return slice(s.start if s.start else 0,
                             s.stop if s.stop else len,
                             s.step if s.step else 1)
        i = make_fullslice(i, self.shape[0])
        j = make_fullslice(j, self.shape[1])

        # make return value
        res = []
        for r in range(i.start, i.stop, i.step):
            row = self.data[r][j]
            res.append(row)

        return Matrix(data=res, dtype=self.dtype)

    def __setitem__(self, ij, value):
        if isinstance(ij, tuple) and len(ij) == 2:
            (i, j) = ij
        else:
            raise ValueError('dimension mismatch')

        assert isinstance(i, int) and isinstance(j, int), 'index should be integer.'

        self.data[i][j] = self.dtype(value)

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

    def to_list(self):
        return self.data


def zeros(shape, dtype=float):
    return Matrix(data=[[dtype(0) for c in range(shape[1])] for r in range(shape[0])], dtype=dtype)
