import ray
ray.init(include_dashboard=False)

@ray.remote
class Counter(object):
    def __init__(self):
        self.n = 0

    def increment(self):
        self.n += 1

    def read(self):
        return self.n

counters = [Counter.remote() for i in range(4)]
[c.increment.remote() for c in counters]

counters[0].increment.remote()

futures = [c.read.remote() for c in counters]
print(ray.get(futures))
