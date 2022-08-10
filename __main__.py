from flask import Flask, redirect, request

app = Flask(__name__)

from urllib.parse import urlparse, urlunparse

FROM_DOMAIN = "resume.chancecallahan.com"
TO_DOMAIN = "www.resumonk.com/gJo0binaSmO4MZ50xDj7Dw"

@app.before_request
def redirect_to_new_domain():
    urlparts = urlparse(request.url)
    if urlparts.netloc == FROM_DOMAIN:
        urlparts_list = list(urlparts)
        urlparts_list[1] = TO_DOMAIN
        return redirect(urlunparse(urlparts_list), code=301)
