"""
Class that implements the fuzzer
"""

import logging
import re

import requests


class Fuzzer(object):
    """Does lovely fuzzing stuff"""
    def __init__(self, url_to_fuzz, fuzz_string_list):
        self.url_to_fuzz = url_to_fuzz
        self.fuzz_string_list = fuzz_string_list

        self.logger = logging.getLogger()
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s, %(name)-12s '
                                      '%(levelname)-8s %(message)s')
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
        # TODO: Change logging to an INI file:
        # https://docs.python.org/3/howto/logging.html
        self.logger.setLevel(logging.DEBUG)

    def check_everything_is_ready(self):
        """This checks that the url and fuzz_string_list are ok
        and that the URL is reachable.
        """
        if not self._check_url_properly_formed():
            self.logger.error('Fuzzer received badly formed URL')
            raise ValueError('URL not properly formed.')
        if not self._check_url_contains_substitution_point():
            self.logger.error('Fuzzer received URL without'
                              ' substitution point.')
            raise ValueError('URL does not contain a substitution point.')
        if not self._check_fuzz_string_list_is_ok():
            self.logger.error('Fuzzer received empty fuzz list.')
            raise ValueError('Fuzz list is empty.')
        try:
            self._check_url_is_reachable()
        except ConnectionError:
            self.logger.error('Fuzzer received an unreachable URL')
            raise ConnectionError('URL is unreachable.')
        self.logger.info('Fuzzer inputs successfully checked.')

    def _check_url_properly_formed(self):
        """Checks that the URL is actually a URL"""
        # https://stackoverflow.com/questions/6883049/regex-to-find-urls-in-string-in-python
        url_regex = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\)'
                               ',]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
                               self.url_to_fuzz)
        if len(url_regex) > 0:
            return True
        else:
            return False

    def _check_url_contains_substitution_point(self):
        """Checks that the URL has a {}"""
        if '{}' in self.url_to_fuzz:
            return True
        else:
            return False

    def _check_fuzz_string_list_is_ok(self):
        """Checks that the fuzz list has at least one entry"""
        if len(self.fuzz_string_list) > 0:
            return True
        else:
            return False

    def _check_url_is_reachable(self):
        """Makes sure the URL without the parameters is reachable"""
        url_without_parameters = self.url_to_fuzz[0:self.url_to_fuzz.find('?')]
        try:
            requests.get(url_without_parameters)
            return True
        except requests.exceptions.ConnectionError:
            raise ConnectionError('Failed to connect to URL.')
