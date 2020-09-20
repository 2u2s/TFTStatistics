######## constants ########
###########################
trait_list = [
    {'key': 'Cultist', 'name': 'Cultist', 'type': 'origin',
     'sets': [{'style': 'bronze', 'min': 3, 'max': 5}, {'style': 'silver', 'min': 6, 'max': 8},
              {'style': 'gold', 'min': 9}]},

    {'key': 'Divine', 'name': 'Divine', 'type': 'origin',
     'sets': [{'style': 'bronze', 'min': 2, 'max': 3}, {'style': 'silver', 'min': 4, 'max': 5},
              {'style': 'gold', 'min': 6, 'max': 7}, {'style': 'chromatic', 'min': 8}]},

    {'key': 'Dusk', 'name': 'Dusk', 'type': 'origin',
     'sets': [{'style': 'bronze', 'min': 2, 'max': 3}, {'style': 'gold', 'min': 4, 'max': 5},
              {'style': 'chromatic', 'min': 6}]},

    {'key': 'Set4_Elderwood', 'name': 'Elderwood', 'type': 'origin',
     'sets': [{'style': 'bronze', 'min': 3, 'max': 5}, {'style': 'gold', 'min': 6, 'max': 8},
              {'style': 'chromatic', 'min': 9}]},

    {'key': 'Set4_Enlightened', 'name': 'Enlightened', 'type': 'origin',
     'sets': [{'style': 'bronze', 'min': 2, 'max': 3}, {'style': 'silver', 'min': 4, 'max': 5},
              {'style': 'gold', 'min': 6}]},

    {'key': 'Set4_Exile', 'name': 'Exile', 'type': 'origin',
     'sets': [{'style': 'bronze', 'min': 1, 'max': 1}, {'style': 'gold', 'min': 2}]},

    {'key': 'Fortune', 'name': 'Fortune', 'type': 'origin',
     'sets': [{'style': 'gold', 'min': 3, 'max': 5}, {'style': 'chromatic', 'min': 6}]},

    {'key': 'Moonlight', 'name': 'Moonlight', 'type': 'origin',
     'sets': [{'style': 'gold', 'min': 3}]},

    {'key': 'Set4_Ninja', 'name': 'Ninja', 'type': 'origin',
     'sets': [{'style': 'bronze', 'min': 1, 'max': 1}, {'style': 'gold', 'min': 4, 'max': 4}]},

    {'key': 'Set4_Spirit', 'name': 'Spirit', 'type': 'origin',
     'sets': [{'style': 'bronze', 'min': 2, 'max': 3}, {'style': 'gold', 'min': 4}]},

    {'key': 'Boss', 'name': 'The Boss', 'type': 'origin',
     'sets': [{'style': 'gold', 'min': 1}]},

    {'key': 'Set4_Tormented', 'name': 'Tormented', 'type': 'origin',
     'sets': [{'style': 'gold', 'min': 1}]},

    {'key': 'Warlord', 'name': 'Warlord', 'type': 'origin',
     'sets': [{'style': 'bronze', 'min': 3, 'max': 5}, {'style': 'gold', 'min': 6, 'max': 8},
              {'style': 'chromatic', 'min': 9}]},

    {'key': 'Set4_Adept', 'name': 'Adept', 'type': 'class',
     'sets': [{'style': 'bronze', 'min': 2, 'max': 2}, {'style': 'gold', 'min': 3, 'max': 3},
              {'style': 'chromatic', 'min': 4}]},

    {'key': 'Set4_Assassin', 'name': 'Assassin', 'type': 'class',
     'sets': [{'style': 'bronze', 'min': 2, 'max': 3}, {'style': 'gold', 'min': 4, 'max': 5},
              {'style': 'chromatic', 'min': 6}]},

    {'key': 'Set4_Brawler', 'name': 'Brawler', 'type': 'class',
     'sets': [{'style': 'bronze', 'min': 2, 'max': 3}, {'style': 'silver', 'min': 4, 'max': 5},
              {'style': 'gold', 'min': 6, 'max': 7}, {'style': 'chromatic', 'min': 8}]},

    {'key': 'Set4_Dazzler', 'name': 'Dazzler', 'type': 'class',
     'sets': [{'style': 'bronze', 'min': 2, 'max': 3}, {'style': 'gold', 'min': 4}]},

    {'key': 'Duelist', 'name': 'Duelist', 'type': 'class',
     'sets': [{'style': 'bronze', 'min': 2, 'max': 3}, {'style': 'silver', 'min': 4, 'max': 5},
              {'style': 'gold', 'min': 6, 'max': 7}, {'style': 'chromatic', 'min': 8}]},

    {'key': 'Emperor', 'name': 'Emperor', 'type': 'class',
     'sets': [{'style': 'gold', 'min': 1, 'max': 1}]},

    {'key': 'Hunter', 'name': 'Hunter', 'type': 'class',
     'sets': [{'style': 'bronze', 'min': 2, 'max': 2}, {'style': 'silver', 'min': 3, 'max': 3},
              {'style': 'gold', 'min': 4, 'max': 4}, {'style': 'chromatic', 'min': 5}]},

    {'key': 'Keeper', 'name': 'Keeper', 'type': 'class',
     'sets': [{'style': 'bronze', 'min': 2, 'max': 3}, {'style': 'gold', 'min': 4, 'max': 5},
              {'style': 'chromatic', 'min': 6}]},

    {'key': 'Set4_Mage', 'name': 'Mage', 'type': 'class',
     'sets': [{'style': 'bronze', 'min': 3, 'max': 5}, {'style': 'gold', 'min': 6, 'max': 8},
              {'style': 'chromatic', 'min': 9}]},

    {'key': 'Set4_Mystic', 'name': 'Mystic', 'type': 'class',
     'sets': [{'style': 'bronze', 'min': 2, 'max': 3}, {'style': 'gold', 'min': 4, 'max': 5},
              {'style': 'chromatic', 'min': 6}]},

    {'key': 'Set4_Shade', 'name': 'Shade', 'type': 'class',
     'sets': [{'style': 'bronze', 'min': 2, 'max': 2}, {'style': 'gold', 'min': 3, 'max': 3},
              {'style': 'chromatic', 'min': 4}]},

    {'key': 'Sharpshooter', 'name': 'Sharpshooter', 'type': 'class',
     'sets': [{'style': 'bronze', 'min': 2, 'max': 3}, {'style': 'gold', 'min': 4, 'max': 5},
              {'style': 'chromatic', 'min': 6}]},

    {'key': 'Set4_Vanguard', 'name': 'Vanguard', 'type': 'class',
     'sets': [{'style': 'bronze', 'min': 2, 'max': 3}, {'style': 'silver', 'min': 4, 'max': 5},
              {'style': 'gold', 'min': 6}]}
]
# for my convenience
Cultist = 'Cultist';                    Divine = 'Divine'
Dusk = 'Dusk';                          Set4_Elderwood = 'Set4_Elderwood'
Set4_Enlightened = 'Set4_Enlightened';  Set4_Exile = 'Set4_Exile'
Fortune = 'Fortune';                    Moonlight = 'Moonlight'
Set4_Ninja = 'Set4_Ninja';              Set4_Spirit = 'Set4_Spirit'
Boss = 'Boss';                          Set4_Tormented = 'Set4_Tormented'
Warlord = 'Warlord';                    Set4_Adept = 'Set4_Adept'
Set4_Assassin = 'Set4_Assassin';        Set4_Brawler = 'Set4_Brawler'
Set4_Dazzler = 'Set4_Dazzler';          Duelist = 'Duelist'
Emperor = 'Emperor';                    Hunter = 'Hunter'
Keeper = 'Keeper';                      Set4_Mage = 'Set4_Mage'
Set4_Mystic = 'Set4_Mystic';            Set4_Shade = 'Set4_Shade'
Sharpshooter = 'Sharpshooter';          Set4_Vanguard = 'Set4_Vanguard'


get_trait_key_by_name = {}
for t in trait_list:
    get_trait_key_by_name[t["name"]] = t["key"]

champion_list = [
    {'name': 'Aatrox', 'championId': 'TFT4_Aatrox', 'cost': 4, 'traits': ['Cultist', 'Set4_Vanguard']},
    {'name': 'Ahri', 'championId': 'TFT4_Ahri', 'cost': 4, 'traits': ['Set4_Spirit', 'Set4_Mage']},
    {'name': 'Akali', 'championId': 'TFT4_Akali', 'cost': 3, 'traits': ['Set4_Ninja', 'Set4_Assassin']},
    {'name': 'Annie', 'championId': 'TFT4_Annie', 'cost': 2, 'traits': ['Fortune', 'Set4_Mage']},
    {'name': 'Aphelios', 'championId': 'TFT4_Aphelios', 'cost': 2, 'traits': ['Moonlight', 'Hunter']},
    {'name': 'Ashe', 'championId': 'TFT4_Ashe', 'cost': 4, 'traits': ['Set4_Elderwood', 'Hunter']},
    {'name': 'Azir', 'championId': 'TFT4_Azir', 'cost': 5, 'traits': ['Warlord', 'Keeper', 'Emperor']},
    {'name': "Cassiopeia", 'championId': 'TFT4_Cassiopeia', 'cost': 4, 'traits': ['Dusk', 'Set4_Mystic']},
    {'name': 'Diana', 'championId': 'TFT4_Diana', 'cost': 1, 'traits': ['Moonlight', 'Set4_Assassin']},
    {'name': 'Elise', 'championId': 'TFT4_Elise', 'cost': 1, 'traits': ['Cultist', 'Keeper']},
    {'name': 'Evelynn', 'championId': 'TFT4_Evelynn', 'cost': 3, 'traits': ['Cultist', 'Set4_Shade']},
    {'name': 'Ezreal', 'championId': 'TFT4_Ezreal', 'cost': 5, 'traits': ['Set4_Elderwood', 'Set4_Dazzler']},
    {'name': 'Fiora', 'championId': 'TFT4_Fiora', 'cost': 1, 'traits': ['Set4_Enlightened', 'Duelist']},
    {'name': 'Garen', 'championId': 'TFT4_Garen', 'cost': 1, 'traits': ['Warlord', 'Set4_Vanguard']},
    {'name': 'Hecarim', 'championId': 'TFT4_Hecarim', 'cost': 2, 'traits': ['Set4_Elderwood', 'Set4_Vanguard']},
    {'name': 'Irelia', 'championId': 'TFT4_Irelia', 'cost': 3, 'traits': ['Set4_Enlightened', 'Divine', 'Set4_Adept']},
    {'name': 'Janna', 'championId': 'TFT4_Janna', 'cost': 2, 'traits': ['Set4_Enlightened', 'Set4_Mystic']},
    {'name': 'Jarvin IV', 'championId': 'TFT4_JarvanIV', 'cost': 2, 'traits': ['Warlord', 'Keeper']},
    {'name': 'Jax', 'championId': 'TFT4_Jax', 'cost': 2, 'traits': ['Divine', 'Duelist']},
    {'name': 'Jhin', 'championId': 'TFT4_Jhin', 'cost': 4, 'traits': ['Cultist', 'Sharpshooter']},
    {'name': 'Jinx', 'championId': 'TFT4_Jinx', 'cost': 3, 'traits': ['Fortune', 'Sharpshooter']},
    {'name': 'Kalista', 'championId': 'TFT4_Kalista', 'cost': 3, 'traits': ['Cultist', 'Duelist']},
    {'name': 'Katarina', 'championId': 'TFT4_Katarina', 'cost': 3, 'traits': ['Warlord', 'Fortune', 'Set4_Assassin']},
    {'name': 'Kayn', 'championId': 'TFT4_Kayn', 'cost': 5, 'traits': ['Set4_Tormented', 'Set4_Shade']},
    {'name': 'Kennen', 'championId': 'TFT4_Kennen', 'cost': 3, 'traits': ['Set4_Ninja', 'Keeper']},
    {'name': 'Kindred', 'championId': 'TFT4_Kindred', 'cost': 3, 'traits': ['Set4_Spirit', 'Hunter']},
    {'name': 'Lee Sin', 'championId': 'TFT4_LeeSin', 'cost': 5, 'traits': ['Divine', 'Duelist']},
    {'name': 'Lillia', 'championId': 'TFT4_Lillia', 'cost': 5, 'traits': ['Dusk', 'Set4_Mage']},
    {'name': 'Lissandra', 'championId': 'TFT4_Lissandra', 'cost': 1, 'traits': ['Moonlight', 'Set4_Dazzler']},
    {'name': 'Lulu', 'championId': 'TFT4_Lulu', 'cost': 2, 'traits': ['Set4_Elderwood', 'Set4_Mage']},
    {'name': 'Lux', 'championId': 'TFT4_Lux', 'cost': 3, 'traits': ['Divine', 'Set4_Dazzler']},
    {'name': 'Maokai', 'championId': 'TFT4_Maokai', 'cost': 2, 'traits': ['Set4_Elderwood', 'Set4_Brawler']},
    {'name': 'Morgana', 'championId': 'TFT4_Morgana', 'cost': 4, 'traits': ['Set4_Enlightened', 'Set4_Dazzler']},
    {'name': 'Nami', 'championId': 'TFT4_Nami', 'cost': 1, 'traits': ['Set4_Enlightened', 'Set4_Mage']},
    {'name': 'Nidalee', 'championId': 'TFT4_Nidalee', 'cost': 1, 'traits': ['Warlord', 'Sharpshooter']},
    {'name': 'Nunu & Willump', 'championId': 'TFT4_Nunu', 'cost': 3, 'traits': ['Set4_Elderwood', 'Set4_Brawler']},
    {'name': 'Pyke', 'championId': 'TFT4_Pyke', 'cost': 2, 'traits': ['Cultist', 'Set4_Assassin']},
    {'name': 'Riven', 'championId': 'TFT4_Riven', 'cost': 4, 'traits': ['Dusk', 'Keeper']},
    {'name': 'Sejuani', 'championId': 'TFT4_Sejuani', 'cost': 4, 'traits': ['Fortune', 'Set4_Vanguard']},
    {'name': 'Sett', 'championId': 'TFT4_Sett', 'cost': 5, 'traits': ['Boss', 'Set4_Brawler']},
    {'name': 'Shen', 'championId': 'TFT4_Shen', 'cost': 4, 'traits': ['Set4_Ninja', 'Set4_Adept', 'Set4_Mystic']},
    {'name': 'Sylas', 'championId': 'TFT4_Sylas', 'cost': 2, 'traits': ['Moonlight', 'Set4_Brawler']},
    {'name': 'Tahm Kench', 'championId': 'TFT4_TahmKench', 'cost': 1, 'traits': ['Fortune', 'Set4_Brawler']},
    {'name': 'Talon', 'championId': 'TFT4_Talon', 'cost': 4, 'traits': ['Set4_Enlightened', 'Set4_Assassin']},
    {'name': 'Teemo', 'championId': 'TFT4_Teemo', 'cost': 2, 'traits': ['Set4_Spirit', 'Sharpshooter']},
    {'name': 'Thresh', 'championId': 'TFT4_Thresh', 'cost': 2, 'traits': ['Dusk', 'Set4_Vanguard']},
    {'name': 'Twisted Fate', 'championId': 'TFT4_TwistedFate', 'cost': 1, 'traits': ['Cultist', 'Set4_Mage']},
    {'name': 'Vayne', 'championId': 'TFT4_Vayne', 'cost': 1, 'traits': ['Dusk', 'Sharpshooter']},
    {'name': 'Veigar', 'championId': 'TFT4_Veigar', 'cost': 3, 'traits': ['Set4_Elderwood', 'Set4_Mage']},
    {'name': 'Vi', 'championId': 'TFT4_Vi', 'cost': 2, 'traits': ['Warlord', 'Set4_Brawler']},
    {'name': 'Warwick', 'championId': 'TFT4_Warwick', 'cost': 4, 'traits': ['Divine', 'Hunter', 'Set4_Brawler']},
    {'name': 'Wukong', 'championId': 'TFT4_Wukong', 'cost': 1, 'traits': ['Divine', 'Set4_Vanguard']},
    {'name': 'Xin Zhao', 'championId': 'TFT4_XinZhao', 'cost': 3, 'traits': ['Warlord', 'Duelist']},
    {'name': 'Yasuo', 'championId': 'TFT4_Yasuo', 'cost': 1, 'traits': ['Set4_Exile', 'Duelist']},
    {'name': 'Yone', 'championId': 'TFT4_Yone', 'cost': 5, 'traits': ['Set4_Exile', 'Set4_Adept']},
    {'name': 'Yuumi', 'championId': 'TFT4_Yuumi', 'cost': 3, 'traits': ['Set4_Spirit', 'Set4_Mystic']},
    {'name': 'Zed', 'championId': 'TFT4_Zed', 'cost': 2, 'traits': ['Set4_Ninja', 'Set4_Shade']},
    {'name': 'Zilean', 'championId': 'TFT4_Zilean', 'cost': 5, 'traits': ['Cultist', 'Set4_Mystic']}
]

# for my convenience
TFT4_Aatrox = 'TFT4_Aatrox';        TFT4_Ahri = 'TFT4_Ahri';                TFT4_Akali = 'TFT4_Akali'
TFT4_Annie = 'TFT4_Annie';          TFT4_Aphelios = 'TFT4_Aphelios';        TFT4_Ashe = 'TFT4_Ashe'
TFT4_Azir = 'TFT4_Azir';            TFT4_Cassiopeia = 'TFT4_Cassiopeia';    TFT4_Diana = 'TFT4_Diana'
TFT4_Elise = 'TFT4_Elise';          TFT4_Evelynn = 'TFT4_Evelynn';          TFT4_Ezreal = 'TFT4_Ezreal'
TFT4_Fiora = 'TFT4_Fiora';          TFT4_Garen = 'TFT4_Garen';              TFT4_Hecarim = 'TFT4_Hecarim'
TFT4_Irelia = 'TFT4_Irelia';        TFT4_Janna = 'TFT4_Janna';              TFT4_JarvanIV = 'TFT4_JarvanIV'
TFT4_Jax = 'TFT4_Jax';              TFT4_Jhin = 'TFT4_Jhin';                TFT4_Jinx = 'TFT4_Jinx'
TFT4_Kalista = 'TFT4_Kalista';      TFT4_Katarina = 'TFT4_Katarina';        TFT4_Kayn = 'TFT4_Kayn'
TFT4_Kennen = 'TFT4_Kennen';        TFT4_Kindred = 'TFT4_Kindred';          TFT4_LeeSin = 'TFT4_LeeSin'
TFT4_Lillia = 'TFT4_Lillia';        TFT4_Lissandra = 'TFT4_Lissandra';      TFT4_Lulu = 'TFT4_Lulu'
TFT4_Lux = 'TFT4_Lux';              TFT4_Maokai = 'TFT4_Maokai';            TFT4_Morgana = 'TFT4_Morgana'
TFT4_Nami = 'TFT4_Nami';            TFT4_Nidalee = 'TFT4_Nidalee';          TFT4_Nunu = 'TFT4_Nunu'
TFT4_Pyke = 'TFT4_Pyke';            TFT4_Riven = 'TFT4_Riven';              TFT4_Sejuani = 'TFT4_Sejuani'
TFT4_Sett = 'TFT4_Sett';            TFT4_Shen = 'TFT4_Shen';                TFT4_Sylas = 'TFT4_Sylas'
TFT4_TahmKench = 'TFT4_TahmKench';  TFT4_Talon = 'TFT4_Talon';              TFT4_Teemo = 'TFT4_Teemo'
TFT4_Thresh = 'TFT4_Thresh';        TFT4_TwistedFate = 'TFT4_TwistedFate';  TFT4_Vayne = 'TFT4_Vayne'
TFT4_Veigar = 'TFT4_Veigar';        TFT4_Vi = 'TFT4_Vi';                    TFT4_Warwick = 'TFT4_Warwick'
TFT4_Wukong = 'TFT4_Wukong';        TFT4_XinZhao = 'TFT4_XinZhao';          TFT4_Yasuo = 'TFT4_Yasuo'
TFT4_Yone = 'TFT4_Yone';            TFT4_Yuumi = 'TFT4_Yuumi';              TFT4_Zed = 'TFT4_Zed'
TFT4_Zilean = 'TFT4_Zilean'

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
    {'id': 18, 'name': 'Sword of the Divine'},
    {'id': 19, 'name': 'Infinity Edge'},
    {'id': 22, 'name': 'Rapid Firecannon'},
    {'id': 23, 'name': "Guinsoo's Rageblade"},
    {'id': 24, 'name': 'Statikk Shiv'},
    {'id': 25, 'name': "Titan's Resolve"},
    {'id': 26, 'name': "Runaan's Hurricane"},
    {'id': 27, 'name': "Zz'Rot Portal"},
    {'id': 28, 'name': "Duelist's Zeal"},
    {'id': 29, 'name': 'Last Whisper'},
    {'id': 33, 'name': "Rabadon's Deathcap"},
    {'id': 34, 'name': "Luden's Echo"},
    {'id': 35, 'name': 'Locket of the Iron Solari'},
    {'id': 36, 'name': 'Ionic Spark'},
    {'id': 37, 'name': 'Morellonomicon'},
    {'id': 38, 'name': "Aspect of Dusk"},
    {'id': 39, 'name': 'Jeweled Gauntlet'},
    {'id': 44, 'name': "Blue Buff"},
    {'id': 45, 'name': 'Frozen Heart'},
    {'id': 46, 'name': 'Chalice of Power'},
    {'id': 47, 'name': 'Redemption'},
    {'id': 48, 'name': "Mage's Hat"},
    {'id': 49, 'name': 'Hand Of Justice'},
    {'id': 55, 'name': 'Bramble Vest'},
    {'id': 56, 'name': 'Gargoyle Stoneplate'},
    {'id': 57, 'name': 'Sunfire Cape'},
    {'id': 58, 'name': 'Vanguard\'s Cuirass'},
    {'id': 59, 'name': 'Shroud of Stillness'},
    {'id': 66, 'name': "Dragon's Claw"},
    {'id': 67, 'name': 'Zephyr'},
    {'id': 68, 'name': 'Elderwood Sprout'},
    {'id': 69, 'name': 'Quicksilver'},
    {'id': 77, 'name': "Warmog's Armor"},
    {'id': 78, 'name': "Warlord's Banner"},
    {'id': 79, 'name': 'Trap Claw'},
    {'id': 88, 'name': 'Force of Nature'},
    {'id': 89, 'name': "Youmuu's Ghostblade"},
    {'id': 99, 'name': "Thief's Gloves"}
]
get_item_id_by_name = {}
for i in item_list:
    get_item_id_by_name[i["name"]] = i["id"]


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


def _get_traits(champions, items=[], chosen=""):
    traits_by_key = {}
    # get traits from champions
    for champion_id in champions:
        champion = None
        for champ in champion_list:
            if champ["championId"] == champion_id:
                champion = champ.copy()
                break;
        for trait in trait_list:
            champion_traits = champion["traits"]
            '''
            try:
                champion_traits = champion["traits"]
            except Exception as e:
                print(e)
                print(champion_id)
            '''
            if trait["key"] in champion_traits:
                if trait["key"] in traits_by_key:
                    traits_by_key[trait["key"]] += 1
                else:
                    traits_by_key[trait["key"]] = 1

    # get traits from items
    for i in range(len(items)):
        t = ""
        if items[i] == 18:
            t = "Divine"
        elif items[i] == 28:
            t = "Duelist"
        elif items[i] == 38:
            t = "Dusk"
        elif items[i] == 48:
            t = "Set4_Mage"
        elif items[i] == 58:
            t = "Set4_Vanguard"
        elif items[i] == 68:
            t = "Set4_Elderwood"
        elif items[i] == 78:
            t = "Warlord"
        elif items[i] == 98:
            t = "Set4_Assassin"
        traits_by_key[t] = traits_by_key.setdefault(t, 0) + 1

    # chosen trait
    if chosen != "":
        traits_by_key[chosen] = traits_by_key.setdefault(chosen, 0) + 1

    output = []
    # return trait key, num_units, tier
    for trait_n in traits_by_key:
        cnt = traits_by_key[trait_n]
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
        # 9Cultist
        "9Cultist": {
            "deck_vector": _make_deck_vector(
                [TFT4_Elise, TFT4_TwistedFate, TFT4_Pyke, TFT4_Evelynn, TFT4_Kalista,
                 TFT4_Aatrox, TFT4_Jhin, TFT4_Zilean]),
            "carry_champion": [],
            "traits": _get_traits([TFT4_Elise, TFT4_TwistedFate, TFT4_Pyke, TFT4_Evelynn, TFT4_Kalista,
                                   TFT4_Aatrox, TFT4_Jhin, TFT4_Zilean], chosen="Cultist"),
            "main_traits": [
                {'name': "Cultist", 'tier_current': 3}
            ]
        },

        # Moonlight
        "Moonlight": {
            "deck_vector": _make_deck_vector(
                [TFT4_Lissandra, TFT4_Aphelios, TFT4_Sylas, TFT4_Kindred, TFT4_Yuumi, TFT4_Ashe, TFT4_Cassiopeia,
                 TFT4_Warwick]),
            "carry_champion": [TFT4_Aphelios],
            "traits": _get_traits([TFT4_Lissandra, TFT4_Aphelios, TFT4_Sylas, TFT4_Kindred, TFT4_Yuumi, TFT4_Ashe, TFT4_Cassiopeia,
                                   TFT4_Warwick]),
            "main_traits": [
                {'name': Moonlight, 'tier_current': 1},
                {'name': Hunter, 'tier_current': 3}
            ]
        },

        # elderwood family
        "Elderwood 8Brawler": {
            "deck_vector": _make_deck_vector(
                [TFT4_Maokai, TFT4_TahmKench, TFT4_Sylas, TFT4_Vi, TFT4_Nunu, TFT4_Ashe, TFT4_Warwick, TFT4_Sett]),
            "carry_champion": [TFT4_Ashe, TFT4_Sett],
            "traits": _get_traits([TFT4_Maokai, TFT4_TahmKench, TFT4_Sylas, TFT4_Vi, TFT4_Nunu, TFT4_Ashe, TFT4_Warwick,
                                   TFT4_Sett], chosen=Set4_Brawler),
            "main_traits": [
                {'name': Set4_Brawler, 'tier_current': 4},
                {'name': Set4_Elderwood, 'tier_current': 1},
                {'name': Hunter, 'tier_current': 1}
            ]
        },

        "6Elderwood 4Brawler": {
            "deck_vector": _make_deck_vector(
                [TFT4_Maokai, TFT4_Hecarim, TFT4_Nunu, TFT4_Ashe, TFT4_Sejuani, TFT4_Warwick, TFT4_Sett, TFT4_Ezreal]),
            "carry_champion": [TFT4_Ashe, TFT4_Sett],
            "traits": _get_traits([TFT4_Maokai, TFT4_Hecarim, TFT4_Nunu, TFT4_Ashe, TFT4_Sejuani, TFT4_Warwick,
                                   TFT4_Sett, TFT4_Ezreal], chosen=Set4_Elderwood),
            "main_traits": [
                {'name': Set4_Brawler, 'tier_current': 2},
                {'name': Set4_Elderwood, 'tier_current': 2},
                {'name': Hunter, 'tier_current': 1}
            ]
        },

        "9Elderwood": {
            "deck_vector": _make_deck_vector(
                [TFT4_Maokai, TFT4_Hecarim, TFT4_Lulu, TFT4_Nunu, TFT4_Veigar, TFT4_Ashe, TFT4_Warwick, TFT4_Ezreal,
                 TFT4_Sett]),
            "carry_champion": [TFT4_Ashe, TFT4_Sett, TFT4_Ezreal],
            "traits": _get_traits([TFT4_Maokai, TFT4_Hecarim, TFT4_Lulu, TFT4_Nunu, TFT4_Veigar, TFT4_Ashe,
                                   TFT4_Warwick, TFT4_Ezreal, TFT4_Sett], items=[68], chosen=Set4_Elderwood),
            "main_traits": [
                {'name': Set4_Brawler, 'tier_current': 4},
                {'name': Set4_Elderwood, 'tier_current': 1},
                {'name': Hunter, 'tier_current': 1}
            ]
        },

        # Sharpshooter
        "6Sharpshooter": {
            "deck_vector": _make_deck_vector(
                [TFT4_Nidalee, TFT4_Vayne, TFT4_Teemo, TFT4_Jinx, TFT4_Yuumi, TFT4_Aatrox, TFT4_Jhin, TFT4_Sejuani,
                 TFT4_Zilean]),
            "carry_champion": [TFT4_Jinx, TFT4_Jhin],
            "traits": _get_traits([TFT4_Nidalee, TFT4_Vayne, TFT4_Teemo, TFT4_Jinx, TFT4_Yuumi, TFT4_Aatrox, TFT4_Jhin,
                                   TFT4_Sejuani, TFT4_Zilean], chosen=Sharpshooter),
            "main_traits": [
                {'name': Sharpshooter, 'tier_current': 3},
                {'name': Set4_Spirit, 'tier_current': 1},
                {'name': Set4_Vanguard, 'tier_current': 1}
            ]
        },

        "6Sharpshooter 4Keeper": {
            "deck_vector": _make_deck_vector(
                [TFT4_Nidalee, TFT4_Vayne, TFT4_JarvanIV, TFT4_Teemo, TFT4_Jinx, TFT4_Kennen, TFT4_Jhin,
                 TFT4_Riven, TFT4_Azir]),
            "carry_champion": [TFT4_Jinx, TFT4_Jhin, TFT4_Riven],
            "traits": _get_traits([TFT4_Nidalee, TFT4_Vayne, TFT4_JarvanIV, TFT4_Teemo, TFT4_Jinx, TFT4_Kennen,
                                   TFT4_Jhin, TFT4_Riven, TFT4_Azir], chosen=Sharpshooter),
            "main_traits": [
                {'name': Sharpshooter, 'tier_current': 3},
                {'name': Keeper, 'tier_current': 2}
            ]
        },

        "6Enlightened": {
            "deck_vector": _make_deck_vector(
                [TFT4_Nami, TFT4_Janna, TFT4_Pyke, TFT4_Irelia, TFT4_Lux, TFT4_Morgana, TFT4_Shen, TFT4_Talon]),
            "carry_champion": [TFT4_Morgana, TFT4_Talon],
            "traits": _get_traits([TFT4_Nami, TFT4_Janna, TFT4_Pyke, TFT4_Irelia, TFT4_Lux, TFT4_Morgana, TFT4_Shen,
                                   TFT4_Talon]),
            "main_traits": [
                {'name': Set4_Enlightened, 'tier_current': 3},
                {'name': Set4_Assassin, 'tier_current': 1}
            ]
        },

        # Zed carry
        "Spirit Shade": {
            "deck_vector": _make_deck_vector(
                [TFT4_Teemo, TFT4_Zed, TFT4_Evelynn, TFT4_Kindred, TFT4_Yuumi, TFT4_Ahri, TFT4_Kayn]),
            "carry_champion": [TFT4_Zed],
            "traits": _get_traits([TFT4_Teemo, TFT4_Zed, TFT4_Evelynn, TFT4_Kindred, TFT4_Yuumi, TFT4_Ahri, TFT4_Kayn]),
            "main_traits": [
                {'name': Set4_Shade, 'tier_current': 2},
                {'name': Set4_Spirit, 'tier_current': 2}
            ]
        },

        "Ninja Shade": {
            "deck_vector": _make_deck_vector(
                [TFT4_Pyke, TFT4_Zed, TFT4_Akali, TFT4_Evelynn, TFT4_Kennen, TFT4_Shen, TFT4_Kayn, TFT4_Zilean]),
            "carry_champion": [TFT4_Zed, TFT4_Evelynn],
            "traits": _get_traits([TFT4_Pyke, TFT4_Zed, TFT4_Akali, TFT4_Evelynn, TFT4_Kennen, TFT4_Shen, TFT4_Kayn,
                                   TFT4_Zilean]),
            "main_traits": [
                {'name': Set4_Ninja, 'tier_current': 2},
                {'name': Set4_Shade, 'tier_current': 3}
            ]
        },

        # Nin Am
        "Ninja Assassin": {
            "deck_vector": _make_deck_vector(
                [TFT4_Diana, TFT4_Pyke, TFT4_Zed, TFT4_Akali, TFT4_Katarina, TFT4_Kennen, TFT4_Shen, TFT4_Talon]),
            "carry_champion": [TFT4_Akali, TFT4_Talon],
            "traits": _get_traits([TFT4_Diana, TFT4_Pyke, TFT4_Zed, TFT4_Akali, TFT4_Katarina, TFT4_Kennen, TFT4_Shen,
                                   TFT4_Talon], chosen=Set4_Assassin),
            "main_traits": [
                {'name': Set4_Ninja, 'tier_current': 2},
                {'name': Set4_Assassin, 'tier_current': 3}
            ]
        },

        "6Duelist": {
            "deck_vector": _make_deck_vector(
                [TFT4_Fiora, TFT4_Yasuo, TFT4_Jax, TFT4_Kalista, TFT4_XinZhao,
                 TFT4_Shen, TFT4_LeeSin, TFT4_Yone]),
            "carry_champion": [TFT4_Kalista, TFT4_Yone],
            "traits": _get_traits([TFT4_Fiora, TFT4_Yasuo, TFT4_Jax, TFT4_Kalista, TFT4_XinZhao,
                                   TFT4_Shen, TFT4_LeeSin, TFT4_Yone]),
            "main_traits": [
                {'name': "Duelist", 'tier_current': 3},
                {'name': "Set4_Exile", 'tier_current': 2}
            ]
        },
        "Spirit 6Mage": {
            "deck_vector": _make_deck_vector(
                ["TFT4_Nami", "TFT4_Annie", "TFT4_Lulu", "TFT4_Veigar", "TFT4_Yuumi",
                 "TFT4_Ahri", "TFT4_Cassiopeia", "TFT4_Lillia"]),
            "carry_champion": ["TFT4_Ahri"],
            "traits": _get_traits(["TFT4_Nami", "TFT4_Annie", "TFT4_Lulu", "TFT4_Veigar", "TFT4_Yuumi",
                                   "TFT4_Ahri", "TFT4_Cassiopeia", "TFT4_Lillia"]),
            "main_traits": [
                {'name': "Set4_Spirit", 'tier_current': 1},
                {'name': "Set4_Mage", 'tier_current': 2}
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
                    if main_trait["key"] not in self.trait_names:
                        is_trait_accomplished = False
                        break

                    d_trait = self.traits[self.trait_names.index(main_trait["key"])]
                    if d_trait["tier_current"] < main_trait["tier_current"]:
                        is_trait_accomplished = False
                        break
                self.is_accomplished = is_trait_accomplished
            return meta_name, max_std_similarity
        return "etc", 0
