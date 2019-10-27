import urllib.request
from urllib.parse import urlparse
import numpy as np

def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros ((size_x, size_y))
    for x in xrange(size_x):
        matrix [x, 0] = x
    for y in xrange(size_y):
        matrix [0, y] = y

    for x in xrange(1, size_x):
        for y in xrange(1, size_y):
            if seq1[x-1] == seq2[y-1]:
                matrix [x,y] = min(
                    matrix[x-1, y] + 1,
                    matrix[x-1, y-1],
                    matrix[x, y-1] + 1
                )
            else:
                matrix [x,y] = min(
                    matrix[x-1,y] + 1,
                    matrix[x-1,y-1] + 1,
                    matrix[x,y-1] + 1
                )
    print (matrix)
    return (matrix[size_x - 1, size_y - 1])

#example: get_title("https://www.nydailynews.com/news/politics/ny-trump-first-pitch-washington-nationals-world-series-20191026-o5rnjkq3trhfnpenpvah4fadtm-story.html?fbclid=IwAR1Bz7xj629rTFw8p5AaKLYSrG6SvLaAZwBNC4vTdMJ0vCyVDzawh7rCnG0")
def get_title(url):
    try:
        webpage = urllib.request.urlopen(url).read()
        title = str(webpage).split('<title>')[1].split('</title>')[0]
        return title
    except:
        return None

def get_domain(url):
    parsed_uri = urlparse(url)
    result = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
    return result

def get_weight(url, weight_dict):
    #get domain title
    source_title = get_title(get_domain(url))
    #look for the right key by getting key with min levenshtein distance
    min_distance = float('inf')
    closest_match = None
    for k in weight_dict.keys():
        temp_distance = levenshtein(source_title, k)/float(max(length(source_title), length(k)))
        if temp_distance <= min_distance:
            closest_match = k
            min_distance = temp_distance
    
    if closest_match == None or min_distance > 0.7:
        return 0.7
    else:
        return weight[closest_match]

def get_reliability_score(weight, related_weights):
    count = len(related_weights)
    average_weight = sorted(related_weights, reverse=True)[:min(10, count)]/float(min(10, count))
    return weight*0.5+average_weight*0.35+min(count, 100)*0.15