#!/usr/bin/python3
"""displays the value of the X-Request-Id variable found in
the header of the response.
"""


if __name__ == "__main__":
    from requests import get
    r = get('https://alx-intranet.hbtn.io/status')
    print("Body response:")
    print("- type: {}".format(type(r)))
    print("- content: {}".format(r))
