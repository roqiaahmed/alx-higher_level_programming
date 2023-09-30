#!/usr/bin/python3


if __name__ == "__main__":
    from urllib.request import urlopen, Request
    from urllib.parse import urlencode
    from sys import argv

    url = argv[1]
    values = {'email' : argv[2]}

    data = urlencode(values)
    data = data.encode('ascii') # data should be bytes
    req = Request(url, data)
    with urlopen(req) as response:
        head = response.headers.get('X-Request-Id')
        print(response.read().decode('utf-8'))
