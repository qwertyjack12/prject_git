class RenderDigit:
    def __call__(self, num, *args, **kwargs):
        try:
            return int(num)
        except:
            return


class InputValues:
    def __init__(self, render):
        self.render = render

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            return [self.render(i) for i in func().split()]

        return wrapper


input_dg = InputValues(RenderDigit())(input)
res = input_dg()
print(res)
