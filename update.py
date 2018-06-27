import subprocess
import os

def update():
### change Direcctory name if needed
	directory = subprocess.check_output("find / -type d -name \"Spector\" ",shell = True)
	line =directory.splitlines()[0]  ###
	
	try:
		os.chdir(line)
		#cwd = os.getcwd()
		#print cwd

		local = subprocess.check_output(r"git log -1  --pretty=format:\"%H ",shell = True)
		local= local.decode("utf-8")[1:41]

		
### Github Link 
		remote = subprocess.check_output(r"git ls-remote https://github.com/mxamusic/Spector.git refs/heads/master",shell = True) 
		remote=remote.decode("utf-8")[:40]
		
		#print('running commit : ' +local) 
		#print('current commit : '+remote)
		
		if local != remote:
			subprocess.check_output("git fetch --all",shell = True)
			subprocess.check_output("git reset --hard origin/master",shell = True)
			subprocess.check_output("git pull origin master",shell = True)
### realese Number ????!!			
			print('Done updating  .. Version!!!!')
	
	except subprocess.CalledProcessError as e:
		print (e.output.decode("utf-8"))
		




