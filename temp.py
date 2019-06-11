def Sinput(acceptable):
    while True:
        acceptable = [str(i) for i in acceptable]
        a = input('Enter {} or {} :'.format(' ,'.join(acceptable[:-1]), acceptable[-1]))
        if a in acceptable:
            return a
            break

a = Sinput([ 1, 2.01, '\'cat\'', 'dog'])
print a
