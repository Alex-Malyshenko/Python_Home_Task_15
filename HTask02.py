# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК. Соберите информацию о содержимом в виде объектов
# namedtuple. Каждый объект хранит: имя файла без расширения или название
# каталога, расширение, если это файл, флаг каталога, название родительского
# каталога. Написать 3-5 тестов к задаче.

import argparse
import os
from collections import namedtuple
from typing import List

def gen_file_data(dir_path: str) -> List[namedtuple]:
    FileData = namedtuple('FileData',
                          ['name', 'ext', 'is_dir', 'parent_dir'])
    return [FileData(
        name=file.split('.')[0]
        if not os.path.isdir(os.path.join(dir_path, file)) else file,
        ext=file.split('.')[-1]
        if not os.path.isdir(os.path.join(dir_path, file)) else '',
        is_dir=os.path.isdir(os.path.join(dir_path, file)),
        parent_dir=os.path
        .abspath(dir_path)
        .split(os.path.sep)[-1])
        for file in os.listdir(dir_path)]


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Command line args parser')
    parser.add_argument('dir_path', default='.', type=str,
                        help="path to dir to collect data from")
    line_args = parser.parse_args()
    res = gen_file_data(line_args.dir_path)
    print(res)


