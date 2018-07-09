import subprocess
import os

def update():
### Search for Spector direcory
###	*** Choose only the first directory path if multiple paths is returned ***
	os.chdir(os.path.expanduser("~"))
	try :
		cmd = r"sudo find / -type d -name Spector -print -quit  2>/dev/null"
		directory = subprocess.check_output(cmd , stderr=subprocess.STDOUT, shell = True )

		line =directory.splitlines()[0]  ###
		print(line )
	except subprocess.CalledProcessError as e:
        	print(e)
        	exit(1)
### change directory to spector directory to be able to use git commands
	os.chdir(line)
### get current local Commit_ID
	try:
		local = subprocess.check_output(r"git log -1  --pretty=format:\"%H ",shell = True)
		local= local.decode("utf-8")[1:41]


### get latest commit_ID at the remote repo
		remote = subprocess.check_output(r"git ls-remote https://github.com/mxamusic/Spector.git refs/heads/master",shell = True)
		remote=remote.decode("utf-8")[:40]

		print('running commit : ' +local)
		print('current commit : '+remote)
### compare  and update if not equal
		if local != remote:
			subprocess.check_output("git fetch --all",shell = True)
			subprocess.check_output("git reset --hard origin/master",shell = True)
			subprocess.check_output("git pull origin master",shell = True)
### realese Number ????!!
			print('Done updating  .. Version!!!!')

	except subprocess.CalledProcessError as e:
		print (e.output.decode("utf-8"))




update()
