### chap04/ale05_step1.py
import json

# Fake a response from HOLLIS with minimal detail
fake_response = {
    "pagination": {
        "numFound": 610,
        "query": "q=The Cat in the Hat&limit=3",
        "limit": 3,
    },
    "items": {
        "mods": [
            {
                "titleInfo": {
                    "nonSort": "The  ",
                    "title": "annotated cat",
                },
                "name": [
                    {
                        "@type": "personal",
                        "namePart": "Nel, Philip",
                        "role": "creator",
                    },
                    {
                        "@type": "corporate",
                        "namePart": "Random House (Firm)",
                        "role": "publisher",
                    }
                ],
            },
            {
                "titleInfo": {
                    "nonSort": "The  ",
                    "title": "cat in the hat",
                },
                "name": [
                    {
                        "@type": "personal",
                        "namePart": "Seuss, Dr.",
                        "role": [
                            "creator",
                            "author",
                            "illustrator",
                        ]
                    },
                    {
                        "@type": "corporate",
                        "namePart": "Random House (Firm)",
                        "role": "publisher",
                    }
                ],
            },
            {
                "titleInfo": {
                    "title": "title with no author",
                },
            },
        ],
    },
}

def main():
    print('Printing our fake response ...')
    j = fake_response
    print("fake_response =", json.dumps(j, indent=4))

    print()

    print('How many matching results were in HOLLIS? ', end='')
    num_results = j['pagination']['numFound']
    if num_results == 1:
        print('1 result')
    else:
        print(f'{num_results} results')

if __name__ == '__main__':
    main()
