from abc import ABC
from abc import abstractmethod


class Step(ABC):
    def __init__(self):  # 每個步驟不一定都須要這個init，所以不加抽象類別
        pass

    @abstractmethod
    def process(self, data, inputs, utils):  # 目前先假設每一個步驗都有這個抽象類別，data為傳遞用的資料，inputs為設定的參數
        pass  # 內容先沒有


class StepException(Exception):  # 錯誤補捉與停止程式，因為是捕捉錯誤所以是要來繼承TypException用的class
    pass

