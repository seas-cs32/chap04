### chap04/qweb1.py
import requests

def main():
    print('Searching wikipedia for "The Cat in the Hat"')

    # Craft a request wikipedia will understand
    s = 'The Cat in the Hat'.replace(' ', '+')
    url = f"https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch={s}&srlimit=1&format=json"

    # Add a field to the request header to comply with Wikipedia's Robot policy
    user_agent = {'User-Agent':'web-query-demo (https://beta.my.harvard.edu/course/COMPSCI32/2026-Spring)'}

    # Send request from our computer to the one running wikipedia
    # Read the response from the wikipedia computer
    response = requests.get(url, headers=user_agent)

    # Print the answer to our question ... sorta
    if response.status_code == 200:
        print(f"Our request to Wikipedia succeeded!")
    else:
        print(f"Hmmm, something might have gone wrong.")

if __name__ == '__main__':
    main()