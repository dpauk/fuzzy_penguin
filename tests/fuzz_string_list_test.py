"""Tests for the fuzzy_penguin/fuzz_string_list.py file"""

import os

import pytest

from fuzzy_penguin import fuzz_string_list


@pytest.fixture
def fuzz_string_object():
    return fuzz_string_list.FuzzStringList()


def test_set_fuzz_file_no_fuzz_file_specified(fuzz_string_object):
    fuzz_string_object._set_fuzz_file()
    assert 'default_fuzz_list.txt' in fuzz_string_object._file_to_load


def test_set_fuzz_file_fuzz_file_specified_and_populated(fuzz_string_object):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fuzz_string_object._set_fuzz_file(os.path.join(dir_path,
                                                   'simple_fuzz_file.txt'))
    assert 'simple_fuzz_file.txt' in fuzz_string_object._file_to_load


def test_set_fuzz_file_fuzz_file_specified_but_empty(fuzz_string_object):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with pytest.raises(EOFError):
        fuzz_string_object._set_fuzz_file(os.path.join(dir_path,
                                                       'blank_fuzz_file.txt'))


def test_set_fuzz_file_file_does_not_exist(fuzz_string_object):
    with pytest.raises(FileNotFoundError):
        fuzz_string_object._set_fuzz_file('does_not_exist.txt')


def test_load_fuzz_file_correct_number_strings_loaded(fuzz_string_object):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    fuzz_string_object._set_fuzz_file(os.path.join(dir_path,
                                                   'simple_fuzz_file.txt'))
    fuzz_string_object.load_fuzz_file()
    assert len(fuzz_string_object.string_list) == 3
