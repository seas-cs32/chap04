### chap04/mashup32.py -- not executable without a Wolfram Alpha dev key 
import requests
import xmltodict

def walpha(query, appid):
    print(f'Asking Wolfram|Alpha "{query}" ...')

    response = requests.get(
        'http://api.wolframalpha.com/v2/query',
        params={'input': query,
                'appid': appid,
                'podtitle': 'Result'
                }
    )
    assert response.status_code == 200

    jlike_response = xmltodict.parse(response.text)
    answer = jlike_response["queryresult"]["pod"]["subpod"]["plaintext"]
    print(f'... answered "{answer}"')
    return answer

def main():
    # Compare wikipedia's and Harvard library's knowledge base.

    # Grab Mike's Wolfram Alpha develop key
    with open('walpha-id.txt') as f:
        appid = f.readline().strip()

    h_query = 'how many books are in the harvard library'
    h_answer = walpha(h_query, appid)
    h_num, h_magnitude, h_units = h_answer.split()[0:3]

    w_query = 'how big is wikipedia'
    w_answer = walpha(w_query, appid)
    w_num, w_magnitude, w_units = w_answer.split()[0:3]

    assert h_magnitude == w_magnitude, 'fix assumption in code'
    h_num, w_num = float(h_num), float(w_num)
    if h_num > w_num:
        print(f'Harvard Library has more {h_units} ({h_num} {h_magnitude})',
              f'than Wikipedia has {w_units} ({w_num} {h_magnitude}).')
    elif h_num < w_num:
        print(f'Wikipedia has more {w_units} ({w_num} {w_magnitude})',
              f'than Harvard Library has {h_units} ({h_num} {h_magnitude}).')
    else:
        print("They're the same size ({h_units} and {w_units})!")

if __name__ == '__main__':
    main()