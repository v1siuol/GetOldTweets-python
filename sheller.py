def new_cmd(date, end):
	return 'python Exporter.py --querysearch "pepsi" --since 2017-03-' + date + ' --until 2017-03-' + end + ' --output output_got_pepsi_201703' + date + '.csv'

def fillStr(num):
	if num < 10:
		return '0' + str(num)
	else:
		return str(num)

start = 3

while start < 10:
	print new_cmd(fillStr(start), fillStr(start+1))
	start += 1

