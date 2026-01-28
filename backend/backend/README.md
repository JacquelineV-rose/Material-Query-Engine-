#Material Query Engine 
Goal: Create the simple material query engine
Input query: Free text
Output: List of relevant material (base on description + literature references) in
table format
 ID: the candidate can choose the method how to generate the ID, must
explain why they choose that method.
 pretty_formula
 Energy Above Hull
 Space Group
 Band Gap
 Predicted Formation Energy
 Magnetic Ordering
 Total Magnetization
 Experimentally Observed
When clicked on the ID, open the detail information page and have a download
function/button which allows users to download the json file.
Requirements:
 Datasize: >=100
 Literature Regerences: All material must have literature references (can
find in Materal Info)
 Database: Elasticsearch
 Data source: https://next-gen.materialsproject.org/



In this project I created the search query.

I started by collecting material data from the Materials Project using their Python API client. I created the list of required fields so that when when it goes to extract the data it knows what to take. 

Then it saves this data into the api_results.json


For the ID I just used material_id because the API was structured that way and I took note of it when I looked at the design example. 

I then created the index and details which were created because I used Flask for the webpage. I cd into the folder with the elasticsearch and ran it, then used Flask for the webpage. 
Flask was responsible for routing between index and details and serving static files

Users can type into a search bar and click "Search" to query the dataset. The filter_Materials() function sends the query to a Flask route, which filters the JSON data 

Matching results are rendered in a table using JavaScript’s .forEach() to loop through and display them.

To avoid freezing the page with too much data I only display search results after the query is made. This is handled by the display() function, which clears any previous results before loading new ones.


Routing.py allowed me to route everything together with my URLS and such so that I could just run that to connect all of it for the webpage. The backend checks if the query matches any part of the material’s formula, ID, or magnetic ordering, then returns the filtered list using jsonify()
. 

I use this to structure the data. I check to see if the query involves the specified material being searched to get rid of excess data being displayed. 


The detail.html page is what you are taken to when you click the material_ID. It does this by extracting the route of material_Id from the URL


I had the styles.css just to make it dark mode because I believe it is easier to read this way. 

