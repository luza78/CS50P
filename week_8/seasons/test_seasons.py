from seasons import validate_date
import pytest


def test_date():
    assert validate_date("2000-01-01") == ("2000", "01", "01")
    assert validate_date("1999-10-01") == ("1999", "10", "01")
    assert validate_date("1993-12-30") == ("1993", "12", "30")

    with pytest.raises(SystemExit):
        validate_date("20000-08-09")
    with pytest.raises(SystemExit):
        validate_date("1980-13-25")
    with pytest.raises(SystemExit):
        validate_date("2000-08-32")
    with pytest.raises(SystemExit):
        validate_date("2000-888-09")
    with pytest.raises(SystemExit):
        validate_date("2000-08-099")
