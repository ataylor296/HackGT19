import urllib.request
from urllib.parse import urlparse
import numpy as np
from googlesearch import search

def levenshtein(seq1, seq2):
    size_x = len(seq1) + 1
    size_y = len(seq2) + 1
    matrix = np.zeros ((size_x, size_y))
    for x in range(size_x):
        matrix [x, 0] = x
    for y in range(size_y):
        matrix [0, y] = y

    for x in range(1, size_x):
        for y in range(1, size_y):
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
    #print (matrix)
    return (matrix[size_x - 1, size_y - 1])

#longest common substring
def LCSubStr(X, Y): 
    m = len(X)
    n = len(Y)

    LCSuff = [[0 for k in range(n+1)] for l in range(m+1)] 
      
    # To store the length of  
    # longest common substring 
    result = 0 
  
    # Following steps to build 
    # LCSuff[m+1][n+1] in bottom up fashion 
    for i in range(m + 1): 
        for j in range(n + 1): 
            if (i == 0 or j == 0): 
                LCSuff[i][j] = 0
            elif (X[i-1] == Y[j-1]): 
                LCSuff[i][j] = LCSuff[i-1][j-1] + 1
                result = max(result, LCSuff[i][j]) 
            else: 
                LCSuff[i][j] = 0
    return result

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
    if not source_title:
        return 60
    #look for the right key by getting key with min levenshtein distance
    # min_distance = float('inf')
    # closest_match = None
    # for k in weight_dict.keys():
    #     temp_distance = levenshtein(source_title, k)/float(max(len(source_title), len(k)))
    #     if temp_distance <= min_distance:
    #         closest_match = k
    #         min_distance = temp_distance
    
    # print(source_title, closest_match, min_distance)
    # if closest_match == None or min_distance > 0.90:
    #     return 0.7
    # else:
    #     return weight_dict[closest_match]['weight']

    #approach using longest common substring
    max_common_substring = 0
    closest_match = None
    for k in weight_dict.keys():
        temp_length = LCSubStr(source_title, k)
        if temp_length > max_common_substring:
            closest_match = k
            max_common_substring = temp_length

    #print(source_title, closest_match, max_common_substring)
    if closest_match == None or max_common_substring < 3:
        return 60
    else:
        return weight_dict[closest_match]['weight']

def get_search_results(title):
    if not title:
        return []
    results = []
    title = ''.join([c for c in title if c.isalpha() or c == " "])
    for url in search(title, stop=5):
        #print(url)
        results.append(url)
    #print(results)
    return results

def get_reliability_score(weight, related_weights):
    count = len(related_weights)
    if not related_weights:
        average_weight = 50
    else:
        average_weight = sum(sorted(related_weights, reverse=True)[:min(10, count)])/float(min(10, count))
    return int(weight*0.55+average_weight*0.35+(min(count, 100))/5.0*10)

def evaluate(url, weight_dict):
    weight = get_weight(url, weight_dict)
    related_weights = [get_weight(u, weight_dict) for u in get_search_results(get_title(url))]
    return get_title(url), get_reliability_score(weight, related_weights)