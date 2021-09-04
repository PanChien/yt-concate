from yt_concate.pipline.steps.step import StepException


class Pipline:  # PipLine(導管)就像一個工廠的產線
    def __init__(self, steps):  # 這個steps是一個清單，裡面裝著步驟，投入的參數
        self.steps = steps  # 作一個.steps屬性，設值為投進來的steps參數

    def run(self, inputs, utils):  # 作一個run method，投入inputs，而inputs是一個字典，裡面裝著設定的參數
        data = None  # 傳遞用的變數，初使值為None
        for step in self.steps:
            try:
                data = step.process(data, inputs, utils)
            except StepException as e:
                print('Exception happened: ', e)
                break
