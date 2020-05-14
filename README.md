# EEnergy
EEnergy API for knowing the nearby energy resources locations and notifying participants if it's viable to form a mircogrid with their neighbors thus saving energy and reducing the load on the main grid


### Built With

* python (Django/DRF)
* PostgreSQL with PostGIS extension for supporting spatial features in the PostgreSQL database
* Docker
  
  
 #### Features Implemented
 * user registeration/login/logout and token authentication handled with rest_auth/allauth
 * each user can be an energy resource owner
 * each energy resource have (generation-owner consumption- net energy- location represented by a geographic point)
 
 #####TODO
 1. divide the world map intro equal districts of a suitable area
 2. each district should have a state whether it is a viable microgrid or not and active microgrid or not 
 3. notify users who are owners if energy resources in a microgrid district
  
PS. the project is under development
