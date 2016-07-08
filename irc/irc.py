import queue
from time import sleep
import socket
import threading
from .command import CMD
from .socket_reader import SocketReader
from .socket_writer import SocketWriter
from PyQt5 import QtCore


USER_MODE = {
    'NORMAL': 0,
    'INVISIBLE': 8
}


class IRCClient(QtCore.QObject):

    new_message_signal = QtCore.pyqtSignal(str)

    def __init__(self, ircaddr="open.ircnet.net", ircport=6667):
        QtCore.QObject.__init__(self)
        self.ircaddr = ircaddr
        self.ircport = ircport
        self.soc = None
        self.cmd_queue = None
        self.in_thread = None
        self.out_thread = None
        self.stop_event = None

    def set_address(self, ircaddr, ircport):
        self.ircaddr = ircaddr
        self.ircport = ircport

    def establish_socket_connection(self):
        self.soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.soc.connect((self.ircaddr, self.ircport))
        self.soc.settimeout(1)
        print('Success Connected Server')

    def login(self, nickname, realname):
        self.cmd_queue.put('PING')
        self.cmd_queue.put(
            CMD.set_nickname(nickname)
        )
        self.cmd_queue.put(
            CMD.login(nickname, realname, USER_MODE['NORMAL'])
        )

    def send_raw_cmd(self, cmd):
        self.cmd_queue.put(cmd)

    def connect(self, connection_signal):
        self.stop_event = threading.Event()
        self.establish_socket_connection()
        self.cmd_queue = queue.Queue()
        connection_signal.emit()

    def start_communication(self):
        self.in_thread = threading.Thread(
            target=SocketReader(
                stop_event=self.stop_event,
                soc=self.soc,
                new_message_signal=self.new_message_signal
                ).start
            )
        self.out_thread = threading.Thread(
            target=SocketWriter(
                stop_event=self.stop_event,
                soc=self.soc,
                cmd_queue=self.cmd_queue,
                ).start
            )
        self.in_thread.start()
        self.out_thread.start()

    def disconnect(self):
        self.stop_event.set()
        self.in_thread.join()
        self.out_thread.join()
