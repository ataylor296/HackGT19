from googlesearch import search

searching = input("input: ")  
print(searching)  

results = []

for url in search('searching', stop=30):
    #print(url)
    results.append(url)
#print(results)
