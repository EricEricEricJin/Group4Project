from DFRobot_RaspberryPi_Expansion_Board import DFRobot_Expansion_Board_IIC as Board


class analRead:
    def __init__(self, port):
        self.board = Board(1, 0x10)
        self.board.begin()
        self.board.set_adc_enable()
        if port == 0:
            self.port = self.board.A0
        elif port == 1:
            self.port = self.board.A1
        elif port == 2:
            self.port = self.board.A2
        elif port == 3:
            self.port = self.board.A3

    def _read_anal(self):
        return self.board.get_adc_value(self.port)

    def read_pwr(self, resistance):
        # P = U^2 / R
        return (self._read_anal() / 4095 * 5) ** 2 / resistance
