### chap04/qweb8.py
import requests
import webbrowser

def h_lib(book):
    # Concatenate the first 3 components of a URL for HTTP
    protocol = 'http'
    hostname = 'api.lib.harvard.edu'
    path = '/v2/items.json'
    url = protocol + '://' + hostname + path

    # Describe the query string as a Python dictionary
    query = {'q': book, 'limit': 5}

    # Add a field to the request header saying what we accept
    accept = {'Accept': 'application/json'}

    response = requests.get(url, params=query, headers=accept)

    # Return a list of matching items from the received response
    if response.json()['pagination']['numFound'] == 0:
        return []
    else:
        return response.json()['items']['mods']

def match(item, desired_book):
    if type(item['titleInfo']) == list:
        ti = item['titleInfo'][0]
    else:
        ti = item['titleInfo']
    return ti['title'].lower() == desired_book.lower()

def get_url(items):
    if type(items) == list:
        for item in items:
            if '@otherType' not in item or item['@otherType'] != 'HOLLIS record':
                continue
            return item['location']['url']
    else:
        return items['location']['url']

def main():
    desired_book = input("What's the title of your desired book? ")

    print(f'Searching HOLLIS for "{desired_book}"')
    items = h_lib(desired_book)

    # Launch a browser window if we find the desired book
    for item in items:
        if match(item, desired_book):
            # Grab this book's HOLLIS url
            hollis_url = get_url(item['relatedItem'])

            # Open a browser window to the appropriate HOLLIS page
            browser = webbrowser.get('safari')
            browser.open(hollis_url)
            break
    else:
        print("Your desired book isn't in HOLLIS.")

if __name__ == '__main__':
    main()