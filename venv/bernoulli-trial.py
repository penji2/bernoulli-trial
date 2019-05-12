import random
import sys


class Bernoulli:

    def __init__(self, probability_parameter):
        if 0 <= probability_parameter <= 1:
            self.p = probability_parameter
        else:
            sys.exit("p must be between 0 and 1")

    def trial(self):  # Bernoulli trial function, probability of success = p, loss = 1 - p
        tmp = random.random()
        if tmp <= self.p:
            result = 1
        else:
            result = 0
        return result  # returns 0 - loss, 1 - success

    def geo_generator(self):  # random variable X generator with geometric distribution
        table_of_success, k_array = list()

        # for i in range(20):
        #     count = 1
        #     for j in range(1000):
        #         tmp = self.trial()
        #         count += 1
        #         table_of_success.append(tmp)
        #         if tmp == 1:
        #             k_array.append(count)

    def histogram(self):  # function that generates histogram of distribution of random X variable
        pass


class Testing:

    def __init__(self):
        pass

    def first_model(self):
        pass

    def second_model(self):
        pass


if __name__ == '__main__':
    obj = Bernoulli(0.5)
    obj.geo_generator()
