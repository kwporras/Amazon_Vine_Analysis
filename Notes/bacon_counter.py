# Import mrjob
from mrjob.job import MRJob

# Create class which inherits, o takes properties, from the MRJob class
class Bacon_count(MRJob):
    # mapper function that assign the input to key-value pairs:
    def mapper(self, _, line):
        # split method to break the test into a list of words
        for word in line.split():
            # convert each word to lowercase
            if word.lower() == "bacon":
                yield "bacon", 1

    # shuffle steop organized the key-value paris so that there's only one key for each unique key, and combines the values into a list
    def reducer(self, key, values):
        yield key, sum(values)

# run the program
if __name__ == "__main__":
   Bacon_count.run()