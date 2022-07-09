# -*- coding: UTF-8 -*-
##### Import
import os, sys, csv, time
from datetime import datetime
from riotwatcher import LolWatcher, ApiError



##### Args & Vars
if len(sys.argv) < 2:
    exit("\nUsage :\npython %s DIROUTPUT\n" % sys.argv[0])


apiKey = "RGAPI-975692e9-b2ef-4cb8-bb76-463a857b5bc4"
region = "kr"
player = "Ironmin136"



##### Main Program
idxPtr = 0
timest = time.strftime("%Y-%m-%d_%H-%M-%S_YR-ProMode_", time.localtime())
output = os.path.join(sys.argv[1], timest + player + ".csv")
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
    "首殺", "首殺助攻", "視野分數", "每分鐘視野分數", "對線視野分數",
    "拆眼數", "結束時間", "遊戲模式", "英雄等級", "KDA",
    "最大CS領先", "分鐘平均金錢", "分鐘平均傷害", "團隊傷害比", "團隊承傷比",
    "單殺數", "死亡總時長"
]

UserInfos = Search.summoner.by_name(region, player)

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
                        StrTimeP = datetime.fromtimestamp(GameData["info"]["gameStartTimestamp"]/1000.0)
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

                    try:
                        StrTimeP = datetime.fromtimestamp(GameData["info"]["gameEndTimestamp"]/1000.0)
                        UserRelates.append(StrTimeP.strftime("%Y-%m-%d_%H-%M-%S"))
                    except:
                        UserRelates.append("NULL")

                    try:
                        UserRelates.append(GameData["info"]["gameMode"])
                    except:
                        UserRelates.append("NULL")

                    try:
                        UserRelates.append(gamer["champLevel"])
                    except:
                        UserRelates.append("NULL")

                    try:
                        UserRelates.append(gamer["challenges"]["kda"])
                    except:
                        UserRelates.append("NULL")

                    try:
                        UserRelates.append(gamer["challenges"]["maxCsAdvantageOnLaneOpponent"])
                    except:
                        UserRelates.append("NULL")

                    try:
                        UserRelates.append(gamer["challenges"]["goldPerMinute"])
                    except:
                        UserRelates.append("NULL")

                    try:
                        UserRelates.append(gamer["challenges"]["damagePerMinute"])
                    except:
                        UserRelates.append("NULL")

                    try:
                        UserRelates.append(gamer["challenges"]["teamDamagePercentage"]*100)
                    except:
                        UserRelates.append("NULL")

                    try:
                        UserRelates.append(gamer["challenges"]["damageTakenOnTeamPercentage"]*100)
                    except:
                        UserRelates.append("NULL")

                    try:
                        UserRelates.append(gamer["challenges"]["soloKills"])
                    except:
                        UserRelates.append("NULL")

                    try:
                        UserRelates.append(gamer["totalTimeSpentDead"])
                    except:
                        UserRelates.append("NULL")

            for gamer in GameData["info"]["participants"]:
                if teamID == gamer["teamId"]:
                    try:
                        UserChampionNames.append(gamer["championName"])
                    except:
                        UserChampionNames.append("NULL")

                    try:
                        GoldEarneds.append(gamer["goldEarned"])
                    except:
                        GoldEarneds.append("NULL")

                    try:
                        TotalDamages.append(gamer["totalDamageDealtToChampions"])
                    except:
                        TotalDamages.append("NULL")

                    try:
                        TotalDamageTakens.append(gamer["totalDamageTaken"])
                    except:
                        TotalDamageTakens.append("NULL")
                else:
                    try:
                        OppoChampionNames.append(gamer["championName"])
                    except:
                        OppoChampionNames.append("NULL")

            CsvWriter.writerow(
                UserRelates[:2] + UserChampionNames + OppoChampionNames + UserRelates[2:7] +
                GoldEarneds + TotalDamages + TotalDamageTakens + UserRelates[7:]
            )

        idxPtr+=100

