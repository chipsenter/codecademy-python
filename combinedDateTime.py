from datetime import datetime
now = datetime.now()

#print '%02d-%02d-%04d' % (now.month, now.day, now.year)
print '%02d/%02d/%04d %02d:%02d:%02d' % (now.month , now.day , now.year , now.hour +6, now.minute , now.second) 