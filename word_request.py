import requests

def request_word(word):
    try:
        headers = {
            "X-RapidAPI-Host": "wordsapiv1.p.rapidapi.com",
            "X-RapidAPI-Key": "ebfccaf907msh923517ca9d8835dp15d15fjsn4391ac7a943b"
        }
        response = requests.get("https://wordsapiv1.p.rapidapi.com/words/" + str(word), headers = headers)
        word_definitions = response.json()
        # print(word_definitions)
        try:
            word = word_definitions['word']
        except:
            print('Word not found!')
            return 1
        try:
            definition = word_definitions['results'][0]['definition']
            print('Definition:\n\t{}'.format(definition))
        except:
            print("No definition found")
        try:
            synonyms = word_definitions['results'][0]['synonyms']
            print('Synonyms:\n\t{}'.format(synonyms))
        except:
            print('No synonyms found')
        try:
            antonyms = word_definitions['results'][0]['antonyms']
            print('Antonyms:\n\t{}'.format(antonyms))
        except:
            print('No antonyms found')
    except:
        print('Word not found!')
# request_word("ability")