from client_test_cases import (
    DESTINATION_TEXT_1,
    DESTINATION_TEXT_2,
    DESTINATION_TEXT_3,
    DESTINATION_TEXT_4,
    SOURCE_TEXT_1,
    SOURCE_TEXT_2,
    SOURCE_TEXT_3,
    SOURCE_TEXT_4,
)

from solution_1 import source_to_destination_text


# TODO: добиться, чтобы все 4 теста проходили


def test_parse_source_text_1():
    assert source_to_destination_text(SOURCE_TEXT_1) == DESTINATION_TEXT_1


def test_parse_source_text_2():
    assert source_to_destination_text(SOURCE_TEXT_2) == DESTINATION_TEXT_2


def test_parse_source_text_3():
    assert source_to_destination_text(SOURCE_TEXT_3) == DESTINATION_TEXT_3


def test_parse_source_text_4():
    assert source_to_destination_text(SOURCE_TEXT_4) == DESTINATION_TEXT_4
