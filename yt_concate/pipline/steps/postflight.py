# Postflight 結束執行後的處理
from .step import Step


class Postflight(Step):
    def process(self, data, inputs, utils):
        print('in Postflight')
        pass