import json
import unittest
import os
import requests

#
# Your name:
# Who you worked with:
#

# Make sure you create an API key at http://www.omdbapi.com/apikey.aspx
# Assign that to the variable API_KEY
API_KEY = ""

def read_cache(CACHE_FNAME):
    """
    This function reads from the JSON cache file and returns a dictionary from the cache data.
    If the file doesn’t exist, it returns an empty dictionary.
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))
    CACHE_FNAME = dir_path + '/' + "cache_movie.json"
    try:
        cache_file = open(CACHE_FNAME, 'r', encoding="utf-8") # Try to read the data from the file
        cache_contents = cache_file.read()  # If it's there, get it into a string
        CACHE_DICTION = json.loads(cache_contents) # And then load it into a dictionary
        cache_file.close() # Close the file, we're good, we got the data in a dictionary.
        return CACHE_DICTION
    except:
        CACHE_DICTION = {}
        return CACHE_DICTION

def write_cache(CACHE_FNAME, CACHE_DICT):
    """
    This function encodes the cache dictionary (CACHE_DICT) into JSON format and
    writes the JSON to the cache file (CACHE_FNAME) to save the search results.
    """
    pass

def create_request_url(title):
    """
    This function prepares and returns the request url for the API call.

    The documentation of the API parameters is at http://www.omdbapi.com/

    Make sure you provide the following parameters besides the title when preparing the request url:
    1. type: one of movie, series, episode
    2. plot: set to short
    3. r: set to json

    Example of a request URL for movie title The Dark Knight:
    http://www.omdbapi.com/?t=The Dark Knight&apikey=xxxxxx&type=movie&plot=short&r=json


    The API key has been blurred out since one shouldn't share API keys publicly
    """
    pass

def get_data_with_caching(title, CACHE_FNAME):
    """
    This function uses the passed movie title to first generate a request_url (using the create_request_url function).
    It then checks if this url is in the dictionary returned by the function read_cache.
    If the request_url exists as a key in the dictionary, it should print "Using cache for <title>"
    and return the results for that request_url.

    If the request_url does not exist in the dictionary, the function should print "Fetching data for <title>"
    and make a call to the OMDB API to get the movie data.

    If data is found for the movie, it should add them to a dictionary (key is the request_url, and value is the results)
    and write out the dictionary to a file using write_cache.

    In certain cases, the OMDB API may return a response for the request_url
    but it may not contain data for any movie: {"Response":"False","Error":"Movie not found!"}
    DO NOT WRITE SUCH DATA TO THE CACHE FILE! Print "Movie Not Found" and return None

    If there was an exception during the search (for reasons such as no network connection, etc),
    it should print out "Exception" and return None.
    """

    pass


def top_movies_rated(rated, CACHE_FNAME):
    """
    This function returns the top ten movies on the basis of the rated specified.
    For example, if it is 'Rated' = 'PG', the function will return top ten movies in a list ranked by their imdbRating
    """
    pass





#######################################
############ EXTRA CREDIT #############
#######################################
def movie_list(cost, CACHE_FNAME):
    """
    The function calls read_cache() to get the movie data stored in the cache file.   
    It analyzes the dictionary returned by read_cache() to return a list of all the movies
    that have received more than the passed in BoxOffice cost in an ascending sorted list of tuples
    """

    pass





#######################################
#### DO NOT CHANGE AFTER THIS LINE ####
#######################################

class TestHomework7(unittest.TestCase):
    def setUp(self):
        dir_path = os.path.dirname(os.path.realpath(__file__))
        self.CACHE_FNAME = dir_path + '/' + "cache_movie.json"
        self.movie_list = ["The Terminator","Monsters, Inc.", "Inside Out", 'V for Vendetta',"My Neighbor Totoro", "Coco",'WALL·E','Aladdin', "Brave", "Cinderella", "The Little Mermaid", "Up", "Frozen", "Moana", "Princess and the Frog", "Snow White and the Seven Drawfs", "Toy Story", "Toy Story 2", "Toy Story 3", "Tangled", "Mulan", "Sleeping Beauty", "The Sword in the Stone"]
        self.API_KEY = API_KEY
        self.cache = read_cache(self.CACHE_FNAME)

    def test_write_cache(self):
        dict = read_cache(self.CACHE_FNAME)
        write_cache(self.CACHE_FNAME, self.cache)
        dict2 = read_cache(self.CACHE_FNAME)
        self.assertEqual(dict2, self.cache)

    def test_create_request_url(self):
        for m in self.movie_list:
            self.assertIn("apikey={}".format(self.API_KEY),create_request_url(m))
            self.assertIn("t={}".format(m),create_request_url(m))
            self.assertIn("type=movie",create_request_url(m))
            self.assertIn("plot=short",create_request_url(m))
            self.assertIn("r=json",create_request_url(m))

    def test_get_data_with_caching(self):
        for m in self.movie_list:
            dict_returned = get_data_with_caching(m, self.CACHE_FNAME)
            if dict_returned:
                self.assertEqual(type(dict_returned), type({}))
                self.assertIn(create_request_url(m),read_cache(self.CACHE_FNAME))
            else:
                self.assertIsNone(dict_returned)
        self.assertEqual(json.loads(requests.get(create_request_url(self.movie_list[0])).text),read_cache(self.CACHE_FNAME)[create_request_url(self.movie_list[0])])

    def test_top_movie_rated(self):

        self.assertEqual(top_movies_rated("PG",self.CACHE_FNAME),['Coco', 'Up', 'Inside Out', 'Tangled', 'Moana', 'Frozen', 'Brave', 'Cinderella'])

        self.assertEqual(len(top_movies_rated("PG",self.CACHE_FNAME)),8)

        self.assertEqual(len(top_movies_rated("PG-13",self.CACHE_FNAME)), 1)

        self.assertEqual(top_movies_rated("PG-13",self.CACHE_FNAME), ['Inception'])

        self.assertEqual(top_movies_rated("G",self.CACHE_FNAME),['WALL·E', 'Toy Story', 'My Neighbor Totoro', 'Toy Story 3', 'Monsters, Inc.', 'Aladdin', 'Toy Story 2', 'The Little Mermaid', 'Mulan', 'Sleeping Beauty'])
        
        self.assertEqual(len(top_movies_rated("G",self.CACHE_FNAME)),10)

        self.assertEqual(top_movies_rated("R",self.CACHE_FNAME), ['Parasite', 'V for Vendetta', 'The Terminator'])

        self.assertEqual(top_movies_rated("R",self.CACHE_FNAME)[2],'The Terminator')


    ######## EXTRA CREDIT #########
    # Keep this commented out if you do not attempt the extra credit
    def test_movie_list(self):
        self.assertEqual(len(movie_list(500000,self.CACHE_FNAME)), 12)
        self.assertEqual(len(movie_list(300000,self.CACHE_FNAME)), 17)
        self.assertEqual(len(movie_list(75000,self.CACHE_FNAME)), 21)
        self.assertEqual(movie_list(75000,self.CACHE_FNAME)[1][0], 'Toy Story')
        self.assertEqual(movie_list(500000,self.CACHE_FNAME)[1], ('The Little Mermaid', '543479'))


def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    CACHE_FNAME = dir_path + '/' + "cache_movie.json"

    movies = ["The Terminator","Monsters, Inc.", "Inside Out", 'V for Vendetta',"My Neighbor Totoro", "Coco",'WALL·E','Aladdin', "Brave", "Cinderella", "The Little Mermaid", "Up", "Frozen", "Moana", "Princess and the Frog", "Snow White and the Seven Drawfs", "Toy Story", "Toy Story 2", "Toy Story 3", "Tangled", "Mulan", "Sleeping Beauty", "The Sword in the Stone"]
    [get_data_with_caching(movie, CACHE_FNAME) for movie in movies]
    print("________________________")
    # Fetch the data for Inception.
    # The data should be requested from the API if this is the first time you are running the program
    # or if you haven't deleted the cache!
    data1 = get_data_with_caching('Inception', CACHE_FNAME)
    data2 = get_data_with_caching('Inception', CACHE_FNAME)
    print("________________________")

    # Getting the data for Parasite
    # The data should be requested from the API if this is the first time you are running the program
    # or if you haven't deleted the cache!
    data1 = get_data_with_caching('Parasite', CACHE_FNAME)
    data2 = get_data_with_caching('Parasite', CACHE_FNAME)
    print("________________________")

    # Getting the data for Ladybird
    # The data should be requested from the API if this is the first time you are running the program
    # or if you haven't deleted the cache!
    data1 = get_data_with_caching('Ladybird', CACHE_FNAME)
    data2 = get_data_with_caching('Ladybird', CACHE_FNAME)
    print("________________________")

    print("Top movies rated PG")
    print(top_movies_rated("PG",CACHE_FNAME))
    print("________________________")

    print("Top movies rated PG-13")
    print(top_movies_rated("PG-13",CACHE_FNAME))
    print("________________________")

    # Extra Credit
    # Keep the statements commented out if you do not attempt the extra credit
    # print("EXTRA CREDIT!")
    # print("Movie list with BoxOffice cost more than $747,000")
    # print(movie_list(747000,CACHE_FNAME))
    # print("________________________")
    #
    # print("Movie list with BoxOffice cost more than $80,000")
    # print(movie_list(80000,CACHE_FNAME))
    # print("________________________")
 
if __name__ == "__main__":
    main()
    # You can comment this out to test with just the main function,
    # But be sure to uncomment it and test that you pass the unittests before you submit!
    unittest.main(verbosity=2)
