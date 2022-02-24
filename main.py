patterns = [
	"example pattern with a [keyword]"
]

keywords = [
	"first_keyword",
	"second_keyword"
]

f = open("export.txt", "w")

for keyword in keywords:
	for pattern in patterns:
		start = pattern.find("[") + 1
		end = pattern.find("]")

		if (start == -1 or end == -1):
			f.write("[WARNING] : No pattern found in :" + pattern + "\n")
			continue

		variable = pattern[start:end]
		if (variable == ""):
			f.write("[WARNING] : Variable is empty in :" + pattern + "\n")
			continue

		first_part = pattern[0:start-1]

		if (end == len(pattern)):
			last_part = ""
		else:
			last_part = pattern[end+1:len(pattern)]

		f.write(first_part + keyword + last_part + "\n")
		f.write("\"" + first_part + keyword + last_part + "\"\n")
		f.write("[" + first_part + keyword + last_part + "]\n")
	f.write("\n")

f.close()
	