import random
import sys
import matplotlib.pyplot as plt


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

    def histogram(self):  # function that generates histogram of distribution of random X variable
        plt.hist(self.k_array, edgecolor='black', bins=20)
        plt.title('Histogram liczby porównań')
        plt.ylabel('Liczba wystąpień danej liczby porównań')
        plt.xlabel('Liczba porównań')
        plt.grid(linestyle='--')
        plt.show()


class Testing:

    def __init__(self):
        pass

    def first_model(self):
        pass

    def second_model(self):
        pass


if __name__ == '__main__':
    obj = Bernoulli(0.75, 10000)
    obj.geo_generator()
    obj.histogram()
