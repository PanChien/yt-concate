# Preflight 開始執行前的處理
from .step import Step


class Preflight(Step):
    def process(self, data, inputs, utils):
        print('in Preflight')
        utils.create_dirs()