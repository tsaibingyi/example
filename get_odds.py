def get_odds(a):
	result={} #{}是字典的意思,詳細用法在我給你的那本書的p2-7有
	n=0
	for i in range(a):
		if i%2==1:
			n+=1 #n在這裡表示第n個奇數
			result[n]=i #將字典中“鍵”的值設為i,表示第n個奇數是i
	return result

out=get_odds(10) #會得到一個字典{ 1:1, 2:3, 3:54:7,5:9}
print(out[3])