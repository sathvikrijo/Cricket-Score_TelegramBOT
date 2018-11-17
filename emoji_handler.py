from emoji import emojize

def get_emoji(value):
    if value == 1:
        emoji_returned = emojize(':one:', use_aliases=True)
    elif value == 2:
        emoji_returned = emojize(':two:',use_aliases=True)
    elif value == 3:
        emoji_returned = emojize(':three:',use_aliases=True)
    elif value == 4:
        emoji_returned = emojize(':four:',use_aliases=True)
    elif value == 5:
        emoji_returned = emojize(':five:',use_aliases=True)
    elif value == 6:
        emoji_returned = emojize(':six:',use_aliases=True)
    elif value == 7:
        emoji_returned = emojize(':seven:',use_aliases=True)
    elif value == 8:
        emoji_returned = emojize(':eight:',use_aliases=True)
    elif value == 9:
        emoji_returned = emojize(':nine:',use_aliases=True)
    elif value == 10:
        emoji_returned = emojize(':ten:',use_aliases=True)
    elif value == 11:
        emoji_returned = emojize(':one::one:',use_aliases=True)
    elif value == 12:
        emoji_returned = emojize(':one::two:',use_aliases=True)
    elif value == 13:
        emoji_returned = emojize(':one::three:',use_aliases=True)
    elif value == 14:
        emoji_returned = emojize(':one::four:',use_aliases=True)
    elif value == 15:
        emoji_returned = emojize(':one::five:',use_aliases=True)
    elif value == 16:
        emoji_returned = emojize(':one::six:',use_aliases=True)
    elif value == 17:
        emoji_returned = emojize(':one::seven:',use_aliases=True)
    elif value == 18:
        emoji_returned = emojize(':one::eight:',use_aliases=True)
    elif value == 19:
        emoji_returned = emojize(':one::nine:',use_aliases=True)
    elif value == 20:
        emoji_returned = emojize(':two::zero:',use_aliases=True)
    return emoji_returned
