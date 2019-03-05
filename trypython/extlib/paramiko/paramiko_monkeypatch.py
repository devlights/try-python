# coding: utf-8
"""
paramiko の SSHClient.exec_command は内部で stdin のみ binary-mode で
処理しているが、stdout と stderr はテキストモードで処理している。

そのため、euc-jp な環境で動かすと UnicodeDecodeError が発生してしまう。

それを防ぐために、stdout, stderr を binary-mode で処理するパッチ関数を以下に定義している。

以下の情報を参考にした。
  https://gist.github.com/smurn/4d45a51b3a571fa0d35d
"""
import paramiko


def monkey_patch():
    paramiko.SSHClient.exec_command = _patched_exec_command


def _patched_exec_command(
        self,
        command: str,
        bufsize: int = -1,
        timeout: int = None,
        get_pty: bool = False,
        environment: dict = None,
) -> tuple:
    """
    元の exec_command の処理そのままで stdout, stderr を binary-mode で処理します。
    """
    chan = self._transport.open_session(timeout=timeout)
    if get_pty:
        chan.get_pty()
    chan.settimeout(timeout)
    if environment:
        chan.update_environment(environment)
    chan.exec_command(command)
    stdin = chan.makefile('wb', bufsize)
    stdout = chan.makefile('rb', bufsize)
    stderr = chan.makefile_stderr('rb', bufsize)
    return stdin, stdout, stderr
