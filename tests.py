"""Module contains unit test functions for hex & time validations.

Functions
---------
test_hex_validation()
    Tests for hex color validation
test_validate_time()
    Tests for time validation
"""

import pytest

import alarm_mgmt as am


def test_hex_validation():
    """Tests for hex color validation."""

    assert am.validate_hex_color('zpiubs') == False


def test_validate_time():
    """Tests for time validation."""

    assert am.validate_time("30:99:00") == False
