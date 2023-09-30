#!/usr/bin/python3


if __name__ == "__main__":
    import urllib.request
    import sys
    
    req = urllib.request.Request(sys.argv[1])
    with urllib.request.urlopen(req) as response:
        the_page = response.headers.get('X-Request-Id')
        print(the_page)
