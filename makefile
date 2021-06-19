REPO = https://github.com/99004324-MehulKothari/Genesis_Ltts_Python.git
MESSAGE = "updates"

clone:
	git clone $(REPO)

add:
	git add --all
	
commit:
	git commit -m $(MESSAGE)
	
push:
	git push
	
pull:
	git pull $(REPO) main
