# researching interaction with lichess API

# public endpoing: explorer.lichess.ovh/lichess

import berserk
import os
import requests
import concurrent.futures
import itertools

token = os.getenv("API_KEY")

session = berserk.TokenSession(token)
client = berserk.Client(session=session)

def get_lichess_opening_moves(fen):
    url = f"https://explorer.lichess.ovh/lichess?variant=standard&fen={fen}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # print(data)
        # return data.get('moves', [])
        # print(dict(itertools.islice(data.items(), 4)))
        return dict(itertools.islice(data.items(), 4)) # we should optimize here to make sure we aren't grabbing rare variations
        # I think it will be more efficient to just set a conditional to be met since we are still requesting anyway
    else:
        print(f"Failed to get data: {response.status_code}")
        return []

# Example FEN for the starting position
fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
metadata = get_lichess_opening_moves(fen)
next_moves = metadata['moves']
number_games = int(metadata['white']) + int(metadata['black']) + int(metadata['draws'])

# Print the moves
for next_move in next_moves:
    # getting rid of the get method for now
    # you should be checking the rate of play the absolute number

    # actually maybe we can do this for the black and white sides at the same time?

    vari_percentage = 
    win_rate = (int(next_move['white']) / (int(next_move['white']) + int(next_move['black']) + int(next_move['draws']))) * 100
    print(f"Move: {next_move['uci']}, White Win Rate: {win_rate:.4g}%")


# for now what if we let a user enter a position and then we can write a dfs algorithm to check if there are any trappy moves there