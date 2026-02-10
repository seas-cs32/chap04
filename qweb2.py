### chap04/qweb2.py
import requests

def main():
    print('Searching wikipedia for "The Cat in the Hat"')

    # Highlight the 4 components of a URL for HTTP
    protocol = 'https'
    hostname = 'en.wikipedia.org'
    path = '/w/api.php'
    query = '?action=query&list=search&srsearch=The+Cat+in+the+Hat&srlimit=1&format=json'

    # Build the URL
    url = f"{protocol}://{hostname}{path}{query}"

    # Add a field to the request header to comply with Wikipedia's Robot policy
    user_agent = {'User-Agent':'web-query-demo (https://beta.my.harvard.edu/course/COMPSCI32/2026-Spring)'}

    # Launch a `get` request
    response = requests.get(url, headers=user_agent)

    if response.status_code == 200:
        print(f"Our request to Wikipedia succeeded!")
    else:
        print(f"Hmmm, something might have gone wrong.")

if __name__ == '__main__':
    main()