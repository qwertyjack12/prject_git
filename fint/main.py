class ImageFileAcceptor:
    def __init__(self, extensions):
        self.extensions = tuple(f'.{i}' for i in extensions)

    def __call__(self, *args, **kwargs):
        print(self.extensions)
        return args[0].endswith(self.extensions)