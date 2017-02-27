# -*- coding: utf-8 -*-
"""
Unit tests for ``pyerf.pyerf``.

Created by Douglas Thor on 2017-02-22 16:08:02 UTC.
"""
# ---------------------------------------------------------------------------
### Imports
# ---------------------------------------------------------------------------
# Standard Library
try:
    from math import inf
except ImportError:
    inf = float('inf')

# Third-Party
import pytest

has_scipy = True
try:
    import numpy as np
    import scipy.special as sp
except ImportError:
    has_scipy = False

# Package / Application
from .. import pyerf


# ---------------------------------------------------------------------------
### Constants
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
### Helper Functions
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
### Unit Tests
# ---------------------------------------------------------------------------
class TestErfInv(object):
    def test_erfinv_error(self):
        # values from
        # http://keisan.casio.com/has10/SpecExec.cgi?id=system/2006/1180573448
        known_values = (
            (0.0001, 8.862269277728946917512E-5),
            (0.001, 8.86227157466552104565E-4),
            (0.01, 0.0088625012809505979078),
            (0.02, 0.0177263950266780184822),
            (0.1, 0.08885599049425768701574),
            (0.3, 0.272462714726754355622),
            (0.5, 0.4769362762044698733814),
            (0.7, 0.7328690779592168522188),
            (0.9, 1.163087153676674086726),
            (0.95, 1.38590382434967794528),
            (0.99, 1.82138636771844967304),
            (0.999, 2.32675376551352467056),
            (0.9999, 2.7510639057120607961),
        )

        for x, expected in known_values:
            result = pyerf.erfinv(x)
            error = (expected - result) / result
            assert abs(error) < 1e-10

    @pytest.mark.skipif(not has_scipy, reason="Numpy or Scipy not installed")
    def test_erfinv_error_vs_scipy(self):
        x = np.arange(-1, 1, 0.0001)
        N = len(x)

        # Calculate the inverse of the error function
        y = np.zeros(N)
        for i in range(N):
            y[i] = pyerf.erfinv(x[i])

        assert np.allclose(y, sp.erfinv(x))

    def test_erfinv_extremes(self):
        assert pyerf.erfinv(1) == inf
        assert pyerf.erfinv(-1) == -inf
        assert pyerf.erfinv(0) == 0

    def test_erfinv_raises_error(self):
        values = (
            -2,
            2,
            -1.00000001,
            1.00000001,
            inf,
        )
        for val in values:
            with pytest.raises(ValueError):
                pyerf.erfinv(val)
