import time
import concurrent.futures

from urllib.request import Request, urlopen


def load_url(url, timeout):
    request = Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
    )
    resp = urlopen(request, timeout=timeout)
    resp.close()
    return resp.code


def main():
    links = open('res.txt', encoding='utf8').read().split('\n')

    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        future_to_url = {executor.submit(load_url, url, 60): url for url in links}
        for index, future in enumerate(concurrent.futures.as_completed(future_to_url)):
            url = future_to_url[future]
            try:
                data = future.result()
            except Exception as exc:
                print('%s - %r generated an exception: %s' % (index, url, exc))
            else:
                print('%s - %r page\'s code is %s' % (index, url, data))

    print(f"The execution time is {round(time.time() - start_time, 3)} seconds")


if __name__ == '__main__':
    main()
