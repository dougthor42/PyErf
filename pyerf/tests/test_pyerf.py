# -*- coding: utf-8 -*-
"""
Unit tests for ``pyerf.pyerf``.

Created by Douglas Thor on 2017-02-22 16:08:02 UTC.
"""
# ---------------------------------------------------------------------------
### Imports
# ---------------------------------------------------------------------------
# Standard Library
import decimal
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
def frange(x, y, jump):
    while x < y:
        yield float(x)
        x += decimal.Decimal(jump)


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


class TestErf(object):
    def test_erf_error(self):
        # values from
        # http://keisan.casio.com/exec/system/1180573449
        known_values = (
            (0.0001, 1.128379163334248694862E-4),
            (0.001, 0.001128378790969236379948),
            (0.01, 0.01128341555584961691591),
            (0.02, 0.02256457469184494422437),
            (0.05, 0.05637197779701662383127),
            (0.1, 0.1124629160182848922033),
            (0.3, 0.3286267594591274276389),
            (0.5, 0.5204998778130465376827),
            (0.7, 0.6778011938374184729756),
            (0.9, 0.796908212422832128519),
            (0.95, 0.8208908072732779419079),
            (0.98, 0.8342315043402078805143),
            (0.99, 0.8385080695553698035798),
            (0.999, 0.8422852702064969420084),
            (0.9999, 0.8426592780487594734183),
            (1, 0.8427007929497148693412),
            (2, 0.9953222650189527341621),
            (3, 0.9999779095030014145586),
            (4, 0.99999998458274209972),
            (-1, -0.8427007929497148693412),
            (-4, -0.99999998458274209972),
        )

        for x, expected in known_values:
            result = pyerf.erf(x)
            error = (expected - result) / result
            assert abs(error) < 1e-10

    def test_erf_extremes(self):
        assert pyerf.erf(0) == 0
        assert pyerf.erf(inf) == 1
        assert pyerf.erf(-inf) == -1

    @pytest.mark.skipif(not has_scipy, reason="Numpy or Scipy not installed")
    def test_erf_error_vs_scipy(self):
        x = np.arange(-4, 4, 0.0001)
        N = len(x)

        # Calculate the inverse of the error function
        y = np.zeros(N)
        for i in range(N):
            y[i] = pyerf.erf(x[i])

        assert np.allclose(y, sp.erf(x))


class TestErfc(object):
    def test_erfc_error(self):
        # values from
        # http://keisan.casio.com/exec/system/1180573449
        known_values = (
            (0.0001, 0.9998871620836665751305),
            (0.001, 0.9988716212090307636201),
            (0.01, 0.9887165844441503830841),
            (0.02, 0.9774354253081550557756),
            (0.05, 0.9436280222029833761687),
            (0.1, 0.8875370839817151077967),
            (0.3, 0.6713732405408725723611),
            (0.5, 0.4795001221869534623173),
            (0.7, 0.3221988061625815270244),
            (0.9, 0.203091787577167871481),
            (0.95, 0.1791091927267220580921),
            (0.98, 0.1657684956597921194857),
            (0.99, 0.1614919304446301964202),
            (0.999, 0.1577147297935030579916),
            (0.9999, 0.1573407219512405265817),
            (1, 0.1572992070502851306588),
            (2, 0.004677734981047265837931),
            (3, 2.20904969985854413728E-5),
            (4, 1.541725790028001885216E-8),
            (-1, 1.842700792949714869341),
            (-4, 1.99999998458274209972),
        )

        for x, expected in known_values:
            result = pyerf.erfc(x)
            error = (expected - result) / result
            assert abs(error) < 1e-10

    @pytest.mark.skipif(not has_scipy, reason="Numpy or Scipy not installed")
    def test_erfc_error_vs_scipy(self):
        x = np.arange(-4, 4, 0.0001)
        N = len(x)

        # Calculate the inverse of the error function
        y = np.zeros(N)
        for i in range(N):
            y[i] = pyerf.erfc(x[i])

        assert np.allclose(y, sp.erfc(x))


class TestErfErfc(object):
    def test_erf_erfc_complements(self):
        data = frange(-4, 4, 0.001)

        for x in data:
            assert round(pyerf.erf(x) + pyerf.erfc(x), 10) == 1

    def test_erfc_extremes(self):
        assert pyerf.erfc(0) == 1
        assert pyerf.erfc(inf) == 0
        assert pyerf.erfc(-inf) == 2
