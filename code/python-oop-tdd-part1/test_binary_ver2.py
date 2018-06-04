import pytest
from binary import Binary


def test_binary_init_int():
    binary = Binary(6)
    assert int(binary) == 6


def test_binary_init_negative():
    with pytest.raises(ValueError):
        binary = Binary(-4)


def test_binary_init_bitstr():
    binary = Binary('110')
    assert int(binary) == 6


def test_binary_init_binstr():
    binary = Binary('0b110')
    assert int(binary) == 6


def test_binary_init_hexstr():
    binary = Binary('0x6')
    assert int(binary) == 6


def test_binary_init_hex():
    binary = Binary(0x6)
    assert int(binary) == 6


def test_binary_init_intseq():
    binary = Binary([1, 1, 0])
    assert int(binary) == 6


def test_binary_init_strseq():
    binary = Binary(['1', '1', '0'])
    assert int(binary) == 6


# Conversions

def test_binary_eq():
    assert Binary(4) == Binary(4)


def test_binary_int():
    binary = Binary(6)
    assert int(binary) == 6


def test_binary_bin():
    binary = Binary(6)
    assert bin(binary) == '0b110'


def test_binary_str():
    binary = Binary(6)
    assert str(binary) == '110'


def test_binary_hex():
    binary = Binary(6)
    assert hex(binary) == '0x6'


# Basic operations

def test_binary_addition_int():
    assert Binary(4) + 1 == Binary(5)


def test_binary_addition_binary():
    assert Binary(4) + Binary(5) == Binary(9)


def test_binary_subtraction_int():
    assert Binary(4) - 1 == Binary(3)


def test_binary_subtraction_binary():
    assert Binary(5) - Binary(4) == Binary(1)


def test_binary_multiplication_int():
    assert Binary(5) * 4 == Binary(20)


def test_binary_multiplication_binary():
    assert Binary(5) * Binary(6) == Binary(30)


def test_binary_division_int():
    assert Binary(20) / 4 == Binary(5)


def test_binary_division_rem_int():
    assert Binary(21) / 4 == Binary(5)


def test_binary_division_binary():
    assert Binary(20) / Binary(5) == Binary(4)


def test_binary_division_rem_binary():
    assert Binary(21) / Binary(5) == Binary(4)


def test_binary_get_bit():
    binary = Binary('0101110001')
    assert binary[0] == '1'
    assert binary[5] == '1'


def test_binary_negative_index():
    assert Binary('0101110001')[-1] == '1'
    assert Binary('0101110001')[-2] == '0'


def test_binary_illegal_index():
    with pytest.raises(IndexError):
        Binary('01101010')[7]


def test_binary_inappropriate_type_index():
    with pytest.raises(TypeError):
        Binary('01101010')['key']


def test_binary_for_loop():
    assert [int(i) for i in Binary('01101010')] == [0, 1, 0, 1, 0, 1, 1]


def test_binary_not():
    assert ~Binary('1101') == Binary('10')


def test_binary_and():
    assert Binary('1101') & Binary('1') == Binary('1')


def test_binary_or():
    assert Binary('1101') | Binary('1') == Binary('1101')


def test_binary_xor():
    assert Binary('1101') ^ Binary('1') == Binary('1100')


def test_binary_shl():
    assert Binary('1101') << 1 == Binary('11010')


def test_binary_shl_pos():
    assert Binary('1101') << 5 == Binary('110100000')


def test_binary_shr():
    assert Binary('1101') >> 1 == Binary('110')


def test_binary_shr_pos():
    assert Binary('1101') >> 5 == Binary('0')
