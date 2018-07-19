import subprocess
import os

def update():


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
