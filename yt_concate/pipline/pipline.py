from yt_concate.pipline.steps.step import StepException


class Pipline:  # PipLine(導管)就像一個工廠的產線
    def __init__(self, steps):
        self.steps = steps

    def run(self, inputs):
        data = None  # 傳遞用的變數，初使值為None
        for step in self.steps:
            try:
                data = step.process(data, inputs)
            except StepException as e:
                print('Exception happened: ', e)
                break
