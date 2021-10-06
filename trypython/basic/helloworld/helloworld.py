from trypython.common.commoncls import SampleBase

class Sample(SampleBase):
    m1: str = 'hello'

    def exec(self) -> None:
        m2: str = 'world'
        print(f'{self.m1} {m2}')


def go():
    obj = Sample()
    obj.exec()
