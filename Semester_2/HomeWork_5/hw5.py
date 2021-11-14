from multiprocessing import Pool
from time import process_time


def factorize(*number):

    result = []
    for num in number:
        dividers = []
        for i in range(1, num+1):
            if num % i == 0:
                dividers.append(i)
        result.append(dividers)
    return result


if __name__ == '__main__':

    with Pool() as pool:
        print(pool.map(factorize, [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158,
              304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]), f'\nwith multiprocessing: {process_time()}')

    print(factorize(1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316,
          380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060), f'\nwithout multiprocessing: {process_time()}')
