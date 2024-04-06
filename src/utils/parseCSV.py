from datetime import datetime
import pandas as pd

# Load the CSV file to examine its contents
file_path = './ranking.csv'
data = pd.read_csv(file_path)
data['movement'] = 0
# Selecting only the relevant columns and renaming them to match the JSON structure
json_data = data.rename(columns={'nickname': 'nickname', 
                                 'profileLink': 'profileLink', 
                                 'position': 'position', 
                                 'faceit_elo': 'faceit_elo', 
                                 'game_skill_level': 'game_skill_level',
                                 'id': 'id'})

# Convert the DataFrame to a list of dictionaries to resemble JSON objects
json_list = json_data.to_dict(orient='records')

# Display the first few to ensure accuracy
json_list

# {
# 			id: 'LOL_LMA0',
# 			position: 2,
# 			nickname: 'Xaka',
# 			faceit_elo: 2914,
# 			game_skill_level: 10,
# 			profileLink: 'https://www.faceit.com/en/players/LOL_LMA0',
# 			movement: 0
# 		},
# 		{
# 			id: '-slinger',
# 			position: 3,
# 			nickname: '-slinger',
# 			faceit_elo: 2809,
# 			game_skill_level: 10,
# 			profileLink: 'https://www.faceit.com/en/players/-slinger',
# 			movement: 0
# 		},
# 		{
# 			id: 'zE',
# 			position: 4,
# 			nickname: 'zE',
# 			faceit_elo: 2561,
# 			game_skill_level: 10,
# 			profileLink: 'https://www.faceit.com/en/players/zE',
# 			movement: 0
# 		},
# 		{
# 			id: 'kioshimqx',
# 			position: 5,
# 			nickname: 'kioshimqx',
# 			faceit_elo: 2520,
# 			game_skill_level: 10,
# 			profileLink: 'https://www.faceit.com/en/players/kioshimqx',
# 			movement: 0
# 		},
# 		{
# 			id: 'chrixus-',
# 			position: 6,
# 			nickname: 'Chrixus-',
# 			faceit_elo: 2427,
# 			game_skill_level: 10,
# 			profileLink: 'https://www.faceit.com/en/players/chrixus-',
# 			movement: 0
# 		},
# 		{
# 			id: 'HOUNGOUNGAGN',
# 			position: 7,
# 			nickname: 'HOUNGOUNGAGN',
# 			faceit_elo: 2397,
# 			game_skill_level: 10,
# 			profileLink: 'https://www.faceit.com/en/players/HOUNGOUNGAGN',
# 			movement: 0
# 		},
# 		{
# 			id: 'Zelli0n',
# 			position: 8,
# 			nickname: 'Zelli0n',
# 			faceit_elo: 2396,
# 			game_skill_level: 10,
# 			profileLink: 'https://www.faceit.com/en/players/Zelli0n',
# 			movement: 0
# 		},
# 		{
# 			id: 'Bidule',
# 			position: 9,
# 			nickname: 'Bidule',
# 			faceit_elo: 2325,
# 			game_skill_level: 10,
# 			profileLink: 'https://www.faceit.com/en/players/Bidule',
# 			movement: 0
# 		},
# 		{
# 			id: 'Trevor033',
# 			position: 10,
# 			nickname: 'Trevor033',
# 			faceit_elo: 2233,
# 			game_skill_level: 10,
# 			profileLink: 'https://www.faceit.com/en/players/Trevor033',
# 			movement: 0
# 		},
# 		{
# 			id: '-zrz',
# 			position: 11,
# 			nickname: '-zrz',
# 			faceit_elo: 2206,
# 			game_skill_level: 10,
# 			profileLink: 'https://www.faceit.com/en/players/-zrz',
# 			movement: 0
# 		},
# 		{
# 			id: 'mejta',
# 			position: 12,
# 			nickname: 'mejta',
# 			faceit_elo: 2144,
# 			game_skill_level: 10,
# 			profileLink: 'https://www.faceit.com/en/players/mejta',
# 			movement: 0
# 		},
# 		{
# 			id: '-keith',
# 			position: 13,
# 			nickname: '-keith',
# 			faceit_elo: 2140,
# 			game_skill_level: 10,
# 			profileLink: 'https://www.faceit.com/en/players/-keith',
# 			movement: 0
# 		},
# 		{
# 			id: 'DR_DRU',
# 			position: 14,
# 			nickname: 'DR_DRU',
# 			faceit_elo: 2085,
# 			game_skill_level: 10,
# 			profileLink: 'https://www.faceit.com/en/players/DR_DRU',
# 			movement: 0
# 		},
# 		{
# 			id: 'stekel1',
# 			position: 15,
# 			nickname: 'stekel1',
# 			faceit_elo: 2062,
# 			game_skill_level: 10,
# 			profileLink: 'https://www.faceit.com/en/players/stekel1',
# 			movement: 0
# 		},
# 		{
# 			id: 'Lukez3ra',
# 			position: 16,
# 			nickname: 'Lukez3ra',
# 			faceit_elo: 2042,
# 			game_skill_level: 10,
# 			profileLink: 'https://www.faceit.com/en/players/Lukez3ra',
# 			movement: 0
# 		},
# 		{
# 			id: 'Sixoku',
# 			position: 17,
# 			nickname: 'Sixoku',
# 			faceit_elo: 2031,
# 			game_skill_level: 10,
# 			profileLink: 'https://www.faceit.com/en/players/Sixoku',
# 			movement: 0
# 		},
# 		{
# 			id: 'RikoduSenin',
# 			position: 18,
# 			nickname: 'RikoduSenin',
# 			faceit_elo: 1995,
# 			game_skill_level: 9,
# 			profileLink: 'https://www.faceit.com/en/players/RikoduSenin',
# 			movement: 0
# 		},
# 		{
# 			id: 'zero_RTK',
# 			position: 19,
# 			nickname: 'seesharp',
# 			faceit_elo: 1929,
# 			game_skill_level: 9,
# 			profileLink: 'https://www.faceit.com/en/players/zero_RTK',
# 			movement: 0
# 		},
# 		{
# 			id: 'left0ver_',
# 			position: 20,
# 			nickname: 'left0ver_',
# 			faceit_elo: 1912,
# 			game_skill_level: 9,
# 			profileLink: 'https://www.faceit.com/en/players/left0ver_',
# 			movement: 0
# 		},
# 		{
# 			id: 'exehh',
# 			position: 21,
# 			nickname: 'exehh',
# 			faceit_elo: 1900,
# 			game_skill_level: 9,
# 			profileLink: 'https://www.faceit.com/en/players/exehh',
# 			movement: 0
# 		},
# 		{
# 			id: 'KD-4',
# 			position: 22,
# 			nickname: 'KD-4',
# 			faceit_elo: 1849,
# 			game_skill_level: 9,
# 			profileLink: 'https://www.faceit.com/en/players/KD-4',
# 			movement: 0
# 		},
# 		{
# 			id: 'MysticMind',
# 			position: 23,
# 			nickname: 'MysticMind',
# 			faceit_elo: 1845,
# 			game_skill_level: 9,
# 			profileLink: 'https://www.faceit.com/en/players/MysticMind',
# 			movement: 0
# 		},
# 		{
# 			id: 'wixinho',
# 			position: 24,
# 			nickname: 'wixinho',
# 			faceit_elo: 1799,
# 			game_skill_level: 9,
# 			profileLink: 'https://www.faceit.com/en/players/wixinho',
# 			movement: 0
# 		},
# 		{
# 			id: 'YRNxUchiha-',
# 			position: 25,
# 			nickname: 'YRNxUchiha-',
# 			faceit_elo: 1662,
# 			game_skill_level: 8,
# 			profileLink: 'https://www.faceit.com/en/players/YRNxUchiha-',
# 			movement: 0
# 		},
# 		{
# 			id: 'Scorpyy_',
# 			position: 26,
# 			nickname: 'ScoRp1oNX',
# 			faceit_elo: 1634,
# 			game_skill_level: 8,
# 			profileLink: 'https://www.faceit.com/en/players/Scorpyy_',
# 			movement: 0
# 		},
# 		{
# 			id: 'Samazzo',
# 			position: 27,
# 			nickname: 'Samazzo',
# 			faceit_elo: 1629,
# 			game_skill_level: 8,
# 			profileLink: 'https://www.faceit.com/en/players/Samazzo',
# 			movement: 0
# 		},
# 		{
# 			id: 'Eneko',
# 			position: 28,
# 			nickname: 'Eneko',
# 			faceit_elo: 1623,
# 			game_skill_level: 8,
# 			profileLink: 'https://www.faceit.com/en/players/Eneko',
# 			movement: 0
# 		},
# 		{
# 			id: 'prasalgado',
# 			position: 29,
# 			nickname: 'prasalgado',
# 			faceit_elo: 1519,
# 			game_skill_level: 7,
# 			profileLink: 'https://www.faceit.com/en/players/prasalgado',
# 			movement: 0
# 		},
# 		{
# 			id: 'BungyCS',
# 			position: 30,
# 			nickname: 'BungyCS',
# 			faceit_elo: 1497,
# 			game_skill_level: 7,
# 			profileLink: 'https://www.faceit.com/en/players/BungyCS',
# 			movement: 0
# 		},
# 		{
# 			id: 'iiKavallo',
# 			position: 31,
# 			nickname: 'iiKavallo',
# 			faceit_elo: 1489,
# 			game_skill_level: 7,
# 			profileLink: 'https://www.faceit.com/en/players/iiKavallo',
# 			movement: 0
# 		},
# 		{
# 			id: 'xMaNtiS',
# 			position: 32,
# 			nickname: 'xMaNtiS',
# 			faceit_elo: 1480,
# 			game_skill_level: 7,
# 			profileLink: 'https://www.faceit.com/en/players/xMaNtiS',
# 			movement: 0
# 		},
# 		{
# 			id: 'BajMT',
# 			position: 33,
# 			nickname: 'BajMT',
# 			faceit_elo: 1459,
# 			game_skill_level: 7,
# 			profileLink: 'https://www.faceit.com/en/players/BajMT',
# 			movement: 0
# 		},
# 		{
# 			id: '-Djele-',
# 			position: 34,
# 			nickname: '-Djele-',
# 			faceit_elo: 1445,
# 			game_skill_level: 7,
# 			profileLink: 'https://www.faceit.com/en/players/-Djele-',
# 			movement: 0
# 		},
# 		{
# 			id: 'haxa__',
# 			position: 35,
# 			nickname: 'haxa__',
# 			faceit_elo: 1416,
# 			game_skill_level: 7,
# 			profileLink: 'https://www.faceit.com/en/players/haxa__',
# 			movement: 0
# 		},
# 		{
# 			id: 'TermIn1440p',
# 			position: 36,
# 			nickname: 'TermIn1440p',
# 			faceit_elo: 1399,
# 			game_skill_level: 7,
# 			profileLink: 'https://www.faceit.com/en/players/TermIn1440p',
# 			movement: 0
# 		},
# 		{
# 			id: 'PreZ_-',
# 			position: 37,
# 			nickname: 'PreZ_-',
# 			faceit_elo: 1386,
# 			game_skill_level: 7,
# 			profileLink: 'https://www.faceit.com/en/players/PreZ_-',
# 			movement: 0
# 		},
# 		{
# 			id: 'Zelli0n',
# 			position: 38,
# 			nickname: 'notifyycs',
# 			faceit_elo: 1372,
# 			game_skill_level: 7,
# 			profileLink: 'https://www.faceit.com/en/players/Zelli0n',
# 			movement: 0
# 		},
# 		{
# 			id: 'Dionegrech',
# 			position: 39,
# 			nickname: 'Dionegrech',
# 			faceit_elo: 1372,
# 			game_skill_level: 7,
# 			profileLink: 'https://www.faceit.com/en/players/Dionegrech',
# 			movement: 0
# 		},
# 		{
# 			id: 'Findagdar',
# 			position: 40,
# 			nickname: 'Findagdar',
# 			faceit_elo: 1362,
# 			game_skill_level: 7,
# 			profileLink: 'https://www.faceit.com/en/players/Findagdar',
# 			movement: 0
# 		},
# 		{
# 			id: 'FaceFear_',
# 			position: 41,
# 			nickname: 'FaceFear_',
# 			faceit_elo: 1330,
# 			game_skill_level: 6,
# 			profileLink: 'https://www.faceit.com/en/players/FaceFear_',
# 			movement: 0
# 		},
# 		{
# 			id: '1mppp',
# 			position: 42,
# 			nickname: '1mppp',
# 			faceit_elo: 1325,
# 			game_skill_level: 6,
# 			profileLink: 'https://www.faceit.com/en/players/1mppp',
# 			movement: 0
# 		},
# 		{
# 			id: 'tr1x--',
# 			position: 43,
# 			nickname: 'tr1x--',
# 			faceit_elo: 1302,
# 			game_skill_level: 6,
# 			profileLink: 'https://www.faceit.com/en/players/tr1x--',
# 			movement: 0
# 		},
# 		{
# 			id: 'PKmlt',
# 			position: 44,
# 			nickname: 'PKmlt',
# 			faceit_elo: 1292,
# 			game_skill_level: 6,
# 			profileLink: 'https://www.faceit.com/en/players/PKmlt',
# 			movement: 0
# 		},
# 		{
# 			id: '-wxlfie-',
# 			position: 45,
# 			nickname: '-wxlfie-',
# 			faceit_elo: 1281,
# 			game_skill_level: 6,
# 			profileLink: 'https://www.faceit.com/en/players/-wxlfie-',
# 			movement: 0
# 		},
# 		{
# 			id: 'ARcheN',
# 			position: 46,
# 			nickname: 'ARcheN',
# 			faceit_elo: 1215,
# 			game_skill_level: 6,
# 			profileLink: 'https://www.faceit.com/en/players/ARcheN',
# 			movement: 0
# 		},
# 		{
# 			id: 'M3ga_MT',
# 			position: 47,
# 			nickname: 'M3ga_MT',
# 			faceit_elo: 1209,
# 			game_skill_level: 6,
# 			profileLink: 'https://www.faceit.com/en/players/M3ga_MT',
# 			movement: 0
# 		},
# 		{
# 			id: 'An6rA',
# 			position: 48,
# 			nickname: 'An6rA',
# 			faceit_elo: 1193,
# 			game_skill_level: 5,
# 			profileLink: 'https://www.faceit.com/en/players/An6rA',
# 			movement: 0
# 		},
# 		{
# 			id: 'Myst1cMind',
# 			position: 49,
# 			nickname: 'Myst1cMind',
# 			faceit_elo: 1193,
# 			game_skill_level: 5,
# 			profileLink: 'https://www.faceit.com/en/players/Myst1cMind',
# 			movement: 0
# 		},
# 		{
# 			id: 'Matli',
# 			position: 50,
# 			nickname: 'Matli',
# 			faceit_elo: 1181,
# 			game_skill_level: 5,
# 			profileLink: 'https://www.faceit.com/en/players/Matli',
# 			movement: 0
# 		},
# 		{
# 			id: 'disa',
# 			position: 51,
# 			nickname: 'disa',
# 			faceit_elo: 1173,
# 			game_skill_level: 5,
# 			profileLink: 'https://www.faceit.com/en/players/disa',
# 			movement: 0
# 		},
# 		{
# 			id: 'DupremeMLT',
# 			position: 52,
# 			nickname: 'DupremeMLT',
# 			faceit_elo: 1172,
# 			game_skill_level: 5,
# 			profileLink: 'https://www.faceit.com/en/players/DupremeMLT',
# 			movement: 0
# 		},
# 		{
# 			id: 'ChubyDik',
# 			position: 53,
# 			nickname: 'ChubyDik',
# 			faceit_elo: 1166,
# 			game_skill_level: 5,
# 			profileLink: 'https://www.faceit.com/en/players/ChubyDik',
# 			movement: 0
# 		},
# 		{
# 			id: 'Frosted--',
# 			position: 54,
# 			nickname: 'Frosted--',
# 			faceit_elo: 1159,
# 			game_skill_level: 5,
# 			profileLink: 'https://www.faceit.com/en/players/Frosted--',
# 			movement: 0
# 		},
# 		{
# 			id: 'fireflymt',
# 			position: 55,
# 			nickname: 'fireflymt',
# 			faceit_elo: 1147,
# 			game_skill_level: 5,
# 			profileLink: 'https://www.faceit.com/en/players/fireflymt',
# 			movement: 0
# 		},
# 		{
# 			id: 'Ac3_JV',
# 			position: 56,
# 			nickname: 'Ac3_JV',
# 			faceit_elo: 1141,
# 			game_skill_level: 5,
# 			profileLink: 'https://www.faceit.com/en/players/Ac3_JV',
# 			movement: 0
# 		},
# 		{
# 			id: 'Dece1ve-',
# 			position: 57,
# 			nickname: 'Dece1ve-',
# 			faceit_elo: 1139,
# 			game_skill_level: 5,
# 			profileLink: 'https://www.faceit.com/en/players/Dece1ve-',
# 			movement: 0
# 		},
# 		{
# 			id: 'GBreezy9',
# 			position: 58,
# 			nickname: 'GBreezy9',
# 			faceit_elo: 1137,
# 			game_skill_level: 5,
# 			profileLink: 'https://www.faceit.com/en/players/GBreezy9',
# 			movement: 0
# 		},
# 		{
# 			id: 'Pocho--',
# 			position: 59,
# 			nickname: 'Pocho--',
# 			faceit_elo: 1132,
# 			game_skill_level: 5,
# 			profileLink: 'https://www.faceit.com/en/players/Pocho--',
# 			movement: 0
# 		},
# 		{
# 			id: 'Nos-MT',
# 			position: 60,
# 			nickname: 'Nos-MT',
# 			faceit_elo: 1125,
# 			game_skill_level: 5,
# 			profileLink: 'https://www.faceit.com/en/players/Nos-MT',
# 			movement: 0
# 		},
# 		{
# 			id: 'luca8k',
# 			position: 61,
# 			nickname: 'luca8k',
# 			faceit_elo: 1114,
# 			game_skill_level: 5,
# 			profileLink: 'https://www.faceit.com/en/players/luca8k',
# 			movement: 0
# 		},
# 		{
# 			id: 'D_lete_',
# 			position: 62,
# 			nickname: 'D_lete_',
# 			faceit_elo: 1067,
# 			game_skill_level: 5,
# 			profileLink: 'https://www.faceit.com/en/players/D_lete_',
# 			movement: 0
# 		},
# 		{
# 			id: 'Cush1mg',
# 			position: 63,
# 			nickname: 'Cush1mg',
# 			faceit_elo: 1055,
# 			game_skill_level: 5,
# 			profileLink: 'https://www.faceit.com/en/players/Cush1mg',
# 			movement: 0
# 		},
# 		{
# 			id: 'Lockstockmt',
# 			position: 64,
# 			nickname: 'Lockstockmt',
# 			faceit_elo: 1055,
# 			game_skill_level: 5,
# 			profileLink: 'https://www.faceit.com/en/players/Lockstockmt',
# 			movement: 0
# 		},
# 		{
# 			id: 'Ssgtluke',
# 			position: 65,
# 			nickname: 'Ssgtluke',
# 			faceit_elo: 1038,
# 			game_skill_level: 4,
# 			profileLink: 'https://www.faceit.com/en/players/Ssgtluke',
# 			movement: 0
# 		},
# 		{
# 			id: 'JKGod-',
# 			position: 66,
# 			nickname: 'JKGod-',
# 			faceit_elo: 1030,
# 			game_skill_level: 4,
# 			profileLink: 'https://www.faceit.com/en/players/JKGod-',
# 			movement: 0
# 		},
# 		{
# 			id: 'boratmalt',
# 			position: 67,
# 			nickname: 'boratmalt',
# 			faceit_elo: 1007,
# 			game_skill_level: 4,
# 			profileLink: 'https://www.faceit.com/en/players/boratmalt',
# 			movement: 0
# 		},
# 		{
# 			id: 'Nos_MT',
# 			position: 68,
# 			nickname: 'Nos_MT',
# 			faceit_elo: 1006,
# 			game_skill_level: 4,
# 			profileLink: 'https://www.faceit.com/en/players/Nos_MT',
# 			movement: 0
# 		},
# 		{
# 			id: 'Astris',
# 			position: 69,
# 			nickname: 'Astris',
# 			faceit_elo: 1004,
# 			game_skill_level: 4,
# 			profileLink: 'https://www.faceit.com/en/players/Astris',
# 			movement: 0
# 		},
# 		{
# 			id: 'Ktulu99',
# 			position: 70,
# 			nickname: 'Ktulu99',
# 			faceit_elo: 1000,
# 			game_skill_level: 4,
# 			profileLink: 'https://www.faceit.com/en/players/Ktulu99',
# 			movement: 0
# 		},
# 		{
# 			id: 'ShocKeRMT',
# 			position: 71,
# 			nickname: 'ShocKeRMT',
# 			faceit_elo: 987,
# 			game_skill_level: 4,
# 			profileLink: 'https://www.faceit.com/en/players/ShocKeRMT',
# 			movement: 0
# 		},
# 		{
# 			id: 'damien1698',
# 			position: 72,
# 			nickname: 'damien1698',
# 			faceit_elo: 984,
# 			game_skill_level: 4,
# 			profileLink: 'https://www.faceit.com/en/players/damien1698',
# 			movement: 0
# 		},
# 		{
# 			id: 'DotRyan',
# 			position: 73,
# 			nickname: 'DotRyan',
# 			faceit_elo: 972,
# 			game_skill_level: 4,
# 			profileLink: 'https://www.faceit.com/en/players/DotRyan',
# 			movement: 0
# 		},
# 		{
# 			id: 'G1bsoNNN',
# 			position: 74,
# 			nickname: 'G1bsoNNN',
# 			faceit_elo: 965,
# 			game_skill_level: 4,
# 			profileLink: 'https://www.faceit.com/en/players/G1bsoNNN',
# 			movement: 0
# 		},
# 		{
# 			id: '-TuNiN',
# 			position: 75,
# 			nickname: '-TuNiN',
# 			faceit_elo: 965,
# 			game_skill_level: 4,
# 			profileLink: 'https://www.faceit.com/en/players/-TuNiN',
# 			movement: 0
# 		},
# 		{
# 			id: 'MEONN',
# 			position: 76,
# 			nickname: 'MEONN',
# 			faceit_elo: 956,
# 			game_skill_level: 4,
# 			profileLink: 'https://www.faceit.com/en/players/MEONN',
# 			movement: 0
# 		},
# 		{
# 			id: 'kingniBBa',
# 			position: 77,
# 			nickname: 'kingniBBa',
# 			faceit_elo: 947,
# 			game_skill_level: 4,
# 			profileLink: 'https://www.faceit.com/en/players/kingniBBa',
# 			movement: 0
# 		},
# 		{
# 			id: 'Ilaizm20',
# 			position: 78,
# 			nickname: 'Ilaizm20',
# 			faceit_elo: 945,
# 			game_skill_level: 4,
# 			profileLink: 'https://www.faceit.com/en/players/Ilaizm20',
# 			movement: 0
# 		},
# 		{
# 			id: 'Lukestivala',
# 			position: 79,
# 			nickname: 'Lukestivala',
# 			faceit_elo: 900,
# 			game_skill_level: 3,
# 			profileLink: 'https://www.faceit.com/en/players/Lukestivala',
# 			movement: 0
# 		},
# 		{
# 			id: 'MeloMlt',
# 			position: 80,
# 			nickname: 'MeloMlt',
# 			faceit_elo: 898,
# 			game_skill_level: 3,
# 			profileLink: 'https://www.faceit.com/en/players/MeloMlt',
# 			movement: 0
# 		},
# 		{
# 			id: 'CichyJanek',
# 			position: 81,
# 			nickname: 'CichyJanek',
# 			faceit_elo: 866,
# 			game_skill_level: 3,
# 			profileLink: 'https://www.faceit.com/en/players/CichyJanek',
# 			movement: 0
# 		},
# 		{
# 			id: 'Undisputed01',
# 			position: 82,
# 			nickname: 'Undisputed01',
# 			faceit_elo: 864,
# 			game_skill_level: 3,
# 			profileLink: 'https://www.faceit.com/en/players/Undisputed01',
# 			movement: 0
# 		},
# 		{
# 			id: 'slotzz__',
# 			position: 83,
# 			nickname: 'slotzz__',
# 			faceit_elo: 863,
# 			game_skill_level: 3,
# 			profileLink: 'https://www.faceit.com/en/players/slotzz__',
# 			movement: 0
# 		},
# 		{
# 			id: 'xMilyy',
# 			position: 84,
# 			nickname: 'xMilyy',
# 			faceit_elo: 809,
# 			game_skill_level: 3,
# 			profileLink: 'https://www.faceit.com/en/players/xMilyy',
# 			movement: 0
# 		},
# 		{
# 			id: 'b0bz31',
# 			position: 85,
# 			nickname: 'b0bz31',
# 			faceit_elo: 803,
# 			game_skill_level: 3,
# 			profileLink: 'https://www.faceit.com/en/players/b0bz31',
# 			movement: 0
# 		},
# 		{
# 			id: 'xixxi',
# 			position: 86,
# 			nickname: 'xixxi',
# 			faceit_elo: 801,
# 			game_skill_level: 3,
# 			profileLink: 'https://www.faceit.com/en/players/xixxi',
# 			movement: 0
# 		},
# 		{
# 			id: 'cissu1',
# 			position: 87,
# 			nickname: 'cissu1',
# 			faceit_elo: 799,
# 			game_skill_level: 3,
# 			profileLink: 'https://www.faceit.com/en/players/cissu1',
# 			movement: 0
# 		},
# 		{
# 			id: 'UniHorseHD',
# 			position: 88,
# 			nickname: 'UniHorseHD',
# 			faceit_elo: 789,
# 			game_skill_level: 3,
# 			profileLink: 'https://www.faceit.com/en/players/UniHorseHD',
# 			movement: 0
# 		},
# 		{
# 			id: 'arogan178',
# 			position: 89,
# 			nickname: 'arogan178',
# 			faceit_elo: 713,
# 			game_skill_level: 2,
# 			profileLink: 'https://www.faceit.com/en/players/arogan178',
# 			movement: 0
# 		},
# 		{
# 			id: 'kalanc',
# 			position: 90,
# 			nickname: 'kalanc',
# 			faceit_elo: 707,
# 			game_skill_level: 2,
# 			profileLink: 'https://www.faceit.com/en/players/kalanc',
# 			movement: 0
# 		},
# 		{
# 			id: 'Manthen',
# 			position: 91,
# 			nickname: 'Manthen',
# 			faceit_elo: 703,
# 			game_skill_level: 2,
# 			profileLink: 'https://www.faceit.com/en/players/Manthen',
# 			movement: 0
# 		},
# 		{
# 			id: 'Giannerz',
# 			position: 92,
# 			nickname: 'Giannerz',
# 			faceit_elo: 606,
# 			game_skill_level: 2,
# 			profileLink: 'https://www.faceit.com/en/players/Giannerz',
# 			movement: 0
# 		}