#!/usr/bin/env python
# -*- coding: utf-8 -*-

import csv

shows = {}
locations = {}
folders = []

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
	#scan each of the folders, and catalogue the locations for each of the files
	
	return







def test():
	#"[HorribleSubs] Masamune-kun no Revenge - 12 [720p].mkv"
	data = getData("[HorribleSubs] Masamune-kun no Revenge - 12 [720p].mkv");
	print("Aid: " + data[0])
	print("Title: " + data[1]);
	print("Ep: " + data[2])

	data2 = getData("[HorribleSubs] 政宗くんのリベンジ - 6 [1080p].mkv");
	print("Aid: " + data2[0])
	print("Title: " + data2[1]);
	print("Ep: " + data2[2])

test();
