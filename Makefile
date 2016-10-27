all: clean

clean:
	rm -rf choicemaster/choicemaster/*.pyc
	rm -rf choicemaster/choicemaster/*~
	rm -rf choicemaster/app/*.pyc
	rm -rf choicemaster/app/*~
	rm -rf choicemaster/app/exam/*.pyc
	rm -rf choicemaster/app/exam/*~
	rm -rf choicemaster/templates/*~
	rm -rf *~
