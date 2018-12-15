import os
import csv
import pandas as pd

def is_furikae(now_row):
	result = []
	for list in furikaelist:
		if row[2] == list[0] and row[4] == list[1]:
			result = now_row[:]
			result[3] = -1 * int(row[3])
			result[4] = list[2]
	return result

csvlist=[]
furikaelist = [ \
  ['口座振替4 ラクテンカ-ドサ-ビ','三菱UFJ銀行','楽天カード'], \
  ['JCB JCBカ-ド','三菱UFJ銀行','JCBカード（スタシア）'], \
  ['J-WESTカ-ド','みずほ銀行','JCBカード（JR）'], \
  ['口座振替 (カ)ジエーシービー','住信SBIネット銀行','JCBカード（オリジナル）'], \
  ['ジエ-シ-ビ-','みずほ銀行','JCBカード（オリジナル）'], \
  ['振込 ホンニンザイケイ','みずほ銀行','三菱UFJ銀行'], \
  ['ネツト カ)ジエ-シ-ビ-','みずほ銀行','JCBカード（オリジナル）'], \
  ['振替/定期 IB','三菱UFJ銀行','三菱UFJ銀行'], \
  ['振替/定期','三菱UFJ銀行','三菱UFJ銀行'], \
]
is_first = True

for nowfile in os.listdir():
	if ".csv" in nowfile and "収入・支出詳細_" in nowfile:
		csvlist.append(nowfile)

outfile = open('result.csv','w')
writer = csv.writer(outfile, lineterminator='\n')

for filename in csvlist:
	infile = open(filename, "r")
	reader = csv.reader(infile)
	header = next(reader)
	if is_first:
		writer.writerow(header)
		is_first = False
	for row in reader:
		furikae = is_furikae(row)
		if furikae:
			writer.writerow(furikae)
		writer.writerow(row)
	infile.close()

outfile.close()


