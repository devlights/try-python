"""
trypython パッケージのメインファイルです.

python インタープリターにて

$ python -m trypython

と起動した場合に実行されます。
"""
import argparse

from trypython import mappings

onetime = False
verbose = False


def main():
    """メイン処理. ユーザに入力を求め、指定されたサンプルを実行します"""
    while True:
        # ユーザにサンプル名の入力を行ってもらう
        user_input: str = input('ENTER EXAMPLE NAME: ').strip()

        if not user_input:
            continue

        if user_input.lower() == 'quit':
            break

        # 候補リストを構築
        candidates = [x for x in mappings.keys() if user_input in x]
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
        if target not in mappings:
            print(f'sorry...not exists - {target}. try again')
            continue

        m = mappings[target]
        if not callable(m):
            print(f'サンプルとして実行不可 {m}')
            continue

        # サンプル実行
        try:
            print(f'\n[START] ==== {target} ====')
            m()
            print(f'[END  ] ==== {target} ====\n')
        except Exception as e:
            print(f'サンプル実行中にエラーが発生しました [{e}]')
        finally:
            if onetime:
                break

    print('\nDONE')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='trypython -- example executor')
    parser.add_argument('-o', '--onetime', action='store_true', help='サンプルを一度だけ実行して終了する')
    parser.add_argument('-v', '--verbose', action='store_true', help='冗長なログ出力モード')

    args = parser.parse_args()

    onetime = args.onetime
    verbose = args.verbose
    main()
