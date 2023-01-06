### chap04/qweb3.py
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

    if response.status_code == 200:
        print(f"Our request to Wikipedia succeeded!")
    else:
        print(f"Hmmm, something might have gone wrong.")

if __name__ == '__main__':
    main()