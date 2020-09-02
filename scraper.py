import requests
from bs4 import BeautifulSoup
import re
import argparse

def scrapeDetails(paramter):
    header={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36'}
    result = requests.get("https://www.investing.com/", headers = header)
    c = result.content
    soup = BeautifulSoup(c, features="lxml")
    url = '/commodities/' + paramter + '-streaming-chart'
    samples = soup.find_all(attrs={'data-pair_url': url})
    samples = remove_html_markup(str(samples))
    return samples

def remove_html_markup(s):
    tag = False
    quote = False
    out = ""
    final = []
    for c in s:
        if c == '<' and not quote:
            tag = True
        elif c == '>' and not quote:
            if out:
                final.append(out)
            out = ""
            tag = False
        elif (c == '"' or c == "'") and tag:
            quote = not quote
        elif not tag:
            out = out + c
    return final[2:-1]