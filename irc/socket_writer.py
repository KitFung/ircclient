from time import sleep
import socket
import queue


class SocketWriter(object):
    def __init__(self, stop_event, soc, cmd_queue):
        self.stop_event = stop_event
        self.soc = soc
        self.cmd_queue = cmd_queue

    def send_cmd(self, cmd):
        b_data = bytes("%s\r\n" % cmd, "UTF-8")
        print(cmd)
        self.soc.send(b_data)

    def start(self):
        while not self.stop_event.is_set():
            sleep(0.1)
            try:
                cmd = self.cmd_queue.get(timeout=1)
                if cmd:
                    self.send_cmd(cmd)
                self.cmd_queue.task_done()
            except queue.Empty as e:
                pass
