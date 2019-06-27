BIN_START_SUBSTRING = '0b'
CHAR_ONE = '1'
CHAR_ZERO = '0'


def to_dec(bin_: str) -> int:

    if not bin_.startswith(BIN_START_SUBSTRING):
        raise TypeError('bin value must starts with `{}`'.format(BIN_START_SUBSTRING))

    chars = bin_[2:]

    if not chars:
        raise ValueError('No chars for converting')

    result = 0

    for ind, c in enumerate(reversed(chars)):
        if c == CHAR_ONE:
            to_add = 2 ** ind
            result += to_add
        elif c != CHAR_ZERO:
            raise ValueError('bin string must contain only `1` and `0` chars')

    return result
