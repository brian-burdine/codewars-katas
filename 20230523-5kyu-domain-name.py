"""
    Name: Extract the domain name from a URL
    Rank: 5 kyu
    Prompt: Write a function that when given a URL as a string,
      parses out just the domain name and returns it as a string. 
"""

# Solution

import re

def domain_name(url):
    url_ptn = re.compile(r"(?P<prtcl>[htps]*://)?(?P<pfx>www\.)?(?P<dmn>[\w-]+)(?P<top_dmn>\.[a-zA-Z.]+)")
    url_re = url_ptn.match(url)
    # print(url)
    # print(url_re.groupdict())
    return url_re.group('dmn')

"""
    start domain_name
    read url
    check for protocol (http/https ://); if it's there, ignore it
    check for prefix (e.g. www.)...ok, a little trickier
    
    A url consists of:
    (protocol)(prefix)domain name.top-level domain(path)(resource)
    or something like that.
    At it's most basic, there is a domain name, followed by a period, followed by a
        top-level domain (the top-level domain potentially containing more periods)
    The domain can be immediately proceeded by either a period or a slash
    I feel like it's going to be harder than the question is expecting if I try to do this
        without assuming that all urls use 'www' for their prefix if they have one, as much
        as that bothers me
"""