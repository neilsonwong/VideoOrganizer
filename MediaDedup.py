#load show titles db

import csv

shows = {}
locations = {}

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
	return stripped[stripped.rfind("-")+1:].strip();

stripper = filterSubMeta("[HorribleSubs] Masamune-kun no Revenge - 12 [720p].mkv")
tit = getTitle(stripper)
num = getEp(stripper)
print(tit + " ep:" + num)