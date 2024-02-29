import re, argparse
import sys
from matplotlib import pyplot
import plistlib
import numpy as np

def findDuplicates(fileName):
    ''' Find the duplicate track in the specific file
    '''

    print('Find duplicate tracks in %s...' % fileName)

    # read in a playlist
    with open(fileName, 'rb') as f:
        plist = plistlib.load(f)

    # get the tracks from the Tracks dictionary
    tracks = plist['Tracks']

    # create a track name dictionary
    trackNames = {}

    # iterate through the tracks
    for trackId, track in tracks.items():
        try:
            name = track['Name']
            duration = track['Total Time']

            # look for existing entries
            if name in trackNames:
                # if a name and duration match, increment the count
                # round the track length to the nearest second
                if duration // 1000 == trackNames[name][0]//1000:
                    count = trackNames[name][1]
                    trackNames[name] = (duration, count + 1)
            else:
                # add dictionary entry as tuple (duration, count)
                trackNames[name] = (duration, 1)
        except:
            # ignore
            pass    
    

    # print(trackNames)

    # store duplicates as (name, count) tuples
    dups = []
    for k, v in trackNames.items():
        if v[1] > 1:
            dups.append((v[1], k))
    
    # Save duplicates to a file
    if len(dups) > 0:
        print("Found %d duplicates. Track names saved to dup.txt" % len(dups))
    else:
        print("No duplicate tracks found!")

    # print(dups)

    f = open("dups.txt", "w")
    for val in dups:
        f.write("[%d] %s \n" % (val[0], val[1]))
    f.close()


def findCommonTracks(fileNames):
    ''' Find the common tracks across multiple p-list files  
    '''

    trackNameSets = []
    for fileName in fileNames:
        # create a new set
        trackNames = set()

        # read in playlist
        with open(fileName, 'rb') as f:
            plist = plistlib.load(f)
        
        # get the tracks
        tracks = plist['Tracks']

        # iterate through the tracks
        for trackId, track in tracks.items():
            try:
                # add the track name to a set
                trackNames.add(track['Name'])
            except:
                # ignore
                pass
        
        # add to list
        trackNameSets.append(trackNames)

    # get the set of common tracks
    commonTracks = set.intersection(*trackNameSets)

    # write to file
    if len(commonTracks) > 0:
        f = open("common.txt", "w", encoding='utf-8')
        for val in commonTracks:
            s = "%s\n" % val
            f.write(s)
        f.close()
        print("%d common tracks found. Track names written to common.txt. " % len(commonTracks))
    else:
        print("No common tracks!")


# findDuplicates('maya.xml')

# print("------")

# findDuplicates('mymusic.xml')

findCommonTracks(['.\\test-data\maya.xml', '.\\test-data\\mymusic.xml'])