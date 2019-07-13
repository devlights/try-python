"""
trypython パッケージのメインファイルです.

python インタープリターにて

$ python -m trypython

と起動した場合に実行されます。
"""
import importlib
import os
import pathlib
import sys
from typing import Dict


class ExampleLoadError(Exception):
    """サンプルのロード中にエラーが発生した場合の例外

    Attributes:
        example_name (str): エラーが発生したモジュール名
    """

    def __init__(self, example_name: str):
        self.example_name = example_name


def load_examples() -> Dict[str, object]:
    """サンプルをロードします.

    Returns:
        dict[str, object]: Key：サンプル名、Value: モジュール の辞書
    Raises:
        ExampleLoadError: ロード中にエラーが発生した場合
    """
    examples = {}
    basedir = pathlib.Path(os.getcwd())

    for p in basedir.rglob('*.py'):
        real_path = str(p)

        # 読み込み不要なものを除外
        if any(ignore in real_path for ignore in ('__init__', '__main__')):
            continue

        # モジュール名を構築
        #   - trypython以降の文字列を取得
        #   - ファイル名の末尾の ".py" を除去
        #   - "/" を "." に置換
        index = real_path.find('trypython')
        mod_name = real_path[index:-3].replace('/', '.')

        if not mod_name:
            continue

        # windows特有のモジュールはOS判定を実施
        if 'windows' in mod_name:
            if os.name != 'nt':
                continue

        # モジュールをロード
        try:
            m = importlib.import_module(mod_name)
            examples[mod_name[mod_name.rfind('.') + 1:]] = m
        except Exception:
            raise ExampleLoadError(mod_name)

    return examples


def main():
    """メイン処理. 存在するサンプルをロードしてユーザに入力を要求します."""
    # サンプルをロード
    try:
        examples = {k.lower(): v for k, v in load_examples().items()}
    except ExampleLoadError as e:
        print(f'サンプルのロード中にエラーが発生しました. [{e.example_name}]')
        sys.exit(-1)

    while True:
        # ユーザにサンプル名の入力を行ってもらう
        user_input: str = input('ENTER EXAMPLE NAME: ').strip()

        if not user_input:
            continue

        if user_input.lower() == 'quit':
            break

        # 候補リストを構築
        candidates = [x for x in examples if user_input in x]
        if not candidates:
            print(f'no hit...try again.')
            continue
        if 1 < len(candidates):
            print(f'hit {len(candidates)} counts.')
            for x in candidates:
                print(f'\t{x}')
            continue

        # 実行対象を検査
        target = candidates[0]
        if target not in examples:
            print(f'sorry...not exists - {target}. try again')
            continue

        m = examples[target]
        if not hasattr(m, 'go'):
            print(f'サンプルとして実行するには go() が実装されている必要があります.')
            continue

        # サンプル実行
        try:
            print(f'\n[START] ==== {m.__name__} ====')
            m.go()
            print(f'[END  ] ==== {m.__name__} ====\n')
        except Exception as e:
            print(f'サンプル実行中にエラーが発生しました [{e}]')

    print('\nDONE')


if __name__ == '__main__':
    main()
