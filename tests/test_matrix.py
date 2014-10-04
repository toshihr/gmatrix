import gmatrix as gm


class TestMatrix:

    @classmethod
    def setup_class(clazz):
        pass

    @classmethod
    def teardown_class(clazz):
        pass

    def setup(self):
        self.m = gm.zeros((2, 3))
        assert self.m.shape == (2, 3)
        self.m[0, 0], self.m[0, 1], self.m[0, 2] = 0., 1., 2.
        self.m[1, 0], self.m[1, 1], self.m[1, 2] = 3., 4., 5.

    def teardown(self):
        pass

    def test_slice(self):
        assert self.m.shape == (2, 3)
        assert self.m[0, :].to_list() == [[0., 1., 2.]], 'row vector'
        assert self.m[:, 0].to_list() == [[0.], [3.]], 'column vector'
