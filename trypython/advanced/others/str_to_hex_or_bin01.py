"""
文字列を16進数に変換するサンプルです。
bitstring を利用します。

参考URL: http://bit.ly/2VllbxA, http://bit.ly/2EyyQfm
"""
from datetime import date

from bitstring import BitArray

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


class Sample(SampleBase):
    def exec(self):
        message = f'Hello World at {date.today()}'
        message_bytes = bytes(message, encoding='utf-8')

        bit_array = BitArray(bytes=message_bytes)

        pr('original', message)
        pr('\t==> hex      ', bit_array.hex)
        pr('\t==> bin      ', bit_array.bin)
        pr('\t==> bytes    ', bit_array.tobytes())
        pr('\t==> str      ', str(bit_array.tobytes(), encoding='utf-8'))
        pr('\t==> length   ', bit_array.length // 8)
        pr('\t==> 1st byte ', bit_array[:8].tobytes())
        pr('\t==> 2nd byte ', bit_array[8:8 * 2].tobytes())
        pr('\t==> last byte', bit_array[-8:].tobytes())


def go():
    obj = Sample()
    obj.exec()
