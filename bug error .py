def distance(kms,ms):
    if kms < 20:
        print("close")
    elif kms < 50:
        print("median")
    else:
        print("far")
distance(20,30)