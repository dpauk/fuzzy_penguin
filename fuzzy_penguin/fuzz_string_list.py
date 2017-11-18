"""
Class that loads and represents a list of strings that will be used for
fuzzing
"""

import os


DEFAULT_FUZZ_LIST = 'default_fuzz_list.txt'


class FuzzStringList(object):
    """Loads and holds a list of strings for fuzzing"""
    def __init__(self, fuzz_file=None):
        self.string_list = []
        self._set_fuzz_file(fuzz_file)

    def _set_fuzz_file(self, fuzz_file=None):
        """Sets the file to load to either the specifed file or the default
        file.  If the file is specifed, it also checks it exists"""
        if fuzz_file:
            if not os.path.isfile(fuzz_file):
                raise FileNotFoundError('Specified file not found.')
            else:
                if os.stat(fuzz_file).st_size == 0:
                    raise EOFError
                self._file_to_load = fuzz_file
        else:
            dir_path = os.path.dirname(os.path.realpath(__file__))
            default_file_path = os.path.join(dir_path, DEFAULT_FUZZ_LIST)

            # make sure the default file actually exists before trying to use
            if os.path.exists(default_file_path):
                self._file_to_load = os.path.join(dir_path, DEFAULT_FUZZ_LIST)
            else:
                raise FileNotFoundError('Default file not found.')

    def load_fuzz_file(self):
        """Loads the specified or default file into a list"""

        string_file = open(self._file_to_load, 'r')

        for line in string_file:
            self.string_list.append(line.strip())

        string_file.close()
