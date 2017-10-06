#################################################
# Script to make Solr Calls using the sql handler
#################################################

import requests
import subprocess
from bs4 import BeautifulSoup

__author__ = 'Gayatri Ghanakota'



class SolrQueryHandler():
	def __init__(self,query):
		"""
		Initiates an object with the parameters passed which is
		the sql query which will be passed on to the solr sql 
		handler
		"""
		self.query = query

	def getResults(self):
		"""
		This function takes in the sql query and calls the solr 
		sql handler and returns back the results
		"""
		query = self.query
		command = "curl --data-urlencode 'stmt="+query+ " ' 'http://localhost:8983/solr/gettingstarted/sql?aggregationMode=facet'"
		print command
		p = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
		out, err = p.communicate()
		return out


	def getCollections():
		"""
		This functions returns back the list of collections in solr
		"""
		collection_list = []
		html = requests.get('http://localhost:8983/solr/admin/collections?action=LIST')
		soup = BeautifulSoup(html.text,"lxml")
		collections = soup.find('arr')
		for ele in collections:
        		collection_list.append(ele.getText())
            
        	return collection_list

