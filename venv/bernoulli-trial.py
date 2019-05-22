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

        plt.bar(x_axis, y_axis)
        plt.grid(linestyle='--')
        plt.show()


class FirstTest(Bernoulli):

    def __init__(self, probability_parameter, num_of_trials):
        Bernoulli.__init__(self, probability_parameter, num_of_trials)

    def trial(self, probab):  # Bernoulli trial function, probability of success = p, loss = 1 - p
        tmp = random.random()
        if tmp <= probab:
            result = 1
        else:
            result = 0
        return result  # returns 0 - loss, 1 - success

    def first_model(self, elem_amount):

        probe_list = [i for i in range(1, elem_amount + 1)]
        tmp = 1
        for i in range(self.n):  # loop that coordinates list appending for histogram
            # another for loop here
            for item in probe_list:
                if self.trial(1 / item) == 1:
                    tmp = 1 / item

            self.k_array.append(tmp)

    def histogram(self, hist_title):  # function that generates histogram of distribution of random X variable
        self.k_array.sort()
        # counter = collections.Counter(self.k_array)
        # x_axis = [x for x in range(len(counter.values()))]
        # y_axis = [item / self.n for item in counter.values()]

        plt.title(hist_title)
        plt.hist(self.k_array)
        # plt.bar(x_axis, y_axis)
        plt.grid(linestyle='--')
        plt.show()


class SecondTest(Bernoulli):

    def __init__(self, probability_parameter, num_of_trials):
        Bernoulli.__init__(self, probability_parameter, num_of_trials)

    def second_model(self, elem_amount):

        probe_list = [i for i in range(1, elem_amount + 1)]
        tmp = 1
        for i in range(self.n):  # loop that coordinates list appending for histogram
            # another for loop here
            for item in probe_list:
                if self.trial() == 1:
                    tmp = item

            self.k_array.append(tmp)

    def histogram(self, hist_title):  # function that generates histogram of distribution of random X variable
        self.k_array.sort()
        # counter = collections.Counter(self.k_array)
        # x_axis = [x for x in range(len(counter.values()))]
        # y_axis = [item / self.n for item in counter.values()]

        plt.title(hist_title)
        plt.hist(self.k_array, bins=self.k_array.sort(), edgecolor='black', density=True, stacked=True)
        # plt.bar(x_axis, y_axis)
        plt.grid(linestyle='--')
        plt.show()


if __name__ == '__main__':
    # obj = Bernoulli(0.6, 10000)
    # obj.geo_generator()
    # obj.histogram("title")

    # first_obj = FirstTest(0.5, 10000)
    # first_obj.first_model(100)
    # first_obj.histogram('Histogram rozkładu zmiennej losowej, Sekwencja 100 elementow, 10000 prob')

    second_obj = SecondTest(0.5, 10000)
    second_obj.second_model(100)
    second_obj.histogram('Histogram rozkładu zmiennej losowej, Sekwencja 100 elementow, 10000 prob')
