import gmatrix as gm


class TestMatrix:

    @classmethod
    def setup_class(clazz):
        pass

    @classmethod
    def teardown_class(clazz):
        pass

    def setup(self):
        self.A = gm.Matrix([[0, 1, 2], [3, 4, 5]], dtype=int)
        self.B = gm.Matrix([[6, 7, 8], [9, 10, 11]], dtype=int)
        self.C = gm.Matrix([[0, 1], [2, 3], [4, 5]], dtype=int)
        self.D = gm.Matrix([[0, 1], [2, 3]], dtype=int)

    def teardown(self):
        pass

    def test_init_by_string(self):
        m = gm.Matrix('0, 1, 2; 3, 4, 5', dtype=int)
        assert m.shape == (2, 3)

    def test_getitem(self):
        assert self.A[0, 0] == 0
        assert self.A[0, :].tolist() == [[0, 1, 2]]
        assert self.A[:, 0].tolist() == [[0], [3]]

    def test_setitem(self):
        m = gm.zeros((2, 3))
        assert m.shape == (2, 3)
        m[0, 0], m[0, 1], m[0, 2] = 0, 1, 2
        m[1, 0], m[1, 1], m[1, 2] = 3, 4, 5

    def test_slice(self):
        assert self.A.shape == (2, 3)
        assert self.A[0, :].tolist() == [[0, 1, 2]], 'row vector'
        assert self.A[:, 0].tolist() == [[0], [3]], 'column vector'

    def test_add(self):
        assert (self.A + self.B).tolist() == [[6, 8, 10], [12, 14, 16]]

    def test_sub(self):
        assert (self.A - self.B).tolist() == [[-6, -6, -6], [-6, -6, -6]]

    def test_multiply(self):
        assert (self.A * self.C).tolist() == [[10, 13], [28, 40]]

    # def test_power(self):
    #     assert (self.D ** 2).tolist() == [[2, 3], [6, 11]]
