# !/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:lupengliang
import logging
import socket
import time

import paramiko


class RemoteControl:
    """后台执行linux"""

    def __init__(self, IP, user, password, shell="bash", supassword=None, port=22):
        self.prompt = "x00109546"
        self.waitstr = self.prompt
        self.interval = 0.1
        policy = paramiko.client.AutoAddPolicy()
        try:
            self.m_client = paramiko.client.SSHClient()
            self.m_client.set_missing_host_key_policy(policy)
            self.m_client.connect(IP, port, user, password, timeout=15)
        except:
            time.sleep(5)
            self.m_client = paramiko.client.SSHClient()
            self.m_client.set_missing_host_key_policy(policy)
            self.m_client.connect(IP, port, user, password, timeout=15)

        self.m_channel = self.m_client.invoke_shell()
        self.m_channel.setblocking(0)
        self.shell = shell

        # *****************
        ret = self.read_until("?", 3, ignore=True)
        logging.debug("wenhao ? ret:%s" % str(ret))

        self.m_channel.send("vt100\n")
        self.loginuser = user
        time.sleep(0.5)
        if user != "root" and supassword:
            self.m_channel.send("su\n")
            ret = self.read_until("assword:", 3)
            logging.debug(repr(ret))
            self.m_channel.send("%s\n" % supassword)
            time.sleep(0.5)

        if shell == "bash":
            self.m_channel.send("bash\n")
            time.sleep(0.5)
            self.m_channel.send("PS1=\"" + self.waitstr + "\"\n")
        elif shell == "csh":
            self.m_channel.send("csh\n")
            time.sleep(0.5)
            self.m_channel.send("unalias cd\n")
            time.sleep(0.5)
            self.m_channel.send("set prompt=\"" + self.waitstr + "\"\n")
            result = self.read_until(self.prompt,0.5, ignorelog=True)
            logging.debug(repr(result))
            result = self.read_until(self.prompt, 0.5, ignorelog=True)
            logging.debug(repr(result))

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        logging.info("ssh close")
        self.close()

    def auto_save_key(self, sshserver):
        self.m_channel.send("ssh%s\n" % sshserver)
        result = self.read_until("yes/no", 1, ignorelog=True)
        logging.debug(repr(result))
        if result.find("yes/no") != -1:
            self.cmd("yes", "assword:")
            self.cmd("\x03")

    def read_until(self, waitstr, timeout, length=None, ignorelog=False):
        result = b""
        waitstr = waitstr.encode('utf-8')
        self.m_channel.settimeout(self.interval)
        total = int(timeout/self.interval)
        recv_number = length
        for i in range(total):
            if recv_number is None:
                recv_number = len(waitstr)
                while True:
                    try:
                        if self.m_channel.recv_ready():
                            result = result + self.m_channel.recv(recv_number)
                        else:
                            break
                    except socket.timeout:
                        recv_number = 1
                        continue
                    except Exception as e:
                        raise e
                    if result.find(waitstr) != -1:
                        break
                    time.sleep(self.interval)
                    if i + 1 >= total:
                        if not ignorelog:
                            logging.info("Wait time out!")
                            return
                    result.decode("utf-8")

    def suUser(self, user, supass, su="su -"):
        self.cmd(su + user, waitstr="asssword")
        self.cmd(supass)
        if self.shell == "bash":
            self.m_channel.send("bash\n")
            time.sleep(0.5)
            self.m_channel.send("PS1=\"" + self.waitstr + "\"\n")
        elif self.shell == "csh":
            self.m_channel.send("csh\n")
            time.sleep(0.5)
            self.m_channel.send("unalias cd\n")
            time.sleep(0.5)
            peompt = self.m_channel.send("set prompt=\"" + self.waitstr + "\"\n")

    def cmd(self, command, waitstr=None, length=None, timeout=3):
        info = ""
        self.m_channel.send(command+"\n")
        if not waitstr:
            waitstr = self.waitstr
        if waitstr:
            result = self.read_until(waitstr, timeout, length)
            logging.info(result)
            info = "\n".join(result.split("\n")[1:])
            return info


if __name__ == '__main__':
    with RemoteControl("8.7.132.4", "pass", "123") as ssh:
        ssh.cmd("ll")



