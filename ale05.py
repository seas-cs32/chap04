### chap04/ale05.py
import requests
import json

# Definitions for step 1. If doing the other
# steps in the problem, set STEP1 to False.
from ale05_step1 import fake_response
STEP1 = True

def main():
    print('Searching HOLLIS for "The Cat in the Hat"')

    # Concatenate the first 3 components of a URL for HTTP
    protocol = 'https'
    hostname = 'api.lib.harvard.edu'
    path = '/v2/items.json'
    url = protocol + '://' + hostname + path

    # Describe the query string as a Python dictionary
    query = {'q': 'The Cat in the Hat',
             'limit': 2
    }

    # Add a field to the request header saying what we accept
    accept = {'Accept': 'application/json'}

    response = requests.get(url, params=query, headers=accept)

    if STEP1:
        # For step 1, replace actual response with a simpler fake one
        j = fake_response
        print("fake_response =", json.dumps(j, indent=4))
    else:
        # Read the response body in JSON format and print it
        j = response.json()
        print("response.json() =", json.dumps(j, indent=4))

    print()

    if j['pagination']['numFound'] == 0:
        print('Zero results')
    else:
        # Process each returned response
        for i, item in enumerate(j['items']['mods']):
            # Print title info
            ti = item['titleInfo']
            if type(ti) == list:
                # Lots of title info; just print the first
                ti = ti[0]
            print(f"Title #{i}: ", end='')
            if 'nonSort' in ti:
                print(ti['nonSort'], end='')
            print(ti['title'])

            # STEP 1: Print author info from fake_response

            # STEP 2: Print author info from HOLLIS's real response

            # STEP 3: Print type of resource in the HOLLIS response

            # STEP 4: Print the abstract in the HOLLIS response, if it exists

if __name__ == '__main__':
    main()
