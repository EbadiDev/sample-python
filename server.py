import re

def fetch_listener(event):
    url = event.request.url
    url_parts = list(urlparse(url))
    url_parts[1] = "fra.bornatejaratdeba.com" 
    url_parts[0] = "https"
    new_url = urlunparse(url_parts)
    new_request = Request(new_url, method=event.request.method,
                           headers=event.request.headers,
                           data=event.request.body,
                           cookies=event.request.cookies,
                           auth=event.request.auth,
                           allow_redirects=event.request.allow_redirects,
                           timeout=event.request.timeout,
                           verify=event.request.verify,
                           cert=event.request.cert)
    return fetch(new_request)

addEventListener("fetch", fetch_listener)
