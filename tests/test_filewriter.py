import os
from unittest import mock

from filewriter import get_filename, read_data, parse_data, Reverse, Writer, Reader


def test_get_filename():
    filename = get_filename('test')
    assert filename == 'test.log'

    filename = get_filename('test', 'txt')
    assert filename == 'test.txt'


def test_read_data():
    data = '{\"test\": \"mest\"}'
    parsed_data = read_data(data)
    expected_data = {'test': 'mest'}
    assert parsed_data == expected_data
    parsed_data = read_data(expected_data, is_json=False)
    assert parsed_data == expected_data


def test_parse_data():
    data = {'test': 'mest'}
    parsed_data = parse_data(data)
    assert parsed_data == '{\"test\": \"mest\"}'
    parsed_data = parse_data(data, is_json=False)
    assert parsed_data == data

def test_reverse():
    assert (Reverse(3) >> 5) == 40
    assert (Reverse(2) << 5) == 1

def test_writer_init_with_no_param():
    writer = Writer()
    assert writer.debug
    assert writer.ext == 'log'
    assert writer.filename == 'debug.log'
    assert writer.fopen_mode == 'w+'
    assert writer.json
    assert writer.callback == None

def test_writer_init_with_params():
    callback = mock.Mock()

    writer = Writer(
        filename="test",
        ext="txt",
        debug=False,
        json=False,
        callback=callback,
    )
    assert writer.debug == False
    assert writer.ext == 'txt'
    assert writer.filename == 'test.txt'
    assert writer.fopen_mode == 'w+'
    assert writer.json == False
    assert writer.callback == callback

def test_writer_test_shift_callback():
    callback = mock.Mock()

    Writer(callback=callback) << {'test': 'mest'}
    callback.assert_called_once_with('debug.log')

def test_writer_file_write():
    Writer() << {}
    os.path.isfile('debug.log')
    os.remove('debug.log')

def test_writer_file_content():
    Writer() << {'test': 'mest'}
    with open('debug.log', 'r') as content_file:
        content = content_file.read()
        assert content == '{\"test\": \"mest\"}'
    os.remove('debug.log')

def test_writer_file_content_with_list():
    Writer() << ['1', '2']
    with open('debug.log', 'r') as content_file:
        content = content_file.read()
        assert content == '"1"\n"2"\n'
    os.remove('debug.log')

def test_writer_file_content_with_iterable():
    Writer() << map(int, ['1', '2'])
    with open('debug.log', 'r') as content_file:
        content = content_file.read()
        assert content == '1\n2\n'
    os.remove('debug.log')

def test_reader_init_with_no_param():
    Writer() << {}
    reader = Reader()
    assert reader.debug
    assert reader.ext == 'log'
    assert reader.filename == 'debug.log'
    assert reader.fopen_mode == 'r'
    assert reader.json
    os.remove('debug.log')

def test_reader_init_with_params():
    Writer(filename='test', ext='txt') << {'test': 'mest'}

    reader = Reader(
        filename="test",
        ext="txt",
        debug=False,
        json=True,
    )
    assert reader.debug == False
    assert reader.ext == 'txt'
    assert reader.filename == 'test.txt'
    assert reader.fopen_mode == 'r'
    assert reader.data == {'test': 'mest'}
    os.remove('test.txt')

def test_reader_define():
    Writer(filename='test', ext='txt') << {'test': 'mest'}
    data = Reader._define('test', ext='txt')
    assert data == {'test': 'mest'}
    os.remove('test.txt')
