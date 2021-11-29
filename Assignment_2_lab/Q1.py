def flip_float_parts(fnum):
    fnum = str(fnum)
    revB = int(fnum[fnum.index(".")-1::-1])
    revF = fnum[fnum.index(".")+1::1]
    fstr = revF+"."+str(revB)
    fnum = float(fstr)
    return fnum


num = flip_float_parts(11.63)
print(num)
