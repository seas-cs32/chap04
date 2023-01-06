### chap04/qweb2.py
import requests

def main():
    print('Searching wikipedia for "The Cat in the Hat"')

    # Highlight the 4 components of a URL for HTTP
    protocol = 'https'
    hostname = 'en.wikipedia.org'
    path = '/w/api.php'
    query = '?action=query&list=search&srsearch=The+Cat+in+the+Hat&srlimit=1&format=json'

    # Build the URL and launch a `get` request
    url = f"{protocol}://{hostname}{path}{query}"
    response = requests.get(url)

    if response.status_code == 200:
        print(f"Our request to Wikipedia succeeded!")
    else:
        print(f"Hmmm, something might have gone wrong.")

if __name__ == '__main__':
    main()