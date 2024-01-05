# sqlalchemy-challenge

SQLalchemy and Flask challenge

This challenge involves querying weather data with the use of python and SQLalchemy. Additionally, our findings will be used in our Flask API.
To begin, created an engine to the data and reflected its tables. References were saved to these tables created our session. We queried to find the most recent date in the data set. Using this information, we were able to calculate one year before this time. The data for the past 12 months was then queried, put into a data frame and plotted using matplotlib.

   The next part of our research involved the stations which took the readings and measurements that we used previously. Through various queries, the most active station was found and its reading from the past 12 months was also put into a data frame and plotted as a histogram.

Finally, the final leg of this project involved designing an API to allow for exploration and interaction with our findings during the previous sections. Flask was used to create an API and several routes were created for use. Specifically, a route for precipitation data, station data, and temperature were created. Additionally, the final routes allow for users to enter a start date to return all temperature data starting from that point, as well as a route for users to enter a specific range of dates they wish to query. 
