# imports
import hashlib
import time
import random
import itertools

def create_hash(text):
    '''create_hash(str text) --> bytes
    Create a sha256 has of given text'''
    orig_hash = hashlib.sha256()        # create a hash
    orig_hash.update(text.encode())     # hash the text
    return orig_hash.digest()           # return the bytes object from the hash

def break_hash(orig_hash, text_len):
    '''break_hash(bytes orig_hash, int text_len) --> [bool broken, time length]
    brute force a hash given the length of the original plaintext and the bytes object'''
    alphabet = [char for char in 'abcdefghijklmnopqrstuvwxyz']      # make alphabet list
    combos = list(itertools.combinations(alphabet, text_len))       # find all combos of this list of a given length
    options = [''.join(combo) for combo in combos]                  # make these options into strings
    broken = False
    start = time.perf_counter()                                     # start timer
    for option in options:                                          # try each option
        # start = time.perf_counter()
        test_hash = hashlib.sha256()
        test_hash.update(option.encode())                           # encode the option as a hash
        if test_hash.digest() == orig_hash:                         # check if the hash matches the hash given
            length = time.perf_counter() - start                    # if so, you've broken the hash. stop timer
            broken = True 
            break
    if broken == False:
        length = time.perf_counter() - start
    return [broken, length]                                         # return True if it worked, False if not (something happened) as well as how long it took

def time_break(strings, text_len, tests=-1):
    '''time_break(list strings, int text_len, [int tests])
    Time how long it takes, on average, to break a string of a given length.'''
    times = []
    all_data = {}
    if tests == -1:                                                 # if tests = -1, then just do all the strings given
        selected_strings = strings
    else:
        selected_strings = [random.choice(strings) for i in range(tests)]   # otherwise, randomly select the given number of tests
    for string in selected_strings:                                 # for every string, test how long it takes to break it
        orig = create_hash(string)
        data = break_hash(orig, text_len)
        if data[0] == True:                                         # if we were able to break it (meaning there were no errors)
            times.append(data[1])                                   # add the times to our data
            all_data[string] = data[1]                              # and note the string we used
    try:                                                            # try to return the average time. if it throws an error, let us know.
        return (sum(times)/tests), all_data
    except Exception as e:
        print('Times = {}'.format(times))
        print('strings: {}'.format(strings))
        raise e

def test_time(n, tests=1):                                          # find out how long it takes to brute force hashes up to length n
    alphabet = [char for char in 'abcdefghijklmnopqrstuvwxyz']
    for i in range(1, n+1):                                         # for each length, get all possible string combos, and then get the average time to break those combos
        combos = list(itertools.combinations(alphabet, i))
        options = [''.join(combo) for combo in combos]
        average, data = time_break(options, i, tests=tests)
        print('Number of characters: \t {0} \t Average time: \t {1}'.format(i, average))    # print results

test_time(30, tests=30)
