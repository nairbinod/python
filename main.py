
from comedy import laugh, please_clap
from outdated_technologies import local_tools

def check_marketing_is_funny(any_reaction):
	please_clap()
	if any_reaction:
		return laugh()
		
		
	else:
		return laugh()

def choose_IDE(choice, coding_together):
	if coding_together:
		return "go to https://repl.it"
	elif choice in local_tools:
		return "go to https://repl.it"
	else:
		return "go to https://repl.it anyway"


print(choose_IDE('replit', True))
print(check_marketing_is_funny('its clearly not'))