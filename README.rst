gmatrix: Generic matrix module for python (WIP)
===================================================
.. image:: https://travis-ci.org/kerug/gmatrix.svg?branch=master
    :target: https://travis-ci.org/kerug/gmatrix

Intended to be used with Galois field.


Usage
=====
::

        >>> import gmatrix as gm
        >>> A = gm.Matrix('1,2;3,4', dtype=int)
        >>> A
        matrix([[
        1 2
        3 4]])
        >>> B = gm.zeros((2,2), dtype=int)
        >>> B[0,0] = 10
        >>> A + B
        matrix([[
        11  2
        3  4]])
        >>>

Install
=======
::

  $ python setup.py install
