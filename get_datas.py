from pantheon import pantheon
import asyncio
import TFTConstants

###############################
server = "kr"
apikey = "RGAPI-90b23334-2b95-4f70-8d19-699fa10518b8"
sleep_time = 1.21
DEBUG = False
PRINT_LOG = False
version = '<Releases/10.18>'
min_match_id = 4619651258
###############################


def requestsLog(url, status, headers):
    print(url, "DEBUG")
    print(status, "DEBUG")
    print(headers, "DEBUG")


panth = pantheon.Pantheon(server, apikey, errorHandling=True)
loop = asyncio.get_event_loop()


######## GETTING USER SUMMONER_ID #######
#########################################
async def getTFTChallengerLeague():
    try:
        data = await panth.getTFTChallengerLeague()
        await asyncio.sleep(sleep_time)
        return data
    except Exception as e:
        print(e)


async def getTFTGrandmasterLeague():
    try:
        data = await panth.getTFTGrandmasterLeague()
        await asyncio.sleep(sleep_time)
        return data
    except Exception as e:
        print(e)


async def getTFTMasterLeague():
    try:
        data = await panth.getTFTMasterLeague()
        await asyncio.sleep(sleep_time)
        return data
    except Exception as e:
        print(e)


#########################################
#########################################


######## GETTING PUUID, MATCH_ID AND MATCH INFO ########
########################################################
async def getTFTSummonerPUUID(summoner_id):
    try:
        data = await panth.getTFTSummoner(summoner_id)
        await asyncio.sleep(sleep_time)
        return data["puuid"]
    except Exception as e:
        print(e)


async def getTFTmatchIds(puuid):
    try:
        data = await panth.getTFTMatchlist(puuid)
        await asyncio.sleep(sleep_time)
        return data
    except Exception as e:
        print(e)


async def getTFTmatchInfo(match_id):
    try:
        data = await panth.getTFTMatch(match_id)
        await asyncio.sleep(sleep_time)
        return data
    except Exception as e:
        print(e)


########################################################
########################################################


# USING TXT FILE BECAUSE OF API REQUEST RATE LIMIT
##################################################
def make_summoner_ids_txt():
    print("make_summoner_ids_txt working...")
    if DEBUG:
        output = open("_tmp_summoner_id.txt", "w")
    else:
        output = open("_summoner_id.txt", "w")
    try:
        challenger = loop.run_until_complete(getTFTChallengerLeague())["entries"]
        grandmaster = loop.run_until_complete(getTFTGrandmasterLeague())["entries"]
        master = loop.run_until_complete(getTFTMasterLeague())["entries"]

        for data in challenger:
            output.write(data["summonerId"] + '\n')
        for data in grandmaster:
            output.write(data["summonerId"] + '\n')
        if not DEBUG:
            for data in master:
                output.write(data["summonerId"] + '\n')
    except Exception as e:
        print(e)
    output.close()


def make_puuids_txt():
    print("make_puuids_txt working...")
    cnt = 0
    try:
        if DEBUG:
            summoner_id_file = open("_tmp_summoner_id.txt", "r")
            print("debuging mode... from make_puuids_txt")
        else:
            summoner_id_file = open("_summoner_id.txt", "r")
        summoner_id_data = summoner_id_file.readline()
    except Exception as e:
        print(e)
        print("_making summoner_ids.txt...")
        make_summoner_ids_txt()

        if DEBUG:
            summoner_id_file = open("_tmp_summoner_id.txt", "r")
        else:
            summoner_id_file = open("_summoner_id.txt", "r")
        summoner_id_data = summoner_id_file.readline()

    if DEBUG:
        output = open("_tmp_puuids.txt", "w")
    else:
        output = open("_puuids.txt", "w")
    while summoner_id_data != "":
        cnt += 1
        print(cnt, "from make_puuids_txt")
        summoner_id = summoner_id_data[:-1]
        output.write(loop.run_until_complete(getTFTSummonerPUUID(summoner_id)) + "\n")
        summoner_id_data = summoner_id_file.readline()
    summoner_id_file.close()
    output.close()


def make_match_ids_txt():
    cnt = 0
    print("make_match_ids_txt working...")
    try:
        if DEBUG:
            puuid_file = open("_tmp_puuids.txt", "r")
        else:
            puuid_file = open("_puuids.txt", "r")
        puuid_data = puuid_file.readline()
    except Exception as e:
        print(e)
        print("_making _puuids.txt... from make_match_ids_txt")
        make_puuids_txt()

        if DEBUG:
            puuid_file = open("_tmp_puuids.txt", "r")
        else:
            puuid_file = open("_puuids.txt", "r")
        puuid_data = puuid_file.readline()

    match_id_set = set()
    while puuid_data != "":
        cnt += 1
        print(cnt, "from make_match_ids_txt")
        puuid = puuid_data[:-1]
        match_id_list = loop.run_until_complete(getTFTmatchIds(puuid))
        for match_id in match_id_list:
            tmp_match_id_int = int(match_id[3:])
            if tmp_match_id_int > min_match_id:
                match_id_set.add(match_id)
        puuid_data = puuid_file.readline()
    puuid_file.close()

    if DEBUG:
        output = open("_tmp_match_ids.txt", "w")
    else:
        output = open("_match_ids.txt", "w")
    for data in match_id_set:
        output.write(data + "\n")
    output.close()


##################################################
##################################################

def make_meta_dict():
    output = {}
    for meta in TFTConstants.Deck.Meta_name:
        output[meta] = {"win": 0, "top4": 0, "rank_sum": 0, "game_cnt": 0, "completed_cnt": 0, "completed_win": 0, "completed_top4": 0, "completed_rank_sum": 0}
    return output


def make_champion_list_for_item():
    output = {}
    for champ in TFTConstants.champion_list:
        output[champ["championId"]] = {}
    return output


class MatchInfo:
    # each champion's best item
    Which_item_favored = make_champion_list_for_item()
    Statistics = make_meta_dict()

    def __init__(self, info):
        self.version = info["game_version"]
        self.participants = info["participants"]
        self.variation = info["game_variation"]


def get_part_match_info(start, end, min_match_id: int):
    game_counted = 0
    try:
        if DEBUG:
            match_ids_file = open("_tmp_match_ids.txt", "r")
        else:
            match_ids_file = open("_match_ids.txt", "r")
        match_id_data = match_ids_file.readline()
    except Exception as e:
        print(e)
        print("_making _match_ids.txt... from get_match_info")
        make_match_ids_txt()

        if DEBUG:
            match_ids_file = open("_tmp_match_ids.txt", "r")
        else:
            match_ids_file = open("_match_ids.txt", "r")
        match_id_data = match_ids_file.readline()

    for i in range(start - 1):
        if match_ids_file.readline() == "":
            return
    file_idx = start

    while file_idx <= end:
        if match_id_data == "":
            break

        match_id = match_id_data[:-1]
        match_id_int = eval(match_id[3:])

        if min_match_id > match_id_int:
            match_id_data = match_ids_file.readline()
            file_idx += 1
            continue

        match_id_data = match_ids_file.readline()
        file_idx += 1
        # catch exceptions
        info = None
        try:
            info = loop.run_until_complete(getTFTmatchInfo(match_id))["info"]
        except Exception as e:
            print(e)
            continue

        # version checking
        if info["game_version"][-len(version):] != version:
            min_match_id = match_id_int
            print("LOG: min_match_id update", min_match_id)
            print(info["game_version"])
            continue
        # remove noise
        if info["game_length"] == 0:
            continue

        game_counted += 1
        match_info = MatchInfo(info)
        for participant in match_info.participants:
            deck = TFTConstants.Deck(participant)
            units = participant["units"]
            if len(units) == 0:
                continue
            meta, similarity = deck.define_meta()

            # updating MatchInfo.Statistics
            if meta != "etc":
                MatchInfo.Statistics[meta]["game_cnt"] += 1
                rank = participant["placement"]
                MatchInfo.Statistics[meta]["rank_sum"] += rank
                if rank == 1:
                    MatchInfo.Statistics[meta]["win"] += 1
                if rank <= 4:
                    MatchInfo.Statistics[meta]["top4"] += 1
                if deck.is_accomplished:
                    MatchInfo.Statistics[meta]["completed_cnt"] += 1
                    MatchInfo.Statistics[meta]["completed_rank_sum"] += rank
                    if rank == 1:
                        MatchInfo.Statistics[meta]["completed_win"] += 1
                    if rank <= 4:
                        MatchInfo.Statistics[meta]["completed_top4"] += 1

            # updating MatchInfo.Which_item_favored
            for unit in units:
                cnt = len(unit["items"])
                character_id = unit["character_id"]
                for i in range(cnt):
                    if unit["items"][i] in MatchInfo.Which_item_favored[character_id]:
                        MatchInfo.Which_item_favored[character_id][unit["items"][i]] += 1
                    else:
                        MatchInfo.Which_item_favored[character_id][unit["items"][i]] = 1
            if PRINT_LOG:
                if similarity != 0:
                    print(meta, similarity)
                    print("is accomplished: ", deck.is_accomplished)
                    print("player's rank: ", participant["placement"])

        # LOG
        print("checked games:", game_counted)

    match_ids_file.close()
    # print(MatchInfo.Which_item_favored)
    # print(MatchInfo.Statistics)


def get_match_info(n=9, steps=1000, saved_instance=[], saved_n=0, min_match_id=0):
    match_info = MatchInfo({"game_version": '', "participants": '', "game_variation": ''})
    if len(saved_instance) != 0:
        MatchInfo.Which_item_favored = saved_instance[0]
        MatchInfo.Statistics = saved_instance[1]
        print("continuing...")

    if n < saved_n:
        print("please check value of n")
        return
    for i in range(saved_n, n):
        print("part" + str(i))
        get_part_match_info(i*steps + 1, i*steps + steps, min_match_id)
        print(MatchInfo.Which_item_favored)
        print(MatchInfo.Statistics)
