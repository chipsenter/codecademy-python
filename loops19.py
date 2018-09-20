dirtbikes = ['Kawasaki', 'Honda', 'Suzuki', 'Yamaha', 'Ktm', 'Can-Am']

print 'You have...'
for d in dirtbikes:
  if d == 'Can-Am':
    print 'A Can-Am is not a dirtbike!' # (It actually is.)
  print 'A', d
else:
  print 'A great selection of dirtbikes!'    