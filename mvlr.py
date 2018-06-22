"""MultiVariate Linear Regression"""

class Hypothesis(object):
    """The hypothesis will have the form 'h(X) = transpo(coeff) * X', where
        - coeff is the vector of the theta coefficient
        - X is the feature vector
        An example with 2 feature:
        h(X) = coeff[0] + coeff[1] * X[0] + coeff[2] * X[1]"""

    def __init__(self, feature_number):
        self.feature_number = feature_number
        self.coeff = [0 for i in range(feature_number + 1)]

    def gradient_descent(self, data_set, learning_rate):
        converge = False
        while not converge:
            coeff = self.new_coeff(data_set, learning_rate)
            if coeff == self.coeff:
                converge = True
            else:
                self.coeff = coeff
            print "trying with coefficient:", self.coeff

    def new_coeff(self, data_set, learning_rate):
        features = data_set.keys()
        list_sum = [0.0 for i in range(self.feature_number + 1)]
        for X in features:
            addend = self.h(X) - data_set[X]
            list_sum[0] += addend
            for i in range(1, len(list_sum)):
                list_sum[i] += addend * X[i-1]
        for i in range(self.feature_number + 1):
            list_sum[i] = self.coeff[i] \
                            - learning_rate * (list_sum[i] / len(features))
        return list_sum


    def h(self, X):
        result = self.coeff[0]
        for i in range(1, self.feature_number + 1):
            result += self.coeff[i] * X[i-1]
        return result

    def cost(self, data_set):
        keys = data_set.keys()
        square_sum = 0.0
        for key in keys:
            square_sum += (self.h(key) - data_set[key]) ** 2
        return square_sum / (2 * len(keys))

    def prediction_function(self):
        return lambda X: self.h(X)

    def __str__(self):
        s = ['h(X) = %f ' % self.coeff[0]]
        for i in range(1, self.feature_number + 1):
            s.append('+ %f * X[%d]' % (self.coeff[i], i-1))
        return ''.join(s)


def regression(training_set, feature_number):
    """This function will learn from the training_set provided
    and output the function that will predict future results.
    The training_set must be a dictionnary of the form {input: output},
    where the input is a list or a tuple of size feature_number
    and the output is a number.
    The returned value is a lambda function, that will try to predict correct
    outputs for some inputs."""

    hypothesis = Hypothesis(feature_number)
    learning_rate = 1

    hypothesis.gradient_descent(training_set, learning_rate)
    print hypothesis
    print "cost = %f" % hypothesis.cost(training_set)
    return hypothesis.prediction_function()
