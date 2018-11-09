import sys
import htmlParser
import yaml
import os

path = os.path.dirname(os.path.realpath(__file__))

with open(path + "\\urls.yaml", 'r') as stream:
	try:
		config = yaml.load(stream)
		
		try:
			restaurant = str(sys.argv[1])
			url = config[restaurant]
			htmlParser.chooseParser(url)
		except:
			# If there's no argument, just take the first URL
			url = list(config.values())[0]
			htmlParser.chooseParser(url)
	
	except yaml.YAMLError as e:
		print(e)