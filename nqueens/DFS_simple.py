import time

n = 13
sol = [0] * n
count = 0

def DFS(row):
    global count
    for col in range(n):
        # 检查冲突
        ok = True
        for i in range(row):
            if col == sol[i] or col - sol[i]== row -i or col - sol[i]==i-row:
                ok = False
                break
        if not ok:
            continue
        # 检查冲突结束
        if row == n-1:
            count +=1
        else:
            sol[row] = col
            DFS(row +1)

if __name__=="__main__":
    # 主程序
    tic = time.time()
    DFS(0)                          # 从第 0 行开始试探
    toc = time.time()
    print("Total solutions: %d" % count)
    print("Elapsed time: %f seconds" % (toc - tic))