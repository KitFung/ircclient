from time import sleep
import socket


class SocketReader(object):

    def __init__(self, stop_event, soc, new_message_signal):
        self.stop_event = stop_event
        self.soc = soc
        self.new_message_signal = new_message_signal

    def receive_data(self):
        data = self.soc.recv(4096)
        return data.decode('utf-8', 'ignore')

    def keep_recieving(self):
        try:
            while True:
                data = self.receive_data()
                if data is not None:
                    print(data)
                    self.new_message_signal.emit(data)
        except socket.timeout as e:
            pass
        except socket.error as e:
            print("error({0}): {1}".format(e.errno, e.strerror))

    def start(self):
        while not self.stop_event.is_set():
            self.keep_recieving()
            sleep(1)
