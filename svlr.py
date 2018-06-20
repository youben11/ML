"""Single Variable Linear Regression"""

class Hypothesis(object):
    """In this class, our hypothesis will have the form 'h(x) = a.x + b'"""

    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def gradient_descent(self, data_set, alpha):
        converge = False
        while not converge:
            a = self.new_a(data_set, alpha)
            b = self.new_b(data_set, alpha)
            if (a, b) == (self.a, self.b):
                converge = True
            else:
                self.a = a
                self.b = b
            print "trying with values a = %f and b = %f" % (a,b)

    def new_a(self, data_set, alpha):
        keys = data_set.keys()
        ssum = 0.0
        for key in keys:
            ssum += (self.h(key) - data_set[key]) * key
        return self.a - alpha * (ssum / len(keys))

    def new_b(self, data_set, alpha):
        keys = data_set.keys()
        ssum = 0.0
        for key in keys:
            ssum += self.h(key) - data_set[key]
        return self.b - alpha * (ssum / len(keys))

    def h(self, x):
        return self.a * x + self.b

    def cost(self, data_set):
        keys = data_set.keys()
        square_sum = 0.0
        for key in keys:
            square_sum += (self.h(key) - data_set[key]) ** 2
        return square_sum / (2 * len(keys))

    def prediction_function(self):
        return lambda x: self.a * x + self.b

    def __str__(self):
        return "h(x) = %f * x + %f" % (self.a, self.b)


def regression(training_set):
    """This function will learn from the training_set provided
    and output the function that will predict future results.
    The training_set must be a dictionnary of the form {input: output},
    where the inputs and outputs are numbers.
    The returned value is a lambda function, that will try to predict correct
    outputs for some inputs."""

    hypothesis = Hypothesis()
    alpha = 0.05
    # we can try to chose the best alpha before starting the learning
    # the best alpha will make the gradient_descent converge rapidly
    hypothesis.gradient_descent(training_set, alpha)
    print hypothesis
    print "cost = %f" % hypothesis.cost(training_set)
    return hypothesis.prediction_function()
