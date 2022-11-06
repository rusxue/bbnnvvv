
def rannum(样本,总数):
    x=1
    for i in range(1,样本):
        x*=(总数-i)/总数
    return 1-x

print(rannum(200,1000000))