import pytest

from fuzzy_penguin import fuzzer


@pytest.fixture
def fuzzer_object():
    return fuzzer.Fuzzer(None, None)


def test_check_url_properly_formed_good_url():
    url = 'https://www.google.co.uk/search?q=python&oq=python'
    fuzzer_object = fuzzer.Fuzzer(url, [])
    assert fuzzer_object._check_url_properly_formed() is True


def test_check_url_properly_formed_bad_url():
    url = 'hps://www.google.co.uk/search?q=python&oq=python'
    fuzzer_object = fuzzer.Fuzzer(url, [])
    assert fuzzer_object._check_url_properly_formed() is False


def test_check_url_contains_substitution_point_has_sub():
    url = 'http://www.example.com/?test={}'
    fuzzer_object = fuzzer.Fuzzer(url, [])
    assert fuzzer_object._check_url_contains_substitution_point() is True


def test_check_url_contains_substitution_point_not_has_sub():
    url = 'http://www.example.com/?test="hellocharlie!"'
    fuzzer_object = fuzzer.Fuzzer(url, [])
    assert fuzzer_object._check_url_contains_substitution_point() is False


def test_check_fuzz_string_list_is_ok_populated_list():
    fuzzer_object = fuzzer.Fuzzer('', ['one'])
    assert fuzzer_object._check_fuzz_string_list_is_ok() is True


def test_check_fuzz_string_list_is_ok_blank_list():
    fuzzer_object = fuzzer.Fuzzer('', [])
    assert fuzzer_object._check_fuzz_string_list_is_ok() is False


def test_check_url_is_reachable_good_url():
    url = 'https://www.google.co.uk/search?q=python&oq=python'
    fuzzer_object = fuzzer.Fuzzer(url, [])
    assert fuzzer_object._check_url_is_reachable() is True


def test_check_url_is_reachable_bad_url():
    url = 'http://www.uihjbn.com/'
    fuzzer_object = fuzzer.Fuzzer(url, [])
    with pytest.raises(ConnectionError):
        fuzzer_object._check_url_is_reachable()
