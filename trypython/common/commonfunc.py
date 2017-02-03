# coding: utf-8

def pr(prefix: str, message: str) -> None:
    """
    指定された値を「＝」で繋いで出力します。

    :param prefix: プリフィックス
    :param message: メッセージ
    :return: 無し
    """
    print(f'{prefix}={message}')