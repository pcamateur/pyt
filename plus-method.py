for r in range(1, 10):
    for c in range(1, r + 1):
        print(' {} + {} = {}'.format(c, r, c + r), end = '\t')
        
    print()