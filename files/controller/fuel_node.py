controller_dir = target_dir + '/fuel-master/'
try:
  os.mkdir(controller_dir)
except:
  pass

os.system('fuel nodes > /etc/fuel-nodes')
files = ['/var/log/', '/etc/my.cnf', '/etc/mysql/', '/etc/fuel-nodes', '/etc/fuel-uuid', '/etc/naily.facts', '/etc/nailgun/', '/etc/naily/', '/etc/haproxy/']
for file in files:
  os.system('cp -a ' + file + ' ' + controller_dir)

