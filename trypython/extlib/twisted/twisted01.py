"""
twisted の サンプルです。
最も基本的な Echo サーバのサンプル

参考URL: http://bit.ly/2VkyAG2

本サンプルを起動して、コマンドラインから
  $ telnet 127.0.0.1 12345
とすると接続できる.
"""
import os

from twisted.internet import reactor
from twisted.internet.address import IPv4Address
from twisted.internet.endpoints import TCP4ServerEndpoint
from twisted.internet.interfaces import ITransport, IReactorCore
from twisted.internet.protocol import Protocol, Factory

from trypython.common.commoncls import SampleBase
from trypython.common.commonfunc import pr


# noinspection PyArgumentList
class EchoProtocol(Protocol):
    def dataReceived(self, data: bytes):
        """
        データを受信した際に呼ばれるメソッド

        データを処理する際は、 self.transport 経由で行う。
        self.transport は、 ITransport インターフェースを実装したもの。

        接続元の情報は、 self.transport.getPeer() で取得できる。
        getPeer() から返るのは、 IPv4Address or IPv6Address。
        どちらも、type, host, port という属性を持つ。

        状態を保持したりする際は、 self.factory 経由で行う。
        self.factory は、 Factory.buildProtocol() 呼び出し時に設定される。
        """
        pr('data received', data)

        if data.strip() == b'quit':
            r: IReactorCore = reactor
            r.stop()

        t: ITransport = self.transport
        t.write(data)

    def connectionMade(self):
        """クライアントから接続された際に呼ばれるメソッド"""
        super().connectionMade()
        t: ITransport = self.transport
        t.write(self._make_welcome_message())

    def _make_welcome_message(self):
        peer: IPv4Address = self.transport.getPeer()
        welcome = bytes(f'Welcome from {peer.host}.{os.linesep}', encoding='utf-8')
        quit_message = bytes(f'Type "quit" to shutdown...{os.linesep}{os.linesep}', encoding='utf-8')
        return welcome + quit_message


class EchoFactory(Factory):
    # この Factory が対象とする Protocol
    protocol = EchoProtocol

    def buildProtocol(self, addr: IPv4Address):
        """
        本Factoryが対象としているプロトコルを生成する.

        デフォルトの実装が、「クラス変数 protocol に設定されているクラスを生成(p)して p.factory に設定する」
        という動作になっているため、普段は protocol に対象の Protocol を設定すれば、いちいちオーバーライドする必要はない。
        本サンプルでは、ログ出力のために利用している。

        猶、本処理を通ることで、 Protocol オブジェクト側から Factory に対して self.factory でアクセスできる。
        Protocol は、接続の度に生成され、切断とともにインスタンスが破棄されるので、状態を保持することができない。
        状態を保持するには、Factory 側に保持する機構を用意して、Protocol 側からは self.factory でアクセスして処理する。

        参考URL: https://bit.ly/2T2U5P2
        """
        pr('addr.type', addr.type)
        pr('addr.host', addr.host)
        pr('addr.port', addr.port)

        return super().buildProtocol(addr)


class Sample(SampleBase):
    def exec(self):
        echo_endpoint = TCP4ServerEndpoint(reactor, 12345)
        echo_endpoint.listen(EchoFactory())

        r: IReactorCore = reactor
        r.run()


def go():
    obj = Sample()
    obj.exec()
