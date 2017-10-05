#!/usr/bin/env python3

# Copyright 2017 Lorenzo Mureu
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import lxml.html
import requests
import sys

XPATH_LIST_LESSON_URLS = r"//div[@id='lessonList']/ul/li/a/@href"
XPATH_LESSON_DOWNLOAD_URL = r"//a[text() = 'Video']/@href"

def _get_html(url):
    page = requests.get(url)
    html = lxml.html.fromstring(page.content)
    return html

def __url_split__(url): return url.rsplit('/', 1)
def _base_url(url): return __url_split__(url)[0]
def _filename(url): return __url_split__(url)[1]

def _url_join(a, b): return a + '/' + b

def download(lesson_url):
    html = _get_html(lesson_url)

    base_url = _base_url(lesson_url)
    download_url = html.xpath(XPATH_LESSON_DOWNLOAD_URL)[0]

    r = requests.get(_url_join(base_url, download_url), stream=True)
    print(r.url)
    # filename = _filename(r.url)
    # print(filename)
    # with open(filename, 'wb') as fd:
    #     for chunk in r.iter_content(chunk_size=128):
    #         fd.write(chunk)

def download_all(origin):
    html = _get_html(origin)
    lessons = html.xpath(XPATH_LIST_LESSON_URLS)

    baseurl = _base_url(origin)

    for url in lessons:
        if url.startswith('template_video.php?'):
            download( _url_join(baseurl, url))

if __name__ == "__main__":
    try:
        download_all(sys.argv[1])
    except IndexError:
        print("Usage: {} <URL>".format(sys.argv[0]))
        exit(1)
