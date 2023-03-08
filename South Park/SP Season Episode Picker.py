alphabet = 'abcdefghijklmnopqrstuvwxyz'
data = {1:13, 2:18, 3:17, 4:17, 5:14, 6:17, 7:15, 8:14, 9:14, 10:14, 11:14, 12:14, 13:14, 14:14, 15:14, 16:14, 17:10, 18:10, 19:10, 20:10, 21:10, 22:10, 23:10, 24:2, 25:6, 26:6}

# Calculates episode / season number
def Calculate(n, words, i):
    # loop for sum of the indexes of the letters from alphabet where 'a' is index 1
    total = 0
    for letter in words[i]:
        total += ( alphabet.index(letter) + 1 ) % 10

    # Modulo n. where n is number of seasons or number of episodes in a certain season.
    total = total % n
    return total

# Takes 2 words as input, converts to a list.
words = input('2words: ').lower()
words = words.split(' ')[:2]

Season = Calculate(26,words,0)
Episode = Calculate(data[Season],words,1)

print(f'Season: {Season}\nEpisode: {Episode}')