######## constants ########
###########################
trait_list = [
    {'key': 'Set3_Blademaster', 'name': 'Blademaster', 'type': 'class',
     'sets': [{'style': 'bronze', 'min': 3, 'max': 5}, {'style': 'gold', 'min': 6, 'max': 8},
              {'style': 'chromatic', 'min': 9}]},

    {'key': 'Blaster', 'name': 'Blaster', 'type': 'class',
     'sets': [{'style': 'bronze', 'min': 2, 'max': 3}, {'style': 'gold', 'min': 4}]},

    {'key': 'Set3_Brawler', 'name': 'Brawler', 'type': 'class',
     'sets': [{'style': 'bronze', 'min': 2, 'max': 3}, {'min': 4}]},

    {'key': 'Set3_Celestial', 'name': 'Celestial', 'type': 'origin',
     'sets': [{'style': 'bronze', 'min': 2, 'max': 3}, {'style': 'gold', 'min': 4, 'max': 5},
              {'style': 'chromatic', 'min': 6}]},

    {'key': 'Chrono', 'name': 'Chrono', 'type': 'origin',
     'sets': [{'style': 'bronze', 'min': 2, 'max': 3}, {'style': 'silver', 'min': 4, 'max': 5},
              {'style': 'gold', 'min': 6, 'max': 7}, {'style': 'chromatic', 'min': 8}]},

    {'key': 'Cybernetic', 'name': 'Cybernetic', 'type': 'origin',
     'sets': [{'style': 'silver', 'min': 3, 'max': 5}, {'style': 'gold', 'min': 6}]},

    {'key': 'DarkStar', 'name': 'Dark Star', 'type': 'origin',
     'sets': [{'style': 'bronze', 'min': 2, 'max': 3}, {'style': 'silver', 'min': 4, 'max': 5},
              {'style': 'gold', 'min': 6, 'max': 7}, {'style': 'chromatic', 'min': 8}]},

    {'key': 'Demolitionist', 'name': 'Demolitionist', 'type': 'class',
     'sets': [{'style': 'gold', 'min': 2}]},

    {'key': 'Infiltrator', 'name': 'Infiltrator', 'type': 'class',
     'sets': [{'style': 'bronze', 'min': 2, 'max': 3}, {'style': 'gold', 'min': 4, 'max': 5},
              {'style': 'chromatic', 'min': 6}]},

    {'key': 'ManaReaver', 'name': 'Mana-Reaver', 'type': 'class',
     'sets': [{'style': 'gold', 'min': 2}]},

    {'key': 'MechPilot', 'name': 'Mech-Pilot', 'type': 'origin',
     'sets': [{'style': 'gold', 'min': 3}]},

    {'key': 'Mercenary', 'name': 'Mercenary', 'type': 'class',
     'sets': [{'style': 'gold', 'min': 1}]},

    {'key': 'Set3_Mystic', 'name': 'Mystic', 'type': 'class',
     'sets': [{'style': 'bronze', 'min': 2, 'max': 3}, {'style': 'gold', 'min': 4}]},

    {'key': 'Protector', 'name': 'Protector', 'type': 'class',
     'sets': [{'style': 'bronze', 'min': 2, 'max': 3}, {'style': 'gold', 'min': 4, 'max': 5},
              {'style': 'chromatic', 'min': 6}]},

    {'key': 'Rebel', 'name': 'Rebel', 'type': 'origin',
     'sets': [{'style': 'bronze', 'min': 3, 'max': 5}, {'style': 'gold', 'min': 6, 'max': 8},
              {'style': 'chromatic', 'min': 9}]},

    {'key': 'Sniper', 'name': 'Sniper', 'type': 'class',
     'sets': [{'style': 'bronze', 'min': 2, 'max': 3}, {'style': 'gold', 'min': 4}]},

    {'key': 'Set3_Sorcerer', 'name': 'Sorcerer', 'type': 'class',
     'sets': [{'style': 'bronze', 'min': 2, 'max': 3}, {'style': 'silver', 'min': 4, 'max': 5},
              {'style': 'gold', 'min': 6}]},

    {'key': 'SpacePirate', 'name': 'Space Pirate', 'type': 'origin',
     'sets': [{'style': 'bronze', 'min': 2, 'max': 3}, {'style': 'gold', 'min': 4}]},

    {'key': 'StarGuardian', 'name': 'Star Guardian', 'type': 'origin',
     'sets': [{'style': 'bronze', 'min': 3, 'max': 5}, {'style': 'gold', 'min': 6}, {'style': 'chromatic', 'min': 9}]},

    {'key': 'Starship', 'name': 'Starship', 'type': 'class',
     'sets': [{'style': 'gold', 'min': 1}]},

    {'key': 'Battlecast', 'name': 'Battlecast', 'type': 'origin',
     'sets': [{'style': 'bronze', 'min': 2, 'max': 3}, {'style': 'silver', 'min': 4, 'max': 5},
              {'style': 'gold', 'min': 6, 'max': 7}, {'style': 'chromatic', 'min': 8}]},

    {'key': 'Vanguard', 'name': 'Vanguard', 'type': 'class',
     'sets': [{'style': 'bronze', 'min': 2, 'max': 3}, {'style': 'silver', 'min': 4, 'max': 5},
              {'style': 'gold', 'min': 6}]},

    {'key': 'Paragon', 'name': 'Paragon', 'type': 'class',
     'sets': [{'style': 'gold', 'min': 1}]}
]
get_trait_key_by_name = {}
for t in trait_list:
    get_trait_key_by_name[t["name"]] = t["key"]

champion_list = [
    {'name': 'Ahri', 'championId': 'TFT3_Ahri', 'cost': 2, 'traits': ['Star Guardian', 'Sorcerer']},
    {'name': 'Annie', 'championId': 'TFT3_Annie', 'cost': 2, 'traits': ['Mech-Pilot', 'Sorcerer']},
    {'name': 'Ashe', 'championId': 'TFT3_Ashe', 'cost': 3, 'traits': ['Celestial', 'Sniper']},
    {'name': 'Aurelion Sol', 'championId': 'TFT3_AurelionSol', 'cost': 5, 'traits': ['Rebel', 'Starship']},
    {'name': 'Bard', 'championId': 'TFT3_Bard', 'cost': 3, 'traits': ['Astro', 'Mystic']},
    {'name': 'Blitzcrank', 'championId': 'TFT3_Blitzcrank', 'cost': 2, 'traits': ['Chrono', 'Brawler']},
    {'name': 'Caitlyn', 'championId': 'TFT3_Caitlyn', 'cost': 1, 'traits': ['Chrono', 'Sniper']},
    {'name': "Cassiopeia", 'championId': 'TFT3_Cassiopeia', 'cost': 3, 'traits': ['Battlecast', 'Mystic']},
    {'name': 'Darius', 'championId': 'TFT3_Darius', 'cost': 2, 'traits': ['Space Pirate', 'Mana-Reaver']},
    {'name': 'Ekko', 'championId': 'TFT3_Ekko', 'cost': 5, 'traits': ['Cybernetic', 'Infiltrato']},
    {'name': 'Ezreal', 'championId': 'TFT3_Ezreal', 'cost': 3, 'traits': ['Chrono', 'Blaster']},
    {'name': 'Fiora', 'championId': 'TFT3_Fiora', 'cost': 1, 'traits': ['Cybernetic', 'Blademaster']},
    {'name': 'Fizz', 'championId': 'TFT3_Fizz', 'cost': 4, 'traits': ['Mech-Pilot', 'Infiltrator']},
    {'name': 'Gangplank', 'championId': 'TFT3_Gangplank', 'cost': 5,
     'traits': ['Space Pirate', 'Mercenary', 'Demolitionist']},
    {'name': 'Gnar', 'championId': 'TFT3_Gnar', 'cost': 4, 'traits': ['Astro', 'Brawler']},
    {'name': 'Graves', 'championId': 'TFT3_Graves', 'cost': 1, 'traits': ['Space Pirate', 'Blaster']},
    {'name': 'Illaoi', 'championId': 'TFT3_Illaoi', 'cost': 1, 'traits': ['Battlecast', 'Brawler']},
    {'name': 'Irelia', 'championId': 'TFT3_Irelia', 'cost': 4, 'traits': ['Cybernetic', 'Mana-Reaver', 'Blademaster']},
    {'name': 'Janna', 'championId': 'TFT3_Janna', 'cost': 5, 'traits': ['Paragon', 'Star Guardian']},
    {'name': 'Jarvan IV', 'championId': 'TFT3_JarvanIV', 'cost': 1, 'traits': ['Dark Star', 'Protector']},
    {'name': 'Jayce', 'championId': 'TFT3_Jayce', 'cost': 3, 'traits': ['Space Pirate', 'Vanguard']},
    {'name': 'Jhin', 'championId': 'TFT3_Jhin', 'cost': 4, 'traits': ['Dark Star', 'Sniper']},
    {'name': 'Jinx', 'championId': 'TFT3_Jinx', 'cost': 4, 'traits': ['Rebel', 'Blaster']},
    {'name': 'Karma', 'championId': 'TFT3_Karma', 'cost': 3, 'traits': ['Dark Star', 'Mystic']},
    {'name': 'KogMaw', 'championId': 'TFT3_KogMaw', 'cost': 2, 'traits': ['Battlecast', 'Blaster']},
    {'name': 'Leona', 'championId': 'TFT3_Leona', 'cost': 1, 'traits': ['Cybernetic', 'Vanguard']},
    {'name': 'Lucian', 'championId': 'TFT3_Lucian', 'cost': 2, 'traits': ['Cybernetic', 'Blaster']},
    {'name': 'Lulu', 'championId': 'TFT3_Lulu', 'cost': 5, 'traits': ['Celestial', 'Mystic']},
    {'name': 'Malphite', 'championId': 'TFT3_Malphite', 'cost': 1, 'traits': ['Rebel', 'Brawler']},
    {'name': 'Master Yi', 'championId': 'TFT3_MasterYi', 'cost': 3, 'traits': ['Rebel', 'Blademaster']},
    {'name': 'Mordekaiser', 'championId': 'TFT3_Mordekaiser', 'cost': 2, 'traits': ['Dark Star', 'Vanguard']},
    {'name': 'Nautilus', 'championId': 'TFT3_Nautilus', 'cost': 2, 'traits': ['Astro', 'Vanguard']},
    {'name': 'Neeko', 'championId': 'TFT3_Neeko', 'cost': 3, 'traits': ['Star Guardian', 'Protector']},
    {'name': 'Nocturne', 'championId': 'TFT3_Nocturne', 'cost': 1, 'traits': ['Battlecast', 'Infiltrator']},
    {'name': 'Poppy', 'championId': 'TFT3_Poppy', 'cost': 1, 'traits': ['Star Guardian', 'Vanguard']},
    {'name': 'Rakan', 'championId': 'TFT3_Rakan', 'cost': 2, 'traits': ['Celestial', 'Protector']},
    {'name': 'Riven', 'championId': 'TFT3_Riven', 'cost': 4, 'traits': ['Chrono', 'Blademaster']},
    {'name': 'Rumble', 'championId': 'TFT3_Rumble', 'cost': 3, 'traits': ['Mech-Pilot', 'Demolitionist']},
    {'name': 'Shaco', 'championId': 'TFT3_Shaco', 'cost': 3, 'traits': ['Dark Star', 'Infiltrator']},
    {'name': 'Shen', 'championId': 'TFT3_Shen', 'cost': 2, 'traits': ['Chrono', 'Blademaster']},
    {'name': 'Soraka', 'championId': 'TFT3_Soraka', 'cost': 4, 'traits': ['Star Guardian', 'Mystic']},
    {'name': 'Syndra', 'championId': 'TFT3_Syndra', 'cost': 3, 'traits': ['Star Guardian', 'Sorcerer']},
    {'name': 'Teemo', 'championId': 'TFT3_Teemo', 'cost': 4, 'traits': ['Astro', 'Sniper']},
    {'name': 'Thresh', 'championId': 'TFT3_Thresh', 'cost': 5, 'traits': ['Chrono', 'Mana-Reaver']},
    {'name': 'Twisted Fate', 'championId': 'TFT3_TwistedFate', 'cost': 1, 'traits': ['Chrono', 'Sorcerer']},
    {'name': 'Urgot', 'championId': 'TFT3_Urgot', 'cost': 5, 'traits': ['Battlecast', 'Protector']},
    {'name': 'Vayne', 'championId': 'TFT3_Vayne', 'cost': 3, 'traits': ['Cybernetic', 'Sniper']},
    {'name': 'Vi', 'championId': 'TFT3_Vi', 'cost': 3, 'traits': ['Cybernetic', 'Brawler']},
    {'name': 'Viktor', 'championId': 'TFT3_Viktor', 'cost': 4, 'traits': ['Battlecast', 'Sorcerer']},
    {'name': 'Wukong', 'championId': 'TFT3_WuKong', 'cost': 4, 'traits': ['Chrono', 'Vanguard']},
    {'name': 'Xayah', 'championId': 'TFT3_Xayah', 'cost': 1, 'traits': ['Celestial', 'Blademaster']},
    {'name': 'Xerath', 'championId': 'TFT3_Xerath', 'cost': 5, 'traits': ['Dark Star', 'Sorcerer']},
    {'name': 'Xin Zhao', 'championId': 'TFT3_XinZhao', 'cost': 2, 'traits': ['Celestial', 'Protector']},
    {'name': 'Yasuo', 'championId': 'TFT3_Yasuo', 'cost': 2, 'traits': ['Rebel', 'Blademaster']},
    {'name': 'Zed', 'championId': 'TFT3_Zed', 'cost': 2, 'traits': ['Rebel', 'Infiltrator']},
    {'name': 'Ziggs', 'championId': 'TFT3_Ziggs', 'cost': 1, 'traits': ['Rebel', 'Demolitionist']},
    {'name': 'Zoe', 'championId': 'TFT3_Zoe', 'cost': 1, 'traits': ['Star Guardian', 'Sorcerer']}
]

item_list = [
    {'id': 1, 'name': 'B.F. Sword'},
    {'id': 2, 'name': 'Recurve Bow'},
    {'id': 3, 'name': 'Needlessly Large Rod'},
    {'id': 4, 'name': 'Tear of the Goddess'},
    {'id': 5, 'name': 'Chain Vest'},
    {'id': 6, 'name': 'Negatron Cloak'},
    {'id': 7, 'name': "Giant's Belt"},
    {'id': 8, 'name': 'Spatula'},
    {'id': 9, 'name': 'Sparring Gloves'},
    {'id': 11, 'name': 'Deathblade'},
    {'id': 12, 'name': 'Giant Slayer'},
    {'id': 13, 'name': 'Hextech Gunblade'},
    {'id': 14, 'name': 'Spear of Shojin'},
    {'id': 15, 'name': 'Guardian Angel'},
    {'id': 16, 'name': 'Bloodthirster'},
    {'id': 17, 'name': "Zeke's Herald"},
    {'id': 18, 'name': 'Blade of the Ruined King'},
    {'id': 19, 'name': 'Infinity Edge'},
    {'id': 22, 'name': 'Rapid Firecannon'},
    {'id': 23, 'name': "Guinsoo's Rageblade"},
    {'id': 24, 'name': 'Statikk Shiv'},
    {'id': 25, 'name': "Titan's Resolve"},
    {'id': 26, 'name': "Runaan's Hurricane"},
    {'id': 27, 'name': "Zz'Rot Portal"},
    {'id': 28, 'name': "Infiltrator's Talons"},
    {'id': 29, 'name': 'Last Whisper'},
    {'id': 33, 'name': "Rabadon's Deathcap"},
    {'id': 34, 'name': "Luden's Echo"},
    {'id': 35, 'name': 'Locket of the Iron Solari'},
    {'id': 36, 'name': 'Ionic Spark'},
    {'id': 37, 'name': 'Morellonomicon'},
    {'id': 38, 'name': "Battlecast Armor"},
    {'id': 39, 'name': 'Jeweled Gauntlet'},
    {'id': 44, 'name': "Seraph's Embrace"},
    {'id': 45, 'name': 'Frozen Heart'},
    {'id': 46, 'name': 'Chalice of Power'},
    {'id': 47, 'name': 'Redemption'},
    {'id': 48, 'name': "Star Guardian's Charm"},
    {'id': 49, 'name': 'Hand Of Justice'},
    {'id': 55, 'name': 'Bramble Vest'},
    {'id': 56, 'name': 'Sword Breaker'},
    {'id': 57, 'name': 'Red Buff'},
    {'id': 58, 'name': 'Rebel Medal'},
    {'id': 59, 'name': 'Shroud of Stillness'},
    {'id': 66, 'name': "Dragon's Claw"},
    {'id': 67, 'name': 'Zephyr'},
    {'id': 68, 'name': 'Celestial Orb'},
    {'id': 69, 'name': 'Quicksilver'},
    {'id': 77, 'name': "Warmog's Armor"},
    {'id': 78, 'name': "Protector's Chestguard"},
    {'id': 79, 'name': 'Trap Claw'},
    {'id': 88, 'name': 'Force of Nature'},
    {'id': 89, 'name': "Dark Star's Heart"},
    {'id': 99, 'name': "Thief's Gloves"}
]
get_item_id_by_name = {}
for i in item_list:
    get_item_id_by_name[i["name"]] = i["id"]

galaxy_list = [
    {
        "key": "TFT3_GameVariation_BigLittleLegends",
        "name": "Medium Legends",
        "description": "Little Legends are bigger and have +25 starting health."
    },
    {
        "key": "TFT3_GameVariation_Bonanza",
        "name": "Treasure Trove",
        "description": "All minions and monsters drop a loot orb."
    },
    {
        "key": "TFT3_GameVariation_FreeNeekos",
        "name": "The Neekoverse",
        "description": "Everyone gets two free copies of Neeko’s Help."
    },
    {
        "key": "TFT3_GameVariation_FreeRerolls",
        "name": "Trade Sector",
        "description": "All players receive one free reroll per round. Free rerolls cannot be saved up."
    },
    {
        "key": "TFT3_GameVariation_MidGameFoN",
        "name": "Superdense Galaxy",
        "description": "Receive a free Force of Nature after the stage 3 carousel."
    },
    {
        "key": "TFT3_GameVariation_None",
        "name": "Normal Game",
        "description": "No special rules."
    },
    {
        "key": "TFT3_GameVariation_StartingItems",
        "name": "Galactic Armory",
        "description": "All players start with the same 2 completed items."
    },
    {
        "key": "TFT3_GameVariation_TwoStarCarousels",
        "name": "Star Cluster",
        "description": "1, 2, and 3 cost units on carousels have two stars."
    },
    {
        "key": "TFT3_GameVariation_LittlerLegends",
        "name": "Littler Little Legends",
        "description": "Everyone starts with 85 health instead of 100."
    }
]

# should update




###########################
###########################
def _make_zeros(n):
    output = []
    for i in range(n):
        output.append(0)
    return output


def _std_dot(v1, v2):
    inner_product = 0
    v1_sq = 0
    v2_sq = 0
    if len(v1) != len(v2):
        print("vector size is different!!!")
        raise ValueError
    else:
        n = len(v1)
        for i in range(n):
            inner_product += v1[i] * v2[i]
            v1_sq += v1[i] * v1[i]
            v2_sq += v2[i] * v2[i]
        std_ip = inner_product / ((v1_sq ** 0.5) * (v2_sq ** 0.5))
        std_ip = round(std_ip * 1000) / 1000
        return std_ip


def _make_deck_vector(deck):
    vector = _make_zeros(len(champion_list))
    for i in range(len(champion_list)):
        for j in range(len(deck)):
            if champion_list[i]["championId"] == deck[j]:
                vector[i] += 1
    return vector


def _get_traits(champions, items=[]):
    traits_by_name = {}
    # get traits from champions
    for champion_id in champions:
        champion = None
        for champ in champion_list:
            if champ["championId"] == champion_id:
                champion = champ.copy()
        for trait in trait_list:
            champion_traits = champion["traits"]
            if trait["name"] in champion_traits:
                if trait["name"] in traits_by_name:
                    traits_by_name[trait["name"]] += 1
                else:
                    traits_by_name[trait["name"]] = 1

    # get traits from items
    for i in range(len(items)):
        if items[i] == 18:
            t = "Blademaster"
            if t in traits_by_name:
                traits_by_name[t] += 1
            else:
                traits_by_name[t] = 1
        elif items[i] == 28:
            t = "Infiltrator"
            if t in traits_by_name:
                traits_by_name[t] += 1
            else:
                traits_by_name[t] = 1
        elif items[i] == 38:
            t = "Battlecast"
            if t in traits_by_name:
                traits_by_name[t] += 1
            else:
                traits_by_name[t] = 1
        elif items[i] == 48:
            t = "Star Guardian"
            if t in traits_by_name:
                traits_by_name[t] += 1
            else:
                traits_by_name[t] = 1
        elif items[i] == 58:
            t = "Rebel"
            if t in traits_by_name:
                traits_by_name[t] += 1
            else:
                traits_by_name[t] = 1
        elif items[i] == 68:
            t = "Celestial"
            if t in traits_by_name:
                traits_by_name[t] += 1
            else:
                traits_by_name[t] = 1
        elif items[i] == 78:
            t = "Protector"
            if t in traits_by_name:
                traits_by_name[t] += 1
            else:
                traits_by_name[t] = 1
        elif items[i] == 98:
            t = "Dark Star"
            if t in traits_by_name:
                traits_by_name[t] += 1
            else:
                traits_by_name[t] = 1

    output = []
    # return trait key, num_units, tier
    for trait_n in traits_by_name:
        cnt = traits_by_name[trait_n]
        for trait in trait_list:
            if trait["name"] == trait_n:
                tier = 0
                sets = trait["sets"]
                for s in sets:
                    if s["min"] <= cnt:
                        tier = sets.index(s) + 1
                output_trait = {'name': trait["key"], 'num_units': cnt, 'tier_current': tier}
                output.append(output_trait)

    return output


class Deck:

    ######## METAS ########
    Metas = {
        # Astro_Sniper Family
        "Astro_Sniper": {
            "parent_deck": "self",
            "deck_vector": _make_deck_vector(
                ["TFT3_Mordekaiser", "TFT3_Nautilus", "TFT3_Jayce", "TFT3_Gnar", "TFT3_Jhin",
                 "TFT3_Teemo", "TFT3_WuKong", "TFT3_Thresh"]),
            "carry_champion": ["TFT3_Teemo"],
            "traits": _get_traits(["TFT3_Caitlyn", "TFT3_Nautilus", "TFT3_Ashe", "TFT3_Gnar", "TFT3_Jhin", "TFT3_Teemo",
                                   "TFT3_WuKong", "TFT3_Thresh"]),
            "main_traits": [
                {'name': "Sniper", 'tier_current': 1},
                {'name': "Vanguard", 'tier_current': 2}
            ]
        },
        "Astro_Sniper_sub_4sniper": {
            "parent_deck": "Astro_Sniper",
            "deck_vector": _make_deck_vector(["TFT3_Caitlyn", "TFT3_Nautilus", "TFT3_Ashe", "TFT3_Karma",
                                              "TFT3_Gnar", "TFT3_Jhin", "TFT3_Teemo", "TFT3_WuKong", "TFT3_Lulu"]),
            "carry_champion": ["TFT3_Teemo"],
            "traits": _get_traits(["TFT3_Caitlyn", "TFT3_Nautilus", "TFT3_Ashe", "TFT3_Karma", "TFT3_Gnar", "TFT3_Jhin",
                                   "TFT3_Teemo", "TFT3_WuKong", "TFT3_Lulu"]),
            "main_traits": [
                {'name': "Sniper", 'tier_current': 2},
                {'name': "Astro", 'tier_current': 1}
            ]
        },
        "Astro_Sniper_sub_4sniper_4vanguard": {
            "parent_deck": "Astro_Sniper",
            "deck_vector": _make_deck_vector(["TFT3_Caitlyn", "TFT3_Mordekaiser", "TFT3_Nautilus", "TFT3_Ashe",
                                              "TFT3_Jayce", "TFT3_Gnar", "TFT3_Jhin", "TFT3_Teemo", "TFT3_WuKong"]),
            "carry_champion": ["TFT3_Teemo"],
            "traits": _get_traits(["TFT3_Caitlyn", "TFT3_Mordekaiser", "TFT3_Nautilus", "TFT3_Ashe", "TFT3_Jayce",
                                   "TFT3_Gnar", "TFT3_Jhin", "TFT3_Teemo", "TFT3_WuKong"]),
            "main_traits": [
                {'name': "Sniper", 'tier_current': 2},
                {'name': "Astro", 'tier_current': 1},
                {'name': "Vanguard", 'tier_current': 2}
            ]
        },

        # Cybernetic Family
        "Cybernetics": {
            "parent_deck": "self",
            "deck_vector": _make_deck_vector(["TFT3_Fiora", "TFT3_Leona", "TFT3_Vi", "TFT3_Vayne", "TFT3_Riven",
                                              "TFT3_Irelia", "TFT3_Ekko", "TFT3_Thresh"]),
            "carry_champion": ["TFT3_Vayne", "TFT3_Irelia"],
            "traits": _get_traits(["TFT3_Fiora", "TFT3_Leona", "TFT3_Vi", "TFT3_Vayne", "TFT3_Riven",
                                   "TFT3_Irelia", "TFT3_Ekko", "TFT3_Thresh"]),
            "main_traits": [
                {'name': "Cybernetic", 'tier_current': 2}
            ]
        },
        "Cybernetics_sub_Lucian": {
            "parent_deck": "Cybernetics",
            "deck_vector": _make_deck_vector(["TFT3_Fiora", "TFT3_Lucian", "TFT3_Vi", "TFT3_Vayne", "TFT3_Riven",
                                              "TFT3_Irelia", "TFT3_Ekko", "TFT3_Thresh"]),
            "carry_champion": ["TFT3_Vayne", "TFT3_Irelia"],
            "traits": _get_traits(["TFT3_Fiora", "TFT3_Lucian", "TFT3_Vi", "TFT3_Vayne", "TFT3_Riven",
                                   "TFT3_Irelia", "TFT3_Ekko", "TFT3_Thresh"]),
            "main_traits": [
                {'name': "Cybernetic", 'tier_current': 2}
            ]
        },
        "Cybernetics_sub_Irelia_main": {
            "parent_deck": "Cybernetics",
            "deck_vector": _make_deck_vector(["TFT3_Leona", "TFT3_Fiora", "TFT3_Vi", "TFT3_Vayne", "TFT3_Riven",
                                              "TFT3_Fizz", "TFT3_Irelia", "TFT3_Ekko", "TFT3_Thresh"]),
            "carry_champion": ["TFT3_Vayne", "TFT3_Irelia"],
            "traits": _get_traits(["TFT3_Leona", "TFT3_Fiora", "TFT3_Vi", "TFT3_Vayne", "TFT3_Riven",
                                   "TFT3_Fizz", "TFT3_Irelia", "TFT3_Ekko", "TFT3_Thresh"]),
            "main_traits": [
                {'name': "Cybernetic", 'tier_current': 2}
            ]
        },
        "Cybernetics_sub_Vayne_main": {
            "parent_deck": "Cybernetics",
            "deck_vector": _make_deck_vector(["TFT3_Caitlyn", "TFT3_Leona", "TFT3_Fiora", "TFT3_Vi", "TFT3_Vayne",
                                              "TFT3_Fizz", "TFT3_Irelia", "TFT3_Ekko", "TFT3_Thresh"]),
            "carry_champion": ["TFT3_Vayne", "TFT3_Irelia"],
            "traits": _get_traits(["TFT3_Caitlyn", "TFT3_Leona", "TFT3_Fiora", "TFT3_Vi", "TFT3_Vayne", "TFT3_Fizz",
                                   "TFT3_Irelia", "TFT3_Ekko", "TFT3_Thresh"]),
            "main_traits": [
                {'name': "Cybernetic", 'tier_current': 2}
            ]
        },

        # Blaster_Brawler Family
        "Blaster_Brawler": {
            "parent_deck": "self",
            "deck_vector": _make_deck_vector(["TFT3_Graves", "TFT3_Illaoi", "TFT3_Blitzcrank", "TFT3_KogMaw",
                                              "TFT3_Ezreal", "TFT3_Vi", "TFT3_Gnar", "TFT3_Jinx"]),
            "carry_champion": ["TFT3_Jinx"],
            "traits": _get_traits(["TFT3_Graves", "TFT3_Illaoi", "TFT3_Blitzcrank", "TFT3_KogMaw", "TFT3_Ezreal",
                                   "TFT3_Vi", "TFT3_Gnar", "TFT3_Jinx"]),
            "main_traits": [
                {'name': "Blaster", 'tier_current': 2},
                {'name': "Set3_Brawler", 'tier_current': 2}
            ]
        },
        "Blaster_Brawler_sub_mystic": {
            "parent_deck": "Blaster_Brawler",
            "deck_vector": _make_deck_vector(["TFT3_Malphite", "TFT3_Blitzcrank", "TFT3_Ezreal", "TFT3_Vi", "TFT3_Gnar",
                                              "TFT3_Jinx", "TFT3_Soraka", "TFT3_AurelionSol", "TFT3_Lulu"]),
            "carry_champion": ["TFT3_Jinx", "TFT3_Gnar"],
            "traits": _get_traits(["TFT3_Malphite", "TFT3_Blitzcrank", "TFT3_Ezreal", "TFT3_Vi", "TFT3_Gnar",
                                   "TFT3_Jinx", "TFT3_Soraka", "TFT3_AurelionSol", "TFT3_Lulu"]),
            "main_traits": [
                {'name': "Blaster", 'tier_current': 1},
                {'name': "Set3_Brawler", 'tier_current': 2},
                {'name': "Set3_Mystic", 'tier_current': 2}
            ]
        },
        "Blaster_Brawler_sub_chrono": {
            "parent_deck": "Blaster_Brawler",
            "deck_vector": _make_deck_vector(["TFT3_Malphite", "TFT3_Blitzcrank", "TFT3_Ezreal", "TFT3_Vi", "TFT3_Gnar",
                                              "TFT3_Jinx", "TFT3_WuKong", "TFT3_AurelionSol", "TFT3_Thresh"]),
            "carry_champion": ["TFT3_Jinx", "TFT3_Gnar", "TFT3_Thresh"],
            "traits": _get_traits(["TFT3_Malphite", "TFT3_Blitzcrank", "TFT3_Ezreal", "TFT3_Vi", "TFT3_Gnar",
                                   "TFT3_Jinx", "TFT3_WuKong", "TFT3_AurelionSol", "TFT3_Thresh"]),
            "main_traits": [
                {'name': "Blaster", 'tier_current': 1},
                {'name': "Set3_Brawler", 'tier_current': 2},
                {'name': "Chrono", 'tier_current': 1}
            ]
        },
        "Blaster_Brawler_sub_Janna": {
            "parent_deck": "Blaster_Brawler",
            "deck_vector": _make_deck_vector(["TFT3_Malphite", "TFT3_Blitzcrank", "TFT3_Ezreal", "TFT3_Vi", "TFT3_Gnar",
                                              "TFT3_Jinx", "TFT3_AurelionSol", "TFT3_Janna", "TFT3_Thresh"]),
            "carry_champion": ["TFT3_Jinx", "TFT3_Gnar", "TFT3_Janna"],
            "traits": _get_traits(["TFT3_Malphite", "TFT3_Blitzcrank", "TFT3_Ezreal", "TFT3_Vi", "TFT3_Gnar",
                                   "TFT3_Jinx", "TFT3_AurelionSol", "TFT3_Janna", "TFT3_Thresh"]),
            "main_traits": [
                {'name': "Blaster", 'tier_current': 1},
                {'name': "Set3_Brawler", 'tier_current': 2},
                {'name': "Paragon", 'tier_current': 1}
            ]
        },
        "Blaster_Brawler_sub_demolitionist": {
            "parent_deck": "Blaster_Brawler",
            "deck_vector": _make_deck_vector(["TFT3_Malphite", "TFT3_Ziggs", "TFT3_Blitzcrank", "TFT3_Ezreal", "TFT3_Vi",
                                              "TFT3_Gnar", "TFT3_Jinx", "TFT3_AurelionSol", "TFT3_Gangplank"]),
            "carry_champion": ["TFT3_Jinx", "TFT3_Gnar", "TFT3_Gangplank"],
            "traits": _get_traits(["TFT3_Malphite", "TFT3_Ziggs", "TFT3_Blitzcrank", "TFT3_Ezreal", "TFT3_Vi",
                                   "TFT3_Gnar", "TFT3_Jinx", "TFT3_AurelionSol", "TFT3_Gangplank"]),
            "main_traits": [
                {'name': "Blaster", 'tier_current': 1},
                {'name': "Set3_Brawler", 'tier_current': 2},
                {'name': "Demolitionist", 'tier_current': 1}
            ]
        },

        "Jinx_Gangplank": {
            "parent_deck": "self",
            "deck_vector": _make_deck_vector(["TFT3_Ziggs", "TFT3_Blitzcrank", "TFT3_Ezreal", "TFT3_Gnar", "TFT3_Jinx",
                                              "TFT3_Soraka", "TFT3_AurelionSol", "TFT3_Gangplank", "TFT3_Lulu"]),
            "carry_champion": ["TFT3_Jinx", "TFT3_Gangplank"],
            "traits": _get_traits(["TFT3_Ziggs", "TFT3_Blitzcrank", "TFT3_Ezreal", "TFT3_Gnar", "TFT3_Jinx",
                                   "TFT3_Soraka", "TFT3_AurelionSol", "TFT3_Gangplank", "TFT3_Lulu"]),
            "main_traits": [
                {'name': "Blaster", 'tier_current': 1},
                {'name': "Set3_Brawler", 'tier_current': 1},
                {'name': "Demolitionist", 'tier_current': 1},
                {'name': "Set3_Mystic", 'tier_current': 1}
            ]
        },

        # 6Blademaster Family
        "6Blademaster": {
            "parent_deck": "self",
            "deck_vector": _make_deck_vector(["TFT3_Shen", "TFT3_Yasuo", "TFT3_Zed", "TFT3_MasterYi", "TFT3_Irelia",
                                              "TFT3_Riven", "TFT3_Fizz", "TFT3_Thresh"]),
            "carry_champion": ["TFT3_Zed", "TFT3_MasterYi"],
            "traits": _get_traits(["TFT3_Shen", "TFT3_Yasuo", "TFT3_Zed", "TFT3_MasterYi", "TFT3_Irelia",
                                   "TFT3_Riven", "TFT3_Fizz", "TFT3_Thresh"], [18]),
            "main_traits": [
                {'name': "Set3_Blademaster", 'tier_current': 2},
                {'name': "ManaReaver", 'tier_current': 1}
            ]
        },
        "6Blademaster_sub_celestial": {
            "parent_deck": "6Blademaster",
            "deck_vector": _make_deck_vector(["TFT3_Xayah", "TFT3_Shen", "TFT3_Yasuo", "TFT3_Zed",
                                              "TFT3_MasterYi", "TFT3_Riven", "TFT3_Fizz", "TFT3_Lulu"]),
            "carry_champion": ["TFT3_Zed", "TFT3_MasterYi"],
            "traits": _get_traits(["TFT3_Xayah", "TFT3_Shen", "TFT3_Yasuo", "TFT3_Zed",
                                   "TFT3_MasterYi", "TFT3_Riven", "TFT3_Fizz", "TFT3_Lulu"], [18]),
            "main_traits": [
                {'name': "Set3_Blademaster", 'tier_current': 2},
                {'name': "Set3_Celestial", 'tier_current': 1}
            ]
        },
        "6Blademaster_sub_Ausol": {
            "parent_deck": "6Blademaster",
            "deck_vector": _make_deck_vector(["TFT3_Shen", "TFT3_Yasuo", "TFT3_Zed", "TFT3_MasterYi", "TFT3_Irelia",
                                              "TFT3_Riven", "TFT3_Fizz", "TFT3_AurelionSol"]),
            "carry_champion": ["TFT3_Zed", "TFT3_MasterYi"],
            "traits": _get_traits(["TFT3_Shen", "TFT3_Yasuo", "TFT3_Zed", "TFT3_MasterYi", "TFT3_Irelia",
                                   "TFT3_Riven", "TFT3_Fizz", "TFT3_AurelionSol"], [18]),
            "main_traits": [
                {'name': "Set3_Blademaster", 'tier_current': 2},
                {'name': "Starship", 'tier_current': 1}
            ]
        },

        "Battlecast_Brawler": {
            "deck_vector": _make_deck_vector(["TFT3_Illaoi", "TFT3_Blitzcrank", "TFT3_Cassiopeia", "TFT3_Vi",
                                              "TFT3_Gnar", "TFT3_Viktor", "TFT3_Urgot", "TFT3_Lulu"]),
            "carry_champion": [],
            "traits": _get_traits(["TFT3_Illaoi", "TFT3_Blitzcrank", "TFT3_Cassiopeia", "TFT3_Vi", "TFT3_Gnar",
                                   "TFT3_Viktor", "TFT3_Urgot", "TFT3_Lulu"]),
            "main_traits": [
                {'name': "Battlecast", 'tier_current': 2},
                {'name': "Set3_Brawler", 'tier_current': 2}
            ]
        },

        # StarGuardian_Sorcerer Family
        "StarGuardian_Sorcerer": {
            "parent_deck": "self",
            "deck_vector": _make_deck_vector(["TFT3_Zoe", "TFT3_Ahri", "TFT3_Neeko", "TFT3_Syndra", "TFT3_Soraka",
                                              "TFT3_Janna", "TFT3_Lulu", "TFT3_Xerath"]),
            "carry_champion": ["TFT3_Neeko", "TFT3_Syndra"],
            "traits": _get_traits(["TFT3_Zoe", "TFT3_Ahri", "TFT3_Neeko", "TFT3_Syndra", "TFT3_Soraka", "TFT3_Janna",
                                   "TFT3_Lulu", "TFT3_Xerath"]),
            "main_traits": [
                {'name': "Set3_Sorcerer", 'tier_current': 2},
                {'name': "StarGuardian", 'tier_current': 2}
            ]
        },
        "StarGuardian_Sorcerer_sub_Viktor": {
            "parent_deck": "StarGuardian_Sorcerer",
            "deck_vector": _make_deck_vector(["TFT3_Poppy", "TFT3_TwistedFate", "TFT3_Zoe", "TFT3_Ahri", "TFT3_Syndra",
                                              "TFT3_Viktor", "TFT3_WuKong", "TFT3_Janna"]),
            "carry_champion": ["TFT3_Syndra", "TFT3_Viktor"],
            "traits": _get_traits(["TFT3_Poppy", "TFT3_TwistedFate", "TFT3_Zoe", "TFT3_Ahri", "TFT3_Syndra",
                                   "TFT3_Viktor", "TFT3_WuKong", "TFT3_Janna"], [48]),
            "main_traits": [
                {'name': "Set3_Sorcerer", 'tier_current': 2},
                {'name': "StarGuardian", 'tier_current': 2}
            ]
        },
        "StarGuardian_Sorcerer_sub_Vik_Ri": {
            "parent_deck": "StarGuardian_Sorcerer",
            "deck_vector": _make_deck_vector(["TFT3_TwistedFate", "TFT3_Zoe", "TFT3_Ahri", "TFT3_Annie", "TFT3_Syndra",
                                              "TFT3_Riven", "TFT3_Soraka", "TFT3_Viktor", "TFT3_Janna"]),
            "carry_champion": ["TFT3_Riven", "TFT3_Viktor"],
            "traits": _get_traits(["TFT3_TwistedFate", "TFT3_Zoe", "TFT3_Ahri", "TFT3_Annie", "TFT3_Syndra",
                                   "TFT3_Riven", "TFT3_Soraka", "TFT3_Viktor", "TFT3_Janna"], [48]),
            "main_traits": [
                {'name': "Set3_Sorcerer", 'tier_current': 3},
                {'name': "StarGuardian", 'tier_current': 2}
            ]
        },

        # 6Sorcerer Family
        "6Sorcerer": {
            "parent_deck": "self",
            "deck_vector": _make_deck_vector(["TFT3_TwistedFate", "TFT3_Zoe", "TFT3_Ahri", "TFT3_Syndra", "TFT3_Riven",
                                              "TFT3_Viktor", "TFT3_Janna", "TFT3_Xerath"]),
            "carry_champion": ["TFT3_Riven", "TFT3_Xerath"],
            "traits": _get_traits(["TFT3_TwistedFate", "TFT3_Zoe", "TFT3_Ahri", "TFT3_Syndra", "TFT3_Riven",
                                   "TFT3_Viktor", "TFT3_Janna", "TFT3_Xerath"]),
            "main_traits": [
                {'name': "Set3_Sorcerer", 'tier_current': 3},
                {'name': "StarGuardian", 'tier_current': 1},
                {'name': "Chrono", 'tier_current': 1}
            ]
        },
        "6Sorcerer_sub_vanguard": {
            "parent_deck": "6Sorcerer",
            "deck_vector": _make_deck_vector(["TFT3_TwistedFate", "TFT3_Zoe", "TFT3_Ahri", "TFT3_Mordekaiser",
                                              "TFT3_Syndra", "TFT3_Viktor", "TFT3_WuKong", "TFT3_Janna",
                                              "TFT3_Xerath"]),
            "carry_champion": ["TFT3_Janna", "TFT3_Xerath"],
            "traits": _get_traits(["TFT3_TwistedFate", "TFT3_Zoe", "TFT3_Ahri", "TFT3_Mordekaiser", "TFT3_Syndra",
                                   "TFT3_Viktor", "TFT3_WuKong", "TFT3_Janna", "TFT3_Xerath"]),
            "main_traits": [
                {'name': "Set3_Sorcerer", 'tier_current': 3},
                {'name': "StarGuardian", 'tier_current': 1},
                {'name': "Paragon", 'tier_current': 1}
            ]
        },
        "6Sorcerer_sub_FiRi": {
            "parent_deck": "6Sorcerer",
            "deck_vector": _make_deck_vector(["TFT3_TwistedFate", "TFT3_Zoe", "TFT3_Ahri", "TFT3_Syndra", "TFT3_Fizz",
                                              "TFT3_Riven", "TFT3_Viktor", "TFT3_Janna", "TFT3_Xerath"]),
            "carry_champion": ["TFT3_Riven", "TFT3_Fizz"],
            "traits": _get_traits(["TFT3_TwistedFate", "TFT3_Zoe", "TFT3_Ahri", "TFT3_Syndra", "TFT3_Fizz",
                                   "TFT3_Riven", "TFT3_Viktor", "TFT3_Janna", "TFT3_Xerath"]),
            "main_traits": [
                {'name': "Set3_Sorcerer", 'tier_current': 3},
                {'name': "StarGuardian", 'tier_current': 1},
                {'name': "Paragon", 'tier_current': 1}
            ]
        },
        "6Sorcerer_sub_FiKo": {
            "parent_deck": "6Sorcerer",
            "deck_vector": _make_deck_vector(["TFT3_TwistedFate", "TFT3_Zoe", "TFT3_Ahri", "TFT3_Syndra", "TFT3_Fizz",
                                              "TFT3_Riven", "TFT3_Viktor", "TFT3_Ekko", "TFT3_Xerath"]),
            "carry_champion": ["TFT3_Riven", "TFT3_Fizz", "TFT3_Ekko"],
            "traits": _get_traits(["TFT3_TwistedFate", "TFT3_Zoe", "TFT3_Ahri", "TFT3_Syndra", "TFT3_Fizz",
                                   "TFT3_Riven", "TFT3_Viktor", "TFT3_Ekko", "TFT3_Xerath"]),
            "main_traits": [
                {'name': "Set3_Sorcerer", 'tier_current': 3},
                {'name': "StarGuardian", 'tier_current': 1},
                {'name': "Paragon", 'tier_current': 1}
            ]
        },


        "Celestial_Protector": {
            "parent_deck": "self",
            "deck_vector": _make_deck_vector(["TFT3_Rakan", "TFT3_XinZhao", "TFT3_Ashe", "TFT3_Cassiopeia",
                                              "TFT3_Neeko", "TFT3_Jhin", "TFT3_Lulu", "TFT3_Urgot"]),
            "carry_champion": [],
            "traits": _get_traits(["TFT3_Rakan", "TFT3_XinZhao", "TFT3_Ashe", "TFT3_Cassiopeia", "TFT3_Neeko",
                                   "TFT3_Jhin", "TFT3_Lulu", "TFT3_Urgot"]),
            "main_traits": [
                {'name': "Set3_Celestial", 'tier_current': 2},
                {'name': "Protector", 'tier_current': 2}
            ]
        },
        "Celestial_6Protector": {
            "parent_deck": "Celestial_Protector",
            "deck_vector": _make_deck_vector(["TFT3_JarvanIV", "TFT3_Rakan", "TFT3_XinZhao", "TFT3_Ashe",
                                              "TFT3_Cassiopeia", "TFT3_Neeko", "TFT3_Lulu", "TFT3_Urgot"]),
            "carry_champion": [],
            "traits": _get_traits(["TFT3_JarvanIV", "TFT3_Rakan", "TFT3_XinZhao", "TFT3_Ashe", "TFT3_Cassiopeia",
                                   "TFT3_Neeko", "TFT3_Lulu", "TFT3_Urgot"], [78]),
            "main_traits": [
                {'name': "Set3_Celestial", 'tier_current': 2},
                {'name': "Protector", 'tier_current': 3}
            ]
        },

        "6DarkStar": {
            "parent_deck": "self",
            "deck_vector": _make_deck_vector(
                ["TFT3_JarvanIV", "TFT3_Mordekaiser", "TFT3_Ashe", "TFT3_Karma", "TFT3_Shaco",
                 "TFT3_Jhin", "TFT3_Lulu", "TFT3_Xerath"]),
            "carry_champion": ["TFT3_Jhin", "TFT3_Xerath"],
            "traits": _get_traits(["TFT3_JarvanIV", "TFT3_Mordekaiser", "TFT3_Ashe", "TFT3_Karma", "TFT3_Shaco",
                                   "TFT3_Jhin", "TFT3_Lulu", "TFT3_Xerath"]),
            "main_traits": [
                {'name': "DarkStar", 'tier_current': 3}
            ]
        },

        "6Rebel": {
            "parent_deck": "self",
            "deck_vector": _make_deck_vector(["TFT3_Malphite", "TFT3_Ziggs", "TFT3_Yasuo", "TFT3_Ezreal",
                                              "TFT3_MasterYi", "TFT3_Jinx", "TFT3_AurelionSol", "TFT3_Gangplank"]),
            "carry_champion": ["TFT3_Jinx", "TFT3_AurelionSol"],
            "traits": _get_traits(["TFT3_Malphite", "TFT3_Ziggs", "TFT3_Yasuo", "TFT3_Ezreal",
                                   "TFT3_MasterYi", "TFT3_Jinx", "TFT3_AurelionSol", "TFT3_Gangplank"]),
            "main_traits": [
                {'name': "Rebel", 'tier_current': 2}
            ]
        },

        "Mech_infiltrator": {
            "parent_deck": "self",
            "deck_vector": _make_deck_vector(["TFT3_Nocturne", "TFT3_Ziggs", "TFT3_Annie", "TFT3_Zed", "TFT3_Rumble",
                                              "TFT3_Shaco", "TFT3_Fizz", "TFT3_Viktor"]),
            "carry_champion": ["TFT3_Zed", "TFT3_Shaco"],
            "traits": _get_traits(["TFT3_Nocturne", "TFT3_Ziggs", "TFT3_Annie", "TFT3_Zed", "TFT3_Rumble",
                                   "TFT3_Shaco", "TFT3_Fizz", "TFT3_Viktor"]),
            "main_traits": [
                {'name': "Set3_Sorcerer", 'tier_current': 3},
                {'name': "MechPilot", 'tier_current': 1}
            ]
        },

        "Mech_mage": {
            "parent_deck": "self",
            "deck_vector": _make_deck_vector(["TFT3_Zoe", "TFT3_Ahri", "TFT3_Annie", "TFT3_Rumble", "TFT3_Syndra",
                                              "TFT3_Fizz", "TFT3_Viktor", "TFT3_Xerath"]),
            "carry_champion": ["TFT3_Viktor", "TFT3_Xerath"],
            "traits": _get_traits(["TFT3_Zoe", "TFT3_Ahri", "TFT3_Annie", "TFT3_Rumble", "TFT3_Syndra",
                                   "TFT3_Fizz", "TFT3_Viktor", "TFT3_Xerath"]),
            "main_traits": [
                {'name': "Infiltrator", 'tier_current': 2},
                {'name': "MechPilot", 'tier_current': 1}
            ]
        },

        "Mech_blaster": {
            "parent_deck": "self",
            "deck_vector": _make_deck_vector(["TFT3_TwistedFate", "TFT3_Annie", "TFT3_Zed", "TFT3_Rumble",
                                              "TFT3_Ezreal", "TFT3_Jinx", "TFT3_Fizz", "TFT3_Gangplank"]),
            "carry_champion": ["TFT3_Jinx", "TFT3_Gangplank"],
            "traits": _get_traits(["TFT3_TwistedFate", "TFT3_Annie", "TFT3_Zed", "TFT3_Rumble",
                                   "TFT3_Ezreal", "TFT3_Jinx", "TFT3_Fizz", "TFT3_Gangplank"]),
            "main_traits": [
                {'name': "Blaster", 'tier_current': 1},
                {'name': "MechPilot", 'tier_current': 1},
                {'name': "Demolitionist", 'tier_current': 1}
            ]
        },
        "Mech_blaster_sub_rebel": {
            "parent_deck": "Mech_blaster",
            "deck_vector": _make_deck_vector(["TFT3_TwistedFate", "TFT3_Annie", "TFT3_Zed", "TFT3_Rumble", "TFT3_Ezreal",
                                              "TFT3_Jinx", "TFT3_Fizz", "TFT3_Gangplank", "TFT3_AurelionSol"]),
            "carry_champion": ["TFT3_Jinx", "TFT3_Gangplank"],
            "traits": _get_traits(["TFT3_TwistedFate", "TFT3_Annie", "TFT3_Zed", "TFT3_Rumble",
                                   "TFT3_Ezreal", "TFT3_Jinx", "TFT3_Fizz", "TFT3_Gangplank", "TFT3_AurelionSol"]),
            "main_traits": [
                {'name': "Blaster", 'tier_current': 1},
                {'name': "MechPilot", 'tier_current': 1},
                {'name': "Demolitionist", 'tier_current': 1},
                {'name': "Rebel", 'tier_current': 1}
            ]
        },

        "4SpacePirate": {
            "parent_deck": "self",
            "deck_vector": _make_deck_vector(["TFT3_Graves", "TFT3_Ziggs", "TFT3_Darius", "TFT3_Jayce", "TFT3_Jinx",
                                              "TFT3_WuKong", "TFT3_AurelionSol", "TFT3_Gangplank", "TFT3_Thresh"]),
            "carry_champion": [],
            "traits": _get_traits(["TFT3_Graves", "TFT3_Ziggs", "TFT3_Darius", "TFT3_Jayce", "TFT3_Jinx",
                                   "TFT3_WuKong", "TFT3_AurelionSol", "TFT3_Gangplank", "TFT3_Thresh"]),
            "main_traits": [
                {'name': "SpacePirate", 'tier_current': 2},
                {'name': "Rebel", 'tier_current': 1},
                {'name': "ManaReaver", 'tier_current': 1},
                {'name': "Demolitionist", 'tier_current': 1}
            ]
        },
        "Chrono_Blademaster": {
            "deck_vector": _make_deck_vector(["TFT3_Shen", "TFT3_Jayce", "TFT3_Irelia", "TFT3_Riven", "TFT3_Soraka",
                                              "TFT3_WuKong", "TFT3_Lulu", "TFT3_Thresh"]),
            "carry_champion": [],
            "traits": _get_traits(["TFT3_Shen", "TFT3_Jayce", "TFT3_Irelia", "TFT3_Riven", "TFT3_Soraka",
                                   "TFT3_WuKong", "TFT3_Lulu", "TFT3_Thresh"]),
            "main_traits": [
                {'name': "Set3_Blademaster", 'tier_current': 1},
                {'name': "Chrono", 'tier_current': 2}
            ]
        },
        "Reroll_Zed": {
            "parent_deck": "self",
            "deck_vector": _make_deck_vector(["TFT3_Nocturne", "TFT3_Rakan", "TFT3_XinZhao", "TFT3_Zed",
                                              "TFT3_Cassiopeia", "TFT3_Karma", "TFT3_Shaco", "TFT3_Fizz"]),
            "carry_champion": ["TFT3_Zed"],
            "traits": _get_traits(["TFT3_Nocturne", "TFT3_Rakan", "TFT3_XinZhao", "TFT3_Zed", "TFT3_Cassiopeia",
                                   "TFT3_Karma", "TFT3_Shaco", "TFT3_Fizz"]),
            "main_traits": [
                {'name': "Infiltrator", 'tier_current': 2},
                {'name': "Set3_Celestial", 'tier_current': 1}
            ]
        },
        "Mystic_Vanguard": {
            "parent_deck": "self",
            "deck_vector": _make_deck_vector(["TFT3_Mordekaiser", "TFT3_Nautilus", "TFT3_Cassiopeia", "TFT3_Jayce",
                                              "TFT3_Karma", "TFT3_Soraka", "TFT3_WuKong", "TFT3_Lulu"]),
            "carry_champion": ["TFT3_Cassiopeia", "TFT3_Jayce"],
            "traits": _get_traits(["TFT3_Mordekaiser", "TFT3_Nautilus", "TFT3_Cassiopeia", "TFT3_Jayce",
                                   "TFT3_Karma", "TFT3_Soraka", "TFT3_WuKong", "TFT3_Lulu"]),
            "main_traits": [
                {'name': "Set3_Mystic", 'tier_current': 2},
                {'name': "Vanguard", 'tier_current': 2}
            ]
        },
        "Mystic_Protector": {
            "parent_deck": "self",
            "deck_vector": _make_deck_vector(["TFT3_Rakan", "TFT3_XinZhao", "TFT3_Cassiopeia", "TFT3_Karma",
                                              "TFT3_Neeko", "TFT3_Soraka", "TFT3_Lulu", "TFT3_Urgot"]),
            "carry_champion": ["TFT3_XinZhao", "TFT3_Cassiopeia", "TFT3_Urgot"],
            "traits": _get_traits(["TFT3_Rakan", "TFT3_XinZhao", "TFT3_Cassiopeia", "TFT3_Karma",
                                   "TFT3_Neeko", "TFT3_Soraka", "TFT3_Lulu", "TFT3_Urgot"]),
            "main_traits": [
                {'name': "Set3_Mystic", 'tier_current': 2},
                {'name': "Protector", 'tier_current': 2}
            ]
        }
    }
    Meta_name = Metas.keys()
    completion_criteria = 0.94

    #######################

    def __init__(self, participant={}):
        self.champions = participant["units"]
        self.traits = participant["traits"]
        champion_names = []
        for champion in self.champions:
            champion_names.append(champion["character_id"])
        trait_names = []
        for trait in self.traits:
            trait_names.append(trait["name"])
        self.champion_names = champion_names
        self.trait_names = trait_names
        self.raw_data = participant
        self.is_accomplished = False
        self.champion_vector = _make_zeros(len(champion_list))
        for i in range(len(champion_list)):
            for j in range(len(self.champions)):
                if champion_list[i]["championId"] == self.champions[j]["character_id"]:
                    self.champion_vector[i] += 1

    def define_meta(self):
        max_std_similarity = 0
        meta_name = ""
        for meta in self.Meta_name:
            std_similarity = _std_dot(self.champion_vector, self.Metas[meta]["deck_vector"])
            if std_similarity > max_std_similarity:
                max_std_similarity = std_similarity
                meta_name = meta

        if max_std_similarity > 0.7:
            if max_std_similarity > self.completion_criteria:
                self.is_accomplished = True

            elif len(self.champions) >= 8:
                is_trait_accomplished = True
                for main_trait in self.Metas[meta_name]["main_traits"]:
                    if main_trait["name"] not in self.trait_names:
                        is_trait_accomplished = False
                        break

                    d_trait = self.traits[self.trait_names.index(main_trait["name"])]
                    if d_trait["tier_current"] < main_trait["tier_current"]:
                        is_trait_accomplished = False
                        break
                self.is_accomplished = is_trait_accomplished

            return meta_name, max_std_similarity
        return "etc", 0


'''
    "StarGuardian_Sorcerer": {
        "deck_vector": _make_deck_vector(["TFT3_Zoe", "TFT3_Poppy", "TFT3_Ahri", "TFT3_Sona", "TFT3_Neeko",
                                          "TFT3_Syndra", "TFT3_VelKoz", "TFT3_Soraka"]),
        "carry_champion": ["TFT3_Sona", "TFT3_Syndra"],
        "traits": _get_traits(["TFT3_Zoe", "TFT3_Poppy", "TFT3_Ahri", "TFT3_Sona", "TFT3_Neeko",
                               "TFT3_Syndra", "TFT3_VelKoz", "TFT3_Soraka"]),
        "main_traits": [
            {'name': "Set3_Sorcerer", 'tier_current': 2},
            {'name': "StarGuardian", 'tier_current': 2}
        ]
    },
    "DarkStar_Sniper": {
        "deck_vector": _make_deck_vector(["TFT3_Mordekaiser", "TFT3_Ashe", "TFT3_Karma", "TFT3_Lux", "TFT3_Shaco",
                                          "TFT3_Jhin", "TFT3_Lulu", "TFT3_Xerath"]),
        "carry_champion": ["TFT3_Jhin", "TFT3_Xerath"],
        "traits": _get_traits(["TFT3_Mordekaiser", "TFT3_Ashe", "TFT3_Karma", "TFT3_Lux", "TFT3_Shaco",
                               "TFT3_Jhin", "TFT3_Lulu", "TFT3_Xerath"]),
        "main_traits": [
            {'name': "DarkStar", 'tier_current': 2},
            {'name': "Sniper", 'tier_current': 1}
        ]
    },
    "Health_Deck": {
        "deck_vector": _make_deck_vector(["TFT3_JarvanIV", "TFT3_Rakan", "TFT3_Sona", "TFT3_XinZhao", "TFT3_Karma",
                                          "TFT3_Neeko", "TFT3_Soraka", "TFT3_Lulu"]),
        "carry_champion": ["TFT3_XinZhao"],
        "traits": _get_traits(["TFT3_JarvanIV", "TFT3_Rakan", "TFT3_Sona", "TFT3_XinZhao", "TFT3_Karma",
                               "TFT3_Neeko", "TFT3_Soraka", "TFT3_Lulu"]),
        "main_traits": [
            {'name': "Set3_Mystic", 'tier_current': 2},
            {'name': "Protector", 'tier_current': 2}
        ]
    }
'''
