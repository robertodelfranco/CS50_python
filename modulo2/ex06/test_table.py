# import pytest
# from _pytest.capture import CaptureFixture
# from table import print_table, print_table_especific

# def test_print_table(capsys: CaptureFixture[str]) -> None:
#     print_table()
#     captured = capsys.readouterr()
#     expected_output = (
#         "Table of 0: 0 0 0 0 0 0 0 0 0 0 0\n"
#         "Table of 1: 0 1 2 3 4 5 6 7 8 9 10\n"
#         "Table of 2: 0 2 4 6 8 10 12 14 16 18 20\n"
#         "Table of 3: 0 3 6 9 12 15 18 21 24 27 30\n"
#         "Table of 4: 0 4 8 12 16 20 24 28 32 36 40\n"
#         "Table of 5: 0 5 10 15 20 25 30 35 40 45 50\n"
#         "Table of 6: 0 6 12 18 24 30 36 42 48 54 60\n"
#         "Table of 7: 0 7 14 21 28 35 42 49 56 63 70\n"
#         "Table of 8: 0 8 16 24 32 40 48 56 64 72 80\n"
#         "Table of 9: 0 9 18 27 36 45 54 63 72 81 90\n"
#     )
#     assert captured.out == expected_output

# def test_print_table_especific(capsys: CaptureFixture[str]) -> None:
#     print_table_especific(5)
#     captured = capsys.readouterr()
#     expected_output = "Table of 5: 5 10 15 20 25 30 35 40 45 50\n"
#     assert captured.out == expected_output
