# -*- coding: UTF-8 -*-

##### Import
import os, sys, csv, time
from datetime import datetime
from riotwatcher import LolWatcher



##### Args & Vars
usage  = "\nUsage   :\n py %s {DIROUTPUT} {RIOTNAME} {REGION} {RIOTAPIKEY}" % sys.argv[0]
usage += "\nExample :\n py %s sampleOutput Ironmin136 kr RGAPI-975692e9-b2ef-4cb8-bb76-463a857b5bc4\n" % sys.argv[0]

if len(sys.argv) < 5:
    exit(usage)


output = sys.argv[1]
player = sys.argv[2]
region = sys.argv[3]
apiKey = sys.argv[4]

if not os.path.isdir(output):
    exit("\nError :\n DIROUTPUT not Existed.\n")



##### Main Program
TStamp = time.strftime("%Y-%m-%d_%H-%M-%S_ChampionData_", time.localtime())
output = os.path.join(output, TStamp + player + ".csv")
Search = LolWatcher(apiKey)
Niddle = Search.summoner.by_name(region, player)
Champs = Search.champion_mastery.by_summoner(region, Niddle["id"])
Fields = [
    'championId', 'championLevel', 'championPoints', 'lastPlayTime', 'championPointsSinceLastLevel',
    'championPointsUntilNextLevel', 'chestGranted', 'tokensEarned', 'summonerId',
]

'''
{
    'championId': 18, 'championLevel': 5, 'championPoints': 84886, 'lastPlayTime': 1656951884000,
    'championPointsSinceLastLevel': 63286, 'championPointsUntilNextLevel': 0, 'chestGranted': True,
    'tokensEarned': 2, 'summonerId': 'ptAEiZqqsGyOd9B4Rvo24lxA8rzGm8lQrO-l3pyrmOD3wDE'
}
'''

with open(output, 'w', encoding='utf-8-sig', newline='') as fout:
    CsvWriter = csv.DictWriter(fout, fieldnames=Fields)

    for i in Champs:
        CsvWriter.writerow(i)


print("\n### Done !!!\n File %s was saved." % output)

