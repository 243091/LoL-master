def win_rate(ch_id, gdata):
    """Calculates champion win rate based on provided global data

    @param ch_id: int, champion id
    @param gdata: matrix of global data, where each row represents one match;
    @returns: champion win rate
    """

    win, n = 0, 0
    for match in gdata:
        champs = match[:10]
        if ch_id in champs:
            k = champs.index(ch_id)
            if k < 5:
                win += match[-1]
            else:
                win += int(match[-1] == 0)
            n += 1

    if n == 0:
        return 0
    else:
        return win / n


def syn(ch_id1, ch_id2, gdata):
    """Calculates synergy of two champions based on provided global data

    @param ch_id1: int, first champion id
    @param ch_id2: int, second champion id
    @param gdata: matrix of global data, where each row represents one match;
    @returns: synergy of two champions
    """

    win, n = 0, 0
    for match in gdata:
        champs = match[:10]
        if (ch_id1 in champs[:5] and ch_id2 in champs[:5]) \
                or (ch_id1 in champs[5:] and ch_id2 in champs[5:]):
            k = champs.index(ch_id1)
            if k < 5:
                win += match[-1]
            else:
                win += int(match[-1] == 0)
            n += 1

    if n == 0:
        return 0
    else:
        return win / n


def synergy(champs, gdata):
    """Calculates synergy feature based on provided global data

    @param champs: list with champions id that are in a match; first 5 from blue team, next red team
    @param gdata: matrix of global data, where each row represents one match;
    @returns: synergy feature
    """

    from itertools import combinations as com
    s = 0
    for i in com(champs[:5], 2):
        s += syn(i[0], i[1], gdata)

    for i in com(champs[5:], 2):
        s -= syn(i[0], i[1], gdata)

    return s


def ctr(ch_id1, ch_id2, gdata):
    """Calculates counter of two champions based on provided global data

    @param ch_id1: int, first champion id
    @param ch_id2: int, second champion id
    @param gdata: matrix of global data, where each row represents one match;
    @returns: counter of two champions
    """

    win, n = 0, 0
    for match in gdata:
        champs = match[:10]
        if (ch_id1 in champs[:5] and ch_id2 in champs[5:]) \
                or (ch_id1 in champs[5:] and ch_id2 in champs[:5]):
            k = champs.index(ch_id1)
            if k < 5:
                win += match[-1]
            else:
                win += int(match[-1] == 0)
            n += 1

    if n == 0:
        return 0
    else:
        return win / n


def counter(champs, gdata):
    """Calculates counter feature based on provided global data

    @param champs: list with champions id that are in a match; first 5 from blue team, next red team
    @param gdata: matrix of global data, where each row represents one match;
    @returns: counter feature
    """

    c = 0
    for i in range(5):
        for j in range(5, 10):
            c += ctr(champs[i], champs[j], gdata)

    return c

