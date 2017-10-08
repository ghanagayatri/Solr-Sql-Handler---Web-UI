# Solr-Sql-Handler - Web-UI
Built a UI using Django on top of the Solr Sql Handler. This works only with Solr 6.6.1


### Start & Stop Solr in Cloud Mode ###
1. bin/solr -e cloud
2. bin/solr stop -all

### How to Use the SQL Handler for Solr ###

Step 1: You will need to run Solr in SolrCloud mode.

Step 2: And indexing some data right after SolrCloud is started:

bin/post -c gettingstarted example/exampledocs/*.xml

Step 3: Let’s retrieve all documents from the gettingstarted collection that have the field inStock equal to true.To do that using the default query parser in Solr we would run the following command:

curl 'localhost:8983/solr/gettingstarted/select?q=inStock:true&fl=id,title&indent=true'

Step 4: curl --data-urlencode 'stmt=select id,name from gettingstarted where inStock = 'true'' http://localhost:8983/solr/gettingstarted/sql

curl --data-urlencode 'stmt=select id,name from gettingstarted where inStock = 'true'' 'http://localhost:8983/solr/gettingstarted/sql?aggregationMode=facet'

curl --data-urlencode 'stmt=select distinct id as distId from gettingstarted where inStock = 'true' order by id desc' 'http://localhost:8983/solr/gettingstarted/sql?aggregationMode=facet'


### References ###
1. http://www.solrtutorial.com/solr-in-5-minutes.html
2. https://sematext.com/blog/2016/04/18/solr-6-solrcloud-sql-support/

Here is how the UI looks like:

![alt text](https://github.com/ghanagayatri/Solr-Sql-Handler---Web-UI/blob/master/Screen%20Shot%202017-10-07%20at%209.33.05%20PM.png)
