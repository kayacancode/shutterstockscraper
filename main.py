from bs4 import BeautifulSoup
import requests as rq
import os

r2 = rq.get("https://www.shutterstock.com/video/clip-9523439-simple-white-8-bit-retro-style-loading-text")
soup2 = BeautifulSoup(r2.text, "html.parser")

link = []

x = soup2.select('source[src^="https://ak.picdn.net"]')

os.mkdir('retrovideos')

# Only one for loop required, shouldn't iterate twice if not required
for index, source in enumerate(x):
    # Store the current url from the image result
    url = source["src"]
    # Check the url for screenshot before putting in the links
    if ".mp4" in url:
        link.append(source['src'])
        # Download the image
        source_data = rq.get(url).content
        # Put the image into the file
        with open("retrovideos/" + str(index + 1) + '.mp4', 'wb+') as f:
            f.write(source_data)

print(link)