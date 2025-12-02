#!/usr/bin/python3
"""
Sends a POST request to a URL with an email as a parameter
and displays the body of the response decoded in utf-8.
"""

import sys
import urllib.error
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url, data=data) as response:
	    body = reponse.read()
	    print(body.decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}") 
