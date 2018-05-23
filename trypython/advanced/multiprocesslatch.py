"""
Java の CoundDownLatch 風なクラス (マルチプロセス処理用)

REFERENCES::
https://stackoverflow.com/questions/10236947/does-python-have-a-similar-control-mechanism-to-javas-countdownlatch
https://qiita.com/shinkiro/items/75f3561d6bc96694ce30
"""
import multiprocessing as mp
import typing as ty


def __for_doctest(l):
    l.count_down()


class CountDownLatch:
    """\
    Java の CoundDownLatch 風なクラスです。
    使い方は Java 版と同じで以下のメソッドを利用します。

    - count_down
    - await

    count_down メソッドを各プロセスが呼び出しカウントを減らす。
    待機を行うプロセスは await メソッドで条件が揃うまで待つ。

    本クラスは、マルチプロセス処理で利用できます。

    >>> # ---------------------------------------------
    >>> # マルチプロセス処理で利用する場合
    >>> # ---------------------------------------------
    >>> import multiprocessing as mp
    >>> import time as tm
    >>> from trypython.advanced.multiprocesslatch import CountDownLatch, __for_doctest

    >>> latch = CountDownLatch(2)
    >>> proc1 = mp.Process(target=__for_doctest, args=(latch,))
    >>> proc2 = mp.Process(target=__for_doctest, args=(latch,))

    >>> latch.count
    2
    >>> latch.await(timeout=1.0)
    False

    >>> proc1.start()
    >>> tm.sleep(1)
    >>> latch.count
    1
    >>> latch.await(timeout=1.0)
    False

    >>> proc2.start()
    >>> tm.sleep(1)
    >>> latch.count
    0
    >>> latch.await(timeout=1.0)
    True
    """

    def __init__(self, count: int = 1):
        """
        オブジェクトを初期化します。

        :param count: カウント。デフォルト値は 1 です。 0 以下は指定できません。(ValueError)

        >>> import trypython.advanced.multiprocesslatch as mp_latch
        >>> latch = mp_latch.CountDownLatch(-1)
        Traceback (most recent call last):
        ...
        ValueError: 0 以下は指定できません。 [-1]
        >>> latch1 = mp_latch.CountDownLatch(1)
        >>> latch2 = mp_latch.CountDownLatch(5)
        """
        if count <= 0:
            raise ValueError(f'0 以下は指定できません。 [{count}]')
        self._count = mp.Value('i', count)  # type: mp.Value
        self.lock = mp.Condition()

    @property
    def count(self):
        """
        現在のカウントを取得します。

        :return: 現在のカウント

        >>> import trypython.advanced.multiprocesslatch as mp_latch
        >>> latch = mp_latch.CountDownLatch(5)
        >>> latch.count
        5
        >>> latch.count_down()
        >>> latch.count
        4
        >>> latch.count_down()
        >>> latch.count_down()
        >>> latch.count_down()
        >>> latch.count
        1
        """
        return self._count.value

    def count_down(self):
        """
        件数を１減らします。

        >>> import trypython.advanced.multiprocesslatch as mp_latch
        >>> latch = mp_latch.CountDownLatch(5)
        >>> latch.count
        5
        >>> latch.count_down()
        >>> latch.count
        4
        >>> latch.count_down()
        >>> latch.count_down()
        >>> latch.count_down()
        >>> latch.count
        1
        """
        with self.lock, self._count.get_lock():
            self._count.value -= 1
            if self._count.value <= 0:
                self.lock.notify_all()

    def await(self, timeout: ty.Optional[float] = None) -> bool:
        """
        カウントが 0 になるまで待機します。
        timeout を指定している場合、指定時間後に結果を返します。
        戻り値が False の場合、タイムアウトしたことを示します。

        :param timeout: タイムアウト（秒）デフォルトは None で、カウントが 0 になるまで無制限待機します。
        :return: タイムアウトした場合は False。それ以外は True

        >>> import trypython.advanced.multiprocesslatch as mp_latch
        >>> latch = mp_latch.CountDownLatch(5)
        >>> latch.count
        5
        >>> latch.await(timeout=0.1)
        False
        >>> latch.count_down()
        >>> latch.count
        4
        >>> latch.await(timeout=0.1)
        False
        >>> latch.count_down()
        >>> latch.count_down()
        >>> latch.count_down()
        >>> latch.count
        1
        >>> latch.await(timeout=0.1)
        False
        >>> latch.count_down()
        >>> latch.count
        0
        >>> latch.await()
        True
        """
        with self.lock, self._count.get_lock():
            if self._count.value > 0:
                return self.lock.wait(timeout=timeout)
            else:
                return True
