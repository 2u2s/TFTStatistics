from pantheon import pantheon
import asyncio
import TFTConstants

###############################
server = "kr"
apikey = "YOUR API KEY"
sleep_time = 1.21
DEBUG = True
PRINT_LOG = False
version = 'Version 10.10.320.3039 (May 07 2020/17:23:49) [PUBLIC] <Releases/10.10>'


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
    return {
        'Reroll_Void': {"win": 0, "top4": 0, "rank_sum": 0, "game_cnt": 0, "completed_cnt": 0, "completed_win": 0, "completed_top4": 0, "completed_rank_sum": 0},
        'Reroll_Xayah': {"win": 0, "top4": 0, "rank_sum": 0, "game_cnt": 0, "completed_cnt": 0, "completed_win": 0, "completed_top4": 0, "completed_rank_sum": 0},
        'Reroll_Xayah_Fiora': {"win": 0, "top4": 0, "rank_sum": 0, "game_cnt": 0, "completed_cnt": 0, "completed_win": 0, "completed_top4": 0, "completed_rank_sum": 0},
        'Reroll_6sorcerer': {"win": 0, "top4": 0, "rank_sum": 0, "game_cnt": 0, "completed_cnt": 0, "completed_win": 0, "completed_top4": 0, "completed_rank_sum": 0},
        'Refeuling_Sona': {"win": 0, "top4": 0, "rank_sum": 0, "game_cnt": 0, "completed_cnt": 0, "completed_win": 0, "completed_top4": 0, "completed_rank_sum": 0},
        'Blaster_Brawler': {"win": 0, "top4": 0, "rank_sum": 0, "game_cnt": 0, "completed_cnt": 0, "completed_win": 0, "completed_top4": 0, "completed_rank_sum": 0},
        'Laser_Printer': {"win": 0, "top4": 0, "rank_sum": 0, "game_cnt": 0, "completed_cnt": 0, "completed_win": 0, "completed_top4": 0, "completed_rank_sum": 0},
        'Vanguard_Jhin': {"win": 0, "top4": 0, "rank_sum": 0, "game_cnt": 0, "completed_cnt": 0, "completed_win": 0, "completed_top4": 0, "completed_rank_sum": 0},
        '4Vanguard_Jhin': {"win": 0, "top4": 0, "rank_sum": 0, "game_cnt": 0, "completed_cnt": 0, "completed_win": 0, "completed_top4": 0, "completed_rank_sum": 0},
        'Cybernetics': {"win": 0, "top4": 0, "rank_sum": 0, "game_cnt": 0, "completed_cnt": 0, "completed_win": 0, "completed_top4": 0, "completed_rank_sum": 0},
        'Chrono_Kayle': {"win": 0, "top4": 0, "rank_sum": 0, "game_cnt": 0, "completed_cnt": 0, "completed_win": 0, "completed_top4": 0, "completed_rank_sum": 0},
        'High_Value': {"win": 0, "top4": 0, "rank_sum": 0, "game_cnt": 0, "completed_cnt": 0, "completed_win": 0, "completed_top4": 0, "completed_rank_sum": 0},
        'Celestial_Darius': {"win": 0, "top4": 0, "rank_sum": 0, "game_cnt": 0, "completed_cnt": 0, "completed_win": 0, "completed_top4": 0, "completed_rank_sum": 0},
        'Mech_infiltrator': {"win": 0, "top4": 0, "rank_sum": 0, "game_cnt": 0, "completed_cnt": 0, "completed_win": 0, "completed_top4": 0, "completed_rank_sum": 0},
        'Rebel_Demolitionist': {"win": 0, "top4": 0, "rank_sum": 0, "game_cnt": 0, "completed_cnt": 0, "completed_win": 0, "completed_top4": 0, "completed_rank_sum": 0},
        'StarGuardian_Sorcerer': {"win": 0, "top4": 0, "rank_sum": 0, "game_cnt": 0, "completed_cnt": 0, "completed_win": 0, "completed_top4": 0, "completed_rank_sum": 0},
        'DarkStar_Sniper': {"win": 0, "top4": 0, "rank_sum": 0, "game_cnt": 0, "completed_cnt": 0, "completed_win": 0, "completed_top4": 0, "completed_rank_sum": 0},
        'Health_Deck': {"win": 0, "top4": 0, "rank_sum": 0, "game_cnt": 0, "completed_cnt": 0, "completed_win": 0, "completed_top4": 0, "completed_rank_sum": 0}
    }


class MatchInfo:
    # each champion's best item
    Which_item_favored = {
        "TFT3_Ahri": {},
        "TFT3_Annie": {},
        "TFT3_Ashe": {},
        "TFT3_AurelionSol": {},
        "TFT3_Blitzcrank": {},
        "TFT3_Caitlyn": {},
        "TFT3_ChoGath": {},
        "TFT3_Darius": {},
        "TFT3_Ekko": {},
        "TFT3_Ezreal": {},
        "TFT3_Fiora": {},
        "TFT3_Fizz": {},
        "TFT3_Gangplank": {},
        "TFT3_Graves": {},
        "TFT3_Irelia": {},
        "TFT3_JarvanIV": {},
        "TFT3_Jayce": {},
        "TFT3_Jhin": {},
        "TFT3_Jinx": {},
        "TFT3_KaiSa": {},
        "TFT3_Karma": {},
        "TFT3_Kassadin": {},
        "TFT3_Kayle": {},
        "TFT3_KhaZix": {},
        "TFT3_Leona": {},
        "TFT3_Lucian": {},
        "TFT3_Lulu": {},
        "TFT3_Lux": {},
        "TFT3_Malphite": {},
        "TFT3_MasterYi": {},
        "TFT3_MissFortune": {},
        "TFT3_Mordekaiser": {},
        "TFT3_Neeko": {},
        "TFT3_Poppy": {},
        "TFT3_Rakan": {},
        "TFT3_Rumble": {},
        "TFT3_Shaco": {},
        "TFT3_Shen": {},
        "TFT3_Sona": {},
        "TFT3_Soraka": {},
        "TFT3_Syndra": {},
        "TFT3_Thresh": {},
        "TFT3_TwistedFate": {},
        "TFT3_VelKoz": {},
        "TFT3_Vi": {},
        "TFT3_WuKong": {},
        "TFT3_Xayah": {},
        "TFT3_Xerath": {},
        "TFT3_XinZhao": {},
        "TFT3_Yasuo": {},
        "TFT3_Ziggs": {},
        "TFT3_Zoe": {}
    }
    # each galaxy's deck statistics
    Galaxy_statistics = {
        "TFT3_GameVariation_BigLittleLegends": make_meta_dict(),
        "TFT3_GameVariation_Bonanza": make_meta_dict(),
        "TFT3_GameVariation_FourCostFirstCarousel": make_meta_dict(),
        "TFT3_GameVariation_FreeNeekos": make_meta_dict(),
        "TFT3_GameVariation_FreeRerolls": make_meta_dict(),
        "TFT3_GameVariation_MidGameFoN": make_meta_dict(),
        "TFT3_GameVariation_None": make_meta_dict(),
        "TFT3_GameVariation_StartingItems": make_meta_dict(),
        "TFT3_GameVariation_TwoStarCarousels": make_meta_dict()
    }

    def clear_up_which_item_favored(self):
        self.Which_item_favored = {
            "TFT3_Ahri": {},
            "TFT3_Annie": {},
            "TFT3_Ashe": {},
            "TFT3_AurelionSol": {},
            "TFT3_Blitzcrank": {},
            "TFT3_Caitlyn": {},
            "TFT3_ChoGath": {},
            "TFT3_Darius": {},
            "TFT3_Ekko": {},
            "TFT3_Ezreal": {},
            "TFT3_Fiora": {},
            "TFT3_Fizz": {},
            "TFT3_Gangplank": {},
            "TFT3_Graves": {},
            "TFT3_Irelia": {},
            "TFT3_JarvanIV": {},
            "TFT3_Jayce": {},
            "TFT3_Jhin": {},
            "TFT3_Jinx": {},
            "TFT3_KaiSa": {},
            "TFT3_Karma": {},
            "TFT3_Kassadin": {},
            "TFT3_Kayle": {},
            "TFT3_KhaZix": {},
            "TFT3_Leona": {},
            "TFT3_Lucian": {},
            "TFT3_Lulu": {},
            "TFT3_Lux": {},
            "TFT3_Malphite": {},
            "TFT3_MasterYi": {},
            "TFT3_MissFortune": {},
            "TFT3_Mordekaiser": {},
            "TFT3_Neeko": {},
            "TFT3_Poppy": {},
            "TFT3_Rakan": {},
            "TFT3_Rumble": {},
            "TFT3_Shaco": {},
            "TFT3_Shen": {},
            "TFT3_Sona": {},
            "TFT3_Soraka": {},
            "TFT3_Syndra": {},
            "TFT3_Thresh": {},
            "TFT3_TwistedFate": {},
            "TFT3_VelKoz": {},
            "TFT3_Vi": {},
            "TFT3_WuKong": {},
            "TFT3_Xayah": {},
            "TFT3_Xerath": {},
            "TFT3_XinZhao": {},
            "TFT3_Yasuo": {},
            "TFT3_Ziggs": {},
            "TFT3_Zoe": {}
        }

    def clear_up_galaxy_statistics(self):
        self.Galaxy_statistics = {
            "TFT3_GameVariation_BigLittleLegends": make_meta_dict(),
            "TFT3_GameVariation_Bonanza": make_meta_dict(),
            "TFT3_GameVariation_FourCostFirstCarousel": make_meta_dict(),
            "TFT3_GameVariation_FreeNeekos": make_meta_dict(),
            "TFT3_GameVariation_FreeRerolls": make_meta_dict(),
            "TFT3_GameVariation_MidGameFoN": make_meta_dict(),
            "TFT3_GameVariation_None": make_meta_dict(),
            "TFT3_GameVariation_StartingItems": make_meta_dict(),
            "TFT3_GameVariation_TwoStarCarousels": make_meta_dict()
        }

    def __init__(self, info):
        self.version = info["game_version"]
        self.participants = info["participants"]
        self.variation = info["game_variation"]


def get_part_match_info(start, end):
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
        info = loop.run_until_complete(getTFTmatchInfo(match_id))["info"]

        match_id_data = match_ids_file.readline()
        file_idx += 1
        if info["game_version"][:13] != version[:13]:
            continue
        game_counted += 1
        match_info = MatchInfo(info)
        for participant in match_info.participants:
            deck = TFTConstants.Deck(participant)
            units = participant["units"]
            if len(units) == 0:
                continue
            meta, similarity = deck.define_meta()

            # updating MatchInfo.Galaxy_statistics
            if meta != "etc":
                MatchInfo.Galaxy_statistics[match_info.variation][meta]["game_cnt"] += 1
                rank = participant["placement"]
                MatchInfo.Galaxy_statistics[match_info.variation][meta]["rank_sum"] += rank
                if rank == 1:
                    MatchInfo.Galaxy_statistics[match_info.variation][meta]["win"] += 1
                if rank <= 4:
                    MatchInfo.Galaxy_statistics[match_info.variation][meta]["top4"] += 1
                if deck.is_accomplished:
                    MatchInfo.Galaxy_statistics[match_info.variation][meta]["completed_cnt"] += 1
                    MatchInfo.Galaxy_statistics[match_info.variation][meta]["completed_rank_sum"] += rank
                    if rank == 1:
                        MatchInfo.Galaxy_statistics[match_info.variation][meta]["completed_win"] += 1
                    if rank <= 4:
                        MatchInfo.Galaxy_statistics[match_info.variation][meta]["completed_top4"] += 1

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
    # print(MatchInfo.Galaxy_statistics)


def get_match_info(n=9):
    match_info = MatchInfo({"game_version": '', "participants": '', "game_variation": ''})
    for i in range(n):
        print("part" + str(i))
        get_part_match_info(i * 1000 + 1, i * 1000 + 1000)
    print(match_info.Which_item_favored)
    print(match_info.Galaxy_statistics)



