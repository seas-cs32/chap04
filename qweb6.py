### chap04/qweb6.py
import requests
import json

def main():
    print('Searching wikipedia for "The Cat in the Hat"')

    # Concatenate the first 3 components of a URL for HTTP
    protocol = 'https'
    hostname = 'en.wikipedia.org'
    path = '/w/api.php'
    url = protocol + '://' + hostname + path

    # Describe the query string as a Python dictionary
    query = {'action': 'query',
             'list': 'search',
             'srsearch': 'The Cat in the Hat',
             'srlimit': 1,
             'format': 'json'
    }

    response = requests.get(url, params=query)

    # Print the response body directly
    print("response.text =", response.text)

    print()

    # Read the response body in JSON format and print it
    j = response.json()
    print("response.json() =", json.dumps(j, indent=4))

    print()

    # Print just the title from the JSON-structured response
    print("Title =", j['query']['search'][0]['title'])

if __name__ == '__main__':
    main()