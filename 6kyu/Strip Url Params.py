# Strip Url Params
#
# https://www.codewars.com/kata/51646de80fd67f442c000013
#
# Complete the method so that it does the following:
# Removes any duplicate query string parameters from the url (the first occurence should be kept)
# Removes any query string parameters specified within the 2nd argument (optional array)
# Examples:
# strip_url_params('www.codewars.com?a=1&b=2&a=2') == 'www.codewars.com?a=1&b=2'
# strip_url_params('www.codewars.com?a=1&b=2&a=2', ['b']) == 'www.codewars.com?a=1'
# strip_url_params('www.codewars.com', ['b']) == 'www.codewars.com'

def strip_url_params(url, params_to_strip=None):
    lst = url.split("&")
    parameters = []
    if "?" in url:
        parameters.append(url[url.index("?") + 1])
        if params_to_strip is not None and parameters[0] in params_to_strip:
            return url[0:url.index("?")]
    if params_to_strip:
        parameters += params_to_strip
    for i in range(1, len(lst)):
        if lst[i][0] in parameters:
            lst = lst[0:i]
            break
    return "&".join(lst)

# Best practice and clever solution:
#
# import urlparse
# import urllib
#
#
# def strip_url_params(url, strip=None):
#     if not strip: strip = []
#
#     parse = urlparse.urlparse(url)
#     query = urlparse.parse_qs(parse.query)
#
#     query = {k: v[0] for k, v in query.iteritems() if k not in strip}
#     query = urllib.urlencode(query)
#     new = parse._replace(query=query)
#
#     return new.geturl()
