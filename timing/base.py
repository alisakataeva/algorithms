import timeit


class Timing:

    def __init__(self):
        pass

    def timeit(self, func, *args):
        start = timeit.default_timer()
        func(*args)
        return str( timeit.default_timer() - start )


class SearchTiming(Timing):

    def __init__(self, func, text, substr):

        self.f = func
        self.t = text
        self.s = substr

        self.text_length = len(self.t)
        self.substr_length = len(self.s)

        self.time = self.timeit(self.f, self.t, self.s)

    def __str__(self):
        return '< SearchTiming Instance : {func} has ended within {time} seconds.'.format(
            func=self.f.__name__,
            time=self.time
        )