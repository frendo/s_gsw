#!/usr/bin/pyth n
# Program to scrap web page thinks using BeautifulSoup4 
#for tag in tags:
#    print (tag.get('href', None))

from bs4 import *
import urllib.request
import sys

def get_tags(url, tags, tag):
	
	
	with urllib.request.urlopen(url) as response:
		html = response.read() 
	soup = BeautifulSoup(html, "html.parser")
	# Retrieve all of the anchor tags
	tags = soup(tag)

	return tags

def process_urls(num_repeats, tag_pos, url, tag):

    tag_pos = tag_pos - 1 
    num_passes = -1
    tags = ''

    while num_passes < num_repeats:

        if num_passes + 1 == num_repeats:
            print ('Last URL: ', url)
        else:
            print('Retrieving: ', url)

        tags = get_tags(url,tags,tag)
        url = tags[tag_pos].get('href')
        num_passes = num_passes + 1

def main():
	
    if len(sys.argv) > 2:
        num_repeats = int(sys.argv[1])  
        tag_pos = int(sys.argv[2])  
        tag = sys.argv[3]
    else:
        num_repeats = int(input('Enter count: '))
        tag_pos = int(input('Enter position: '))
        tag = input('Enter tag: ')

    url = input('Enter URL: ')

    process_urls(num_repeats, tag_pos, url, tag)
	
if __name__ == '__main__':
  main()

# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
