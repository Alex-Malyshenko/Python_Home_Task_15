import os
import shutil
from collections import namedtuple
from HTask02 import gen_file_data
import pytest

@pytest.fixture
def temp_dir():
    """
    Fixture that creates temporary dir 'test_dir' with 4 elements inside:
    2 empty dirs 'a' and 'b'
    2 files 'c.py' and 'd.txt'
    and returns temp dir name

    Clears temp dir afterwards
    """
    os.mkdir('test_dir')
    d_name = 'test_dir'
    os.makedirs(os.path.join(d_name, 'a'))
    os.makedirs(os.path.join(d_name, 'b'))
    with open(os.path.join(d_name, 'c.py'), 'w', encoding='UTF-8') as f1:
        f1.write('# test1')
    with open(os.path.join(d_name, 'd.txt'), 'w', encoding='UTF-8') as f1:
        f1.write('test2')
    yield d_name
    shutil.rmtree(d_name)

@pytest.fixture
def file_data():
    return namedtuple('FileData',
                      ['name', 'ext', 'is_dir', 'parent_dir'])


def test_gen_file_data_correct_file_name(temp_dir, file_data):
    res = gen_file_data(temp_dir)
    expected = file_data(
        name='a', ext='', is_dir=True, parent_dir='test_dir')
    assert res[0].name == expected.name


def test_gen_file_data_correct_file_ext(temp_dir, file_data):
    res = gen_file_data(temp_dir)
    expected = file_data(
        name='c', ext='txt', is_dir=False, parent_dir='test_dir')
    assert res[3].ext == expected.ext


def test_gen_file_data_is_dir(temp_dir, file_data):
    res = gen_file_data(temp_dir)
    expected = file_data(
        name='a', ext='', is_dir=True, parent_dir='test_dir')
    assert res[0].is_dir == expected.is_dir


def test_gen_file_data_correct_parent_dir(temp_dir, file_data):
    res = gen_file_data(temp_dir)
    expected = file_data(
        name='b', ext='', is_dir=True, parent_dir='test_dir')
    assert res[1].parent_dir == expected.parent_dir


def test_gen_file_data_correct_size(temp_dir, file_data):
    assert len(gen_file_data(temp_dir)) == 4
