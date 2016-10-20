all: clean

clean:
	rm -rf choicemaster/choicemaster/*.pyc
	rm -rf choicemaster/choicemaster/*~
	rm -rf choicemaster/app/*.pyc
	rm -rf choicemaster/app/*~
	rm -rf choicemaster/app/user/*.pyc
	rm -rf choicemaster/app/user/*~
	rm -rf choicemaster/templates/*~
