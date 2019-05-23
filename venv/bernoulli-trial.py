import random
import sys
import matplotlib.pyplot as plt
import numpy as np
import collections


class Bernoulli:

    def __init__(self, probability_parameter, num_of_trials):
        self.n = num_of_trials
        self.k_array = list()
        if 0 <= probability_parameter <= 1:
            self.p = probability_parameter
        else:
            sys.exit("p must be between 0 and 1")

    @staticmethod
    def set_generator(set_amount):
        for i in range(1, set_amount + 1):
            yield i

    def trial(self):  # Bernoulli trial function, probability of success = p, loss = 1 - p
        tmp = random.random()
        if tmp <= self.p:
            result = 1
        else:
            result = 0
        return result  # returns 0 - loss, 1 - success

    def geo_generator(self):  # random variable X generator with geometric distribution
        table_of_success = list()
        for i in range(self.n):
            k = 1
            while True:
                tmp = self.trial()
                if tmp == 1:
                    break
                table_of_success.append(tmp)
                k += 1
            self.k_array.append(k)
            # print("table of success ", table_of_success)
            # print("karray", k_array)

    def histogram(self, hist_title):  # function that generates histogram of distribution of random X variable
        self.k_array.sort()
        counter = collections.Counter(self.k_array)
        x_axis = [x for x in range(len(counter.values()))]
        y_axis = [item / self.n for item in counter.values()]

        plt.title(hist_title)

        plt.bar(x_axis, y_axis, edgecolor='black')
        plt.grid(linestyle='--')
        plt.show()


class FirstTest(Bernoulli):

    def __init__(self, probability_parameter, num_of_trials):
        Bernoulli.__init__(self, probability_parameter, num_of_trials)

    def first_model(self, set_amount):
        tmp = 1
        for i in range(self.n):  # loop that coordinates list appending for histogram
            # another for loop here
            for item in FirstTest.set_generator(set_amount):
                if self.trial(1 / item) == 1:
                    tmp = 1 / item

            self.k_array.append(tmp)

    def trial(self, probab):  # Bernoulli trial function, probability of success = p, loss = 1 - p
        tmp = random.random()
        if tmp <= probab:
            result = 1
        else:
            result = 0
        return result  # returns 0 - loss, 1 - success


class SecondTest(Bernoulli):

    def __init__(self, probability_parameter, num_of_trials):
        Bernoulli.__init__(self, probability_parameter, num_of_trials)

    def second_model(self, set_amount):
        tmp = 1
        for i in range(self.n):  # loop that coordinates list appending for histogram
            # another for loop here
            for item in Bernoulli.set_generator(set_amount):
                if self.trial() == 1:
                    tmp = item

            self.k_array.append(tmp)


if __name__ == '__main__':
    set_amount = 100
    number_of_trials = 100000
    prob = 0.5
    #
    # obj = Bernoulli(prob, number_of_trials)
    # obj.geo_generator()
    # obj.histogram('Histogram rozkładu zmiennej losowej, {} prob'.format(number_of_trials))

    first_obj = FirstTest(prob, number_of_trials)
    first_obj.first_model(set_amount)
    first_obj.histogram('Histogram rozkładu zmiennej losowej, Sekwencja {} elementow, {} prob'.format(set_amount, number_of_trials))
    #
    # second_obj = SecondTest(prob, number_of_trials)
    # second_obj.second_model(set_amount)
    # second_obj.histogram('Histogram rozkładu zmiennej losowej, Sekwencja {} elementow, {} prob'.format(set_amount, number_of_trials))
