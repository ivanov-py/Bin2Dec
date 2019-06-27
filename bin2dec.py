BIN_START_SUBSTRING = '0b'


def to_dec(bin_: str) -> int:

    _check_is_bin(bin_)

    chars = bin_[2:]

    _check_contain_only_1_and_0(chars)
    _check_has_chars(chars)

    result = 0

    for ind, c in enumerate(reversed(chars)):
        if c == '1':
            to_add = 2 ** ind
            result += to_add

    return result


def _check_is_bin(s: str):
    if not s.startswith(BIN_START_SUBSTRING):
        raise TypeError('bin value must starts with `{}`'.format(BIN_START_SUBSTRING))


def _check_contain_only_1_and_0(s: str):
    if not all(map(lambda x: x in ['0', '1'], s)):
        raise ValueError('bin string must contain only `1` and `0` chars')


def _check_has_chars(s: str):
    if not s:
        raise ValueError('No chars for converting')
