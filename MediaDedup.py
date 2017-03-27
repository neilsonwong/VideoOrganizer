#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv
import os
import re

shows = {}
locations = {}
# folders = ["/home/neilson/Music", "/home/neilson/temp"]
folders = ["/home/neilson/Videos"]
conflicts = {}

#load titles into our db
with open('anime-titles.dat.gz.txt') as csvFile:
	reader = csv.DictReader(filter(lambda row: row[0]!='#', csvFile), delimiter='|')
	for row in reader:
		#do something with each row
		#print(row)
		shows[row['title']] = row['aid']


def filterSubMeta(filename):
	#[HorribleSubs] Masamune-kun no Revenge - 12 [720p].mkv

	#remove subGroup
	start = filename.find(']');
	if (start != -1):
		start += 1

	end = filename.find('[720p]')
	if (end == -1):
		end = filename.index('[1080p]')
	if (end ==  -1):
		end = filename.index('[480p]')

	if (end == -1):
		#could not strip the end, log this
		print(filename)
	else:
		return (filename[start:end]).strip()

def getTitle(stripped):
	return stripped.rstrip("- 1234567890")
def getEp(stripped):
	return stripped[stripped.rfind("-")+1:].strip()
def getAId(title):
	return shows.get(title)

def getData(filename):
	stripped = filterSubMeta(filename)
	title = getTitle(stripped)
	num = getEp(stripped)
	aid = getAId(title)
	return (aid, title, num)

def scanFolders():
	#"(\[(?P<group>[0-9a-zA-Z_]+)\])
	#[ ._-]*
	#(?P<series>.+?[ ._-].+?)\
	#[ ._-]+
	#(?P<ep>\d{1,3})
	#[ ._-]+
	#(\[|\(|[ ._])?
	#(?P<res>\d{1,3})p
	#\]
	#\.
	#(?P<format>mkv|avi|mp4|m4p|ogg|mov|mpg|mpeg)"

	patern = re.compile(r"(\[(?P<group>[0-9a-zA-Z_]+)\])[ ._-]*(?P<series>.+?[ ._-].+?)[ ._-]+(?P<ep>\d{1,3})[ ._-]+(\[|\(|[ ._])?(?P<res>\d{1,3})p\]\.(?P<format>mkv|avi|mp4|m4p|ogg|mov|mpg|mpeg)")

	#scan each of the folders, and catalogue the locations for each of the files
	for folder in folders:
		for subdir, dirs, files in os.walk(folder):
			for file in files:
				m = patern.match(file)
				if (m):
					addShow(m.group('group'), m.group('series'), m.group('ep'), m.group('res'), m.group('format'), os.path.join(subdir, file))

	return

def addShow(group, series, ep, resolution, format, path):
	#print(group)
	#print(series)
	#print(ep)
	#print(resolution)
	#print(format)
	#print

	#add to db
	if locations.get(series, None) == None:
		#create group
		locations[series] = {}

	showObj = {"group": group, "resolution": resolution, "format": format, "path": path}

	if locations.get(series).get(ep, None) == None:
		locations.get(series)[ep] = [showObj]
	else:
		locations.get(series)[ep].append(showObj)

	return

def getShow(series):

	return

def printLocations():
	for series in locations:
	    print(series)
	    for ep in locations[series]:
	    	if (len(locations[series][ep]) == 1):
		        	print("\t" + ep + " :\t" + locations[series][ep][0]['path'])
	    	else:
	    		print("\t" + ep + " :")
		    	for i, val in enumerate(locations[series][ep]):
		        	print("\t\t" + val['path'])
	return

def test():
	scanFolders()
	printLocations()


test();
