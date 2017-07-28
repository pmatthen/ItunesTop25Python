import urllib, json

url = "https://rss.itunes.apple.com/api/v1/us/itunes-music/top-songs/25/explicit/json"
response = urllib.urlopen(url)
data = json.loads(response.read())

resultsList = data['feed']['results']

for index in range(len(resultsList)):
    resultsListDictionary = resultsList[index]
    print("{}. {} - {}".format((index+1), resultsListDictionary['artistName'], resultsListDictionary['name']))