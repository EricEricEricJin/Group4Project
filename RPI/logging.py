from socket import *
class Logging:
    def __init__(self, master_addr):
        self.log_sock = socket(AF_INET, SOCK_DGRAM)
        self.master_addr = master_addr

    def log(self, packed_data):
        self.log_sock.sendto(packed_data, self.master_addr)
        print("SEND", packed_data)
