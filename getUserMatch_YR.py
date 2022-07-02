# -*- coding: UTF-8 -*-
##### Import
import os, sys, csv, time
from datetime import datetime
from riotwatcher import LolWatcher, ApiError



##### YR Requirement
''' [ *() = (TOP, JUNGLE, MIDDLE, BOTTOM, UTILITY) ]
"individualPosition", "gameStarttimeTSamp", "championName *(Nmain)", "championName *(Oppo)", "timePlayed"
"win", "kills", "deaths", "assists", "goldEarned *(Nmain)"
"totalDamageDealtToChampions *(Nmain)", "totalDamageTaken *(Nmain)", "controlWardsPlaced", "teamId", "teamBaronKills"
"dragonTakedowns", "teamRiftHeraldKills", "hadAfkTeammate", "laneMinionsFirst10Minutes", "killParticipation"
"firstBloodKill", "firstBloodAssist", "visionScore", "visionScorePerMinute", "visionScoreAdvantageLaneOpponent"
"wardsKilled"
'''



##### Args & Vars
usage  = "\nUsage   :\n python %s {DIROUTPUT} {RIOTNAME} {REGION} {RIOTAPIKEY}" % sys.argv[0]
usage += "\nExample :\n python %s OutpurDir Ironmin136 kr RGAPI-975692e9-b2ef-4cb8-bb76-463a857b5bc4\n" % sys.argv[0]
if len(sys.argv) < 5:
    exit(usage)


output = sys.argv[1]
player = sys.argv[2]
region = sys.argv[3]
apiKey = sys.argv[4]

if not os.path.isdir(output):
    exit("\nError :\n DIROUTPUT not Existed.\n")



##### Main Program
idxPtr = 0
timeTS = time.strftime("%Y-%m-%d_%H-%M-%S_YR-NorMode_", time.localtime())
output = os.path.join(output, timeTS + player + ".csv")
Search = LolWatcher(apiKey)
Fields = [
    "線路", "開始時間", "同隊-TOP", "同隊-JUNGLE", "同隊-MIDDLE",
    "同隊-BOTTOM", "同隊-UTILITY", "敵隊-TOP", "敵隊-JUNGLE", "敵隊-MIDDLE",
    "敵隊-BOTTOM", "敵隊-UTILITY", "遊戲時長", "勝負", "擊殺",
    "死亡", "助攻", "經濟-TOP", "經濟-JUNGLE", "經濟-MIDDLE",
    "經濟-BOTTOM", "經濟-UTILITY", "傷害-TOP", "傷害-JUNGLE", "傷害-MIDDLE",
    "傷害-BOTTOM", "傷害-UTILITY", "承傷-TOP", "承傷-JUNGLE", "承傷-MIDDLE",
    "承傷-BOTTOM", "承傷-UTILITY", "放眼數", "對伍ID", "團隊巴龍數",
    "團隊龍種數", "預示者數", "同隊掛機玩家", "前10分鐘CS", "擊殺參與率",
    "首殺", "首殺助攻", "視野分數", "每分鐘視野分數", "對線視野分數", "拆眼數"
]


try:
    UserInfos = Search.summoner.by_name(region, player)
except:
    exit("\nError :\n Riot Token was Expired. Please refresh it.\n")


with open(output, 'w', encoding='utf-8-sig') as fout:
    CsvWriter = csv.writer(fout)
    CsvWriter.writerow(Fields)
    while True:
        try:
            UserGames = Search.match.matchlist_by_puuid(region, UserInfos['puuid'], start=idxPtr, count=100)
        except:
            exit()

        for game in UserGames:
            time.sleep(1)
            teamID, UserRelates, UserChampionNames, OppoChampionNames = 0, [], [], []
            GoldEarneds, TotalDamages, TotalDamageTakens = [], [], []
            GameData = Search.match.by_id(region, game)

            print(GameData['metadata']['matchId'])

            for gamer in GameData["info"]["participants"]:
                if gamer["puuid"] == UserInfos['puuid']:
                    teamID = gamer["teamId"]

                    try:
                        UserRelates.append(gamer["individualPosition"])
                    except:
                        UserRelates.append("NULL")

                    try:
                        StrTimeP = datetime.fromtimeTSamp(GameData["info"]["gameStarttimeTSamp"]/1000.0)
                        UserRelates.append(StrTimeP.strftime("%Y-%m-%d_%H-%M-%S"))
                    except:
                        UserRelates.append("NULL")

                    try:
                        UserRelates.append(gamer["timePlayed"])
                    except:
                        UserRelates.append("NULL")

                    try:
                        UserRelates.append(gamer["win"])
                    except:
                        UserRelates.append("NULL")

                    try:
                        UserRelates.append(gamer["kills"])
                    except:
                        UserRelates.append("NULL")

                    try:
                        UserRelates.append(gamer["deaths"])
                    except:
                        UserRelates.append("NULL")

                    try:
                        UserRelates.append(gamer["assists"])
                    except:
                        UserRelates.append("NULL")

                    try:
                        UserRelates.append(gamer["challenges"]["controlWardsPlaced"])
                    except:
                        UserRelates.append("NULL")

                    try:
                        UserRelates.append(gamer["teamId"])
                    except:
                        UserRelates.append("NULL")

                    try:
                        UserRelates.append(gamer["challenges"]["teamBaronKills"])
                    except:
                        UserRelates.append("NULL")

                    try:
                        UserRelates.append(gamer["challenges"]["dragonTakedowns"])
                    except:
                        UserRelates.append("NULL")

                    try:
                        UserRelates.append(gamer["challenges"]["teamRiftHeraldKills"])
                    except:
                        UserRelates.append("NULL")

                    try:
                        UserRelates.append(gamer["challenges"]["hadAfkTeammate"])
                    except:
                        UserRelates.append("NULL")

                    try:
                        UserRelates.append(gamer["challenges"]["laneMinionsFirst10Minutes"])
                    except:
                        UserRelates.append("NULL")

                    try:
                        UserRelates.append(gamer["challenges"]["killParticipation"])
                    except:
                        UserRelates.append("NULL")

                    try:
                        UserRelates.append(gamer["firstBloodKill"])
                    except:
                        UserRelates.append("NULL")

                    try:
                        UserRelates.append(gamer["firstBloodAssist"])
                    except:
                        UserRelates.append("NULL")

                    try:
                        UserRelates.append(gamer["visionScore"])
                    except:
                        UserRelates.append("NULL")

                    try:
                        UserRelates.append(gamer["challenges"]["visionScorePerMinute"])
                    except:
                        UserRelates.append("NULL")

                    try:
                        UserRelates.append(gamer["challenges"]["visionScoreAdvantageLaneOpponent"])
                    except:
                        UserRelates.append("NULL")

                    try:
                        UserRelates.append(gamer["wardsKilled"])
                    except:
                        UserRelates.append("NULL")

            for gamer in GameData["info"]["participants"]:
                if teamID == gamer["teamId"]:
                    try:
                        UserChampionNames.append(gamer["championName"])
                    except:
                        UserChampionNames.append("NULL")
                else:
                    try:
                        OppoChampionNames.append(gamer["championName"])
                    except:
                        OppoChampionNames.append("NULL")

            for gamer in GameData["info"]["participants"]:
                if teamID == gamer["teamId"]:
                    try:
                        GoldEarneds.append(gamer["goldEarned"])
                    except:
                        GoldEarneds.append("NULL")

            for gamer in GameData["info"]["participants"]:
                if teamID == gamer["teamId"]:
                    try:
                        TotalDamages.append(gamer["totalDamageDealtToChampions"])
                    except:
                        TotalDamages.append("NULL")

            for gamer in GameData["info"]["participants"]:
                if teamID == gamer["teamId"]:
                    try:
                        TotalDamageTakens.append(gamer["totalDamageTaken"])
                    except:
                        TotalDamageTakens.append("NULL")

            CsvWriter.writerow(
                UserRelates[:2] + UserChampionNames + OppoChampionNames + UserRelates[2:7] +
                GoldEarneds + TotalDamages + TotalDamageTakens + UserRelates[7:]
            )

        idxPtr+=100


print("\n### Done !!!\n File %s was saved." % output)

