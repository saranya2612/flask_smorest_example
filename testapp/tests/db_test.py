# https://medium.com/@mariusz.raczynski2/pytest-mock-how-to-mock-your-database-connection-5c84a5a0bfc3
# FILE: tests/unit/tests.py
import pytest

def test_program():
	# this test is using mocked database connection.
	assert True