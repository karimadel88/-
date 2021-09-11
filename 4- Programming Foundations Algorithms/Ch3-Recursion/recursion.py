def countDown(x):
    if x == 0:
        print("Done")
        return
    else:
        print(x, "count down ...")
        return countDown(x-1)


countDown(5)
