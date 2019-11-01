import random

def file_to_dict(fname):
	ans = {}
	f = open(fname)
	for line in f.readlines():
		try:
			ans[line.split(",")[0]] = float(line.split(",")[1])
		except:
			pass
	ans.pop("Total")
	return ans

def choose_rand(values):
	rand = random.random() * 100
	print("Our number is", rand)
	total = 0
	for x in values:
		total += values[x]
		if rand < total:
			print(x)
			return
	print("Other")


def main():
	vals = file_to_dict("occupations.csv")
	choose_rand(vals)



main()
