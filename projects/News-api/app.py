import requests as r
from send import send

aoi_key="0667aeb2affd48adaf530ef641041b77"
t="tesla"
url=f"https://newsapi.org/v2/everything?q={t}&from=2026-05-05&" \
    "sortBy=publishedAt&apiKey=0667aeb2affd48adaf530ef641041b77&language=en"

request=r.get(url)
content=request.json()
print(content)
body = ""
for article in content["articles"]:
    if article["title"] is not None:
        body += (
            article["title"] + "\n"
            + article["description"]
            + "\n" + article["url"] + "\n\n"
        )
send(body.encode("utf-8"))