'''
Use this after use get_datas.py!!!!
'''

from pantheon import pantheon
import asyncio
from get_datas import *

'''
reading _summoner_id.txt
'''
summoner_id_file = open("_tmp.txt", "r")
summoner_id_data = summoner_id_file.readline()
match_id_set = set([])
summoner_id_list = []

loop = asyncio.get_event_loop()

while (summoner_id_data != ""):
    summoner_id_list.append(summoner_id_data[:-1])
    summoner_id_data = summoner_id_file.readline()
summoner_id_file.close()

'''
'''
tmp_puuid = loop.run_until_complete(getTFTSummonerPUUID(summoner_id_list[0]))
tmp_puuid = "EJfRF3eO_82ZmeP5wpZHMtccfPpIkwojHWzh3smK4YvsTdanRne0N_gmM__8HaE8T8w69Uud_dBbew"
# tmp_matchs = loop.run_until_complete(getTFTmatchIds(tmp_puuid))
tmp_matchs = ['KR_4391738921', 'KR_4391771761', 'KR_4388279208', 'KR_4385472073', 'KR_4385345293', 'KR_4385285616',
              'KR_4379203180', 'KR_4379107186', 'KR_4374361193', 'KR_4373946085', 'KR_4373918473', 'KR_4373913076',
              'KR_4373786347', 'KR_4373761462', 'KR_4373647000', 'KR_4373469412', 'KR_4373494173', 'KR_4373421680',
              'KR_4373227671', 'KR_4373263744']
x = tmp_matchs[1]
tmp_matchdata = loop.run_until_complete(getTFTmatchInfo(x))["info"]
print(tmp_matchdata)

