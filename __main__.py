from word_request import request_word

if __name__ == "__main__":
    continue_search = True
    print('Welcome to your personal Thesaurus!')
    while continue_search:
        word = str(input("Enter word to search (-1 to leave): "))
        if word == '-1':
            print('Thank you for using our service')
            break
        else:
            request_word(word)
