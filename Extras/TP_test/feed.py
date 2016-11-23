import feedparser
url = 'http://www.telam.com.ar/rss2/ultimasnoticias.xml'

# first request
feed = feedparser.parse(url)
for k, v in feed.items():
    print(k, v)

# store the etag and modified
last_etag = feed.etag
print(last_etag)
last_modified = feed.modified
print(last_modified)

# check if new version exists
feed_update = feedparser.parse(url, etag=last_etag, modified=last_modified)

# if feed_update.status == 304:
#     # no changes