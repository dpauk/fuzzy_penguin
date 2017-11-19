import sys

from fuzzer import Fuzzer
from fuzz_string_list import FuzzStringList


def main():
    fuzz_strings = FuzzStringList()
    try:
        fuzz_strings.load_fuzz_file()
    except Exception as err:
        sys.stderr.write('ERROR: {}'.format(str(err)))
        return 1
    fuzzer = Fuzzer('', [])
    try:
        fuzzer.check_everything_is_ready()
    except Exception as err:
        sys.stderr.write('ERROR: {}'.format(str(err)))
    return 1


if __name__ == '__main__':
    sys.exit(main())
