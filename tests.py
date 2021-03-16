
import pytest
import alarm_mgmt as am


def test_hex_validation():
    assert am.validate_hex_color('zpiubs') == False


def test_validate_time():
    assert am.validate_time("30:99:00") == False

print(pytest)
    


