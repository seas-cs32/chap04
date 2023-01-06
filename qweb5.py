### chap04/qweb5.py
import requests

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

    # Print the response headers with a line per key
    print("response.headers =")
    for key, value in response.headers.items():
        print(f"    {key}: {value}")

    # This is how we can access one of the keys
    print("Content-Type:", response.headers['Content-Type'])

if __name__ == '__main__':
    main()