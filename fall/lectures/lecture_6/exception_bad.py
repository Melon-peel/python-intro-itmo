# this example is bad, because catching this way leads to catching system-level exceptions either
while True:
    try:
        input()
    except BaseException:
        print("ha-ha!")