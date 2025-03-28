# import pytest
# from functions_everywhere import shrink, enlarge
# from _pytest.capture import CaptureFixture

# def test_shrink(capsys: CaptureFixture[str]) -> None:
# 	shrink('abcdefghijklmnopqrstuvwxyz')
# 	given = capsys.readouterr()
# 	expected = 'abcdefgh\n'
# 	assert expected == given.out

# def test_enlarge(capsys: CaptureFixture[str]) -> None:
# 	enlarge('a')
# 	given = capsys.readouterr()
# 	expected = 'aZZZZZZZ\n'
# 	assert given.out == expected
