import pytest
import conversor as con

def test_mxn_a_usd():
    # Probamos que 2000 MXN a una tasa de 20.00 sean exactamente 100 USD
    assert con.mxn_a_usd(2000) == 100.0

def test_usd_a_mxn():
    # Probamos que 100 USD a una tasa de 20.00 sean exactamente 2000 MXN
    assert con.usd_a_mxn(100) == 2000.0
