import hashlib
import time
import random
import itertools

def create_hash(text):
    orig_hash = hashlib.sha256()
    orig_hash.update(text.encode())
    return orig_hash.digest()

def break_hash(orig_hash, text_len):
    alphabet = [char for char in 'abcdefghijklmnopqrstuvwxyz']
    combos = list(itertools.combinations(alphabet, text_len))
    options = [''.join(combo) for combo in combos]
    broken = False
    start = time.perf_counter()
    for option in options:
        # start = time.perf_counter()
        test_hash = hashlib.sha256()
        test_hash.update(option.encode())
        if test_hash.digest() == orig_hash:
            length = time.perf_counter() - start
            broken = True 
            break
    if broken == False:
        length = time.perf_counter() - start
    return [broken, length]

def time_break(strings, text_len, tests=-1):
    times = []
    all_data = {}
    if tests == -1:
        selected_strings = strings
    else:
        selected_strings = [random.choice(strings) for i in range(tests)]
    for string in selected_strings:
        orig = create_hash(string)
        data = break_hash(orig, text_len)
        if data[0] == True:
            times.append(data[1])
            all_data[string] = data[1]
    try:
        return (sum(times)/tests), all_data
    except Exception as e:
        print('Times = {}'.format(times))
        print('strings: {}'.format(strings))
        raise e

def test_time(n, tests=1):
    alphabet = [char for char in 'abcdefghijklmnopqrstuvwxyz']
    for i in range(1, n+1):
        combos = list(itertools.combinations(alphabet, i))
        options = [''.join(combo) for combo in combos]
        average, data = time_break(options, i, tests=tests)
        print('Number of characters: \t {0} \t Average time: \t {1}'.format(i, average))

test_time(30, tests=30)
