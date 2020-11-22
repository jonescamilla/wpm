# imports for mock_generator()
import gzip
import json
# imports for test_maker()
import random
from english_200 import collection as english_200
from english_1000 import collection as english_1000

# generates a new tests based on imported words
def test_maker(test_length, collection):
    new_test = ''

    for _x in range(test_length):
        new_test += collection[random.randint(0, len(collection) - 1)] + ' '
        # remove the final space in generated test

    new_test = new_test[:-1]

    return new_test

# generate a list of mock tests and gzip for wpm application use
def mock_generator(mock_range, test_length, db):

    data = []

    for y in range(mock_range):
    # [{"author": "...", "title": "...", "text": "...", "id": ...}, ...]
        data.append([
            "jon.escamilla",
            "generated test",
            test_maker(test_length, db),
            y
        ])

    # serialize json as a formated string
    json_str = json.dumps(data) + "\n"
    json_bytes = json_str.encode('utf-8')

    # open file as a writable file
    with gzip.open('wpm/data/examples.json.gz', 'w') as orig_file:
        # write to the file with our new generated tests
        orig_file.write(json_bytes)

    # return data

mock_generator(500, 50, english_200)


# ways to integrate to typing test

    # make file to hold index state
    # invoke ever arrow click or space click to add a test to the end
        # remove mock range
        # only append to existing tests

# rewrite file every new test and display that file
    # may cause errors with previous and next tests
        # can maybe be solved by making three tests at a time
            # when next is clicked move over and generate a new test at the end
            # then delete oldest test
