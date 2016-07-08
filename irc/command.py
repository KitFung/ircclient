class CMD(object):

    @classmethod
    def set_nickname(cls, nickname):
        return 'NICK %s' % nickname

    @classmethod
    def login(cls, username, realname, mode):
        return 'USER %s %d * :%s' % (username, mode, realname)

    @classmethod
    def join_channel(cls, channel):
        return "JOIN #%s" % channel

    @classmethod
    def list_channel_user(cls, channel):
        return "WHO #%s" % channel

    @classmethod
    def ping_target(cls, target):
        return "PING %d" % target

    @classmethod
    def msg_target(cls, target, msg):
        return "PRIVMSG {} {}".format(target, msg)

    @classmethod
    def quit(cls):
        return "QUIT"
