import time
import concurrent.futures

from hashlib import md5
from random import choice


def generate_coin():
    while True:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            return f'{s} {h}'


def main():
    start_time = time.time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=60) as executor:
        f = {executor.submit(generate_coin): _ for _ in range(10)}
        for index, future in enumerate(concurrent.futures.as_completed(f), 1):
            print(f'{index} - {future.result()}')

    print(f"The execution time is {round(time.time() - start_time, 3)} seconds")


if __name__ == '__main__':
    main()
