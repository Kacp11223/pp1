def mask(card):
    return ''.join(['*' if i > 1 and i < len(card)-4 else card[i] for i in range(len(card))])
