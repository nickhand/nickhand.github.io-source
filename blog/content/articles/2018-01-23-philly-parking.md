Title: An Interactive Look at Parking Tickets in Philadelphia
date: 2018-01-23 21:00
comments: true
slug: philly-parking
tags: philadelphia, parking, dataviz, open-data, dc.js, d3.js

<!-- PELICAN_BEGIN_SUMMARY -->

{% img /blog/images/parking_tickets_map.jpg An interactive density map of tickets across Philly %}

I recently moved back to Philadelphia after finishing my
astrophysics PhD at Berkeley. To get reacquainted with my hometown, I began
exploring the treasure trove of data that is
[OpenDataPhilly](https://www.opendataphilly.org).
With over 300 public datasets, there's a lot to dig in to. I started
with the parking violation data, which ranges from 2012 to 2016. The data
offered a good chance to learn some of the latest data viz tools.
Namely, I took advantage of the open source
javascript library [dc.js](https://dc-js.github.io/dc.js/), which neatly ties
together the [d3.js](https://d3js.org) and
[crossfilter](http://square.github.io/crossfilter/) tools.
Here, I'll discuss these tools as well as some of the trends that
jumped out of the ticketing data.  

The data visualization is up and running at <http://nickhand.pythonanywhere.com>,
and the source code is hosted on my
[GitHub](https://github.com/nickhand/philly-parking-violations).
Keep reading for the gritty details, or otherwise, happy exploring!

<!-- PELICAN_END_SUMMARY -->

## The data

The data is available on
[Philly's open data website](https://www.opendataphilly.org/dataset/parking-violations).
In addition to hosting the data, the portal also links to several previous
analyses and visualizations that have been done since the data was first published
back in 2015. These include an analysis by
[philly.com](http://data.philly.com/philly/parking/]), a series of maps
by [Tony Smith and Ken Steif](https://imgur.com/a/TgxYw), and a visualization
by the [city itself](https://data.phila.gov/visualizations/parking-violations).
These visualizations focus mainly on the entirety of the data, spanning
several years, and are great for detecting seasonal and year-to-year trends.
I wanted to dig into the data on a more granular level, so
I decided to focus on monthly trends. This also helped limit the size of the data
(and load times for users) and keep the interactive features running smoothly.

I downloaded the data in a CSV format and wrote a
[short Python script](https://github.com/nickhand/philly-parking-violations/blob/master/clean-data.py) to
pre-process and clean the data set. I needed to fix a few inconsistencies with
the data; most importantly, the latitude/longitude coordinates for a portion of
the data set seemed to be mislabeled and needed to be reversed. And since I was
looking at the data on a month-by-month basis, I also needed to partition the
data by month into separate files. This was all easily accomplished using the
[Pandas](http://pandas.pydata.org) Python library. I ended up with 60 data files
stored in JSON format, covering 2012 through 2016. Each data file stored the
following attributes about each parking ticket issued during those years:
latitude, longitude, timestamp, fine amount, zip code, day of week, hour,
ticket description, issuing agency, and street location.

## Making the visualization

The app visualizes the parking ticket data in the following ways:

- the total number of tickets and total fine amount
- a table showing the top 10 most common ticket locations
- a bar chart showing the number of tickets per hour
- a row chart showing the number of tickets for each zip code in the city
- a heat map showing the number of tickets as a function of hour and day of week
- an interactive map showing the density of tickets across the city using hexagonal binning
- a row chart showing the number of tickets for each ticket type
- a row chart giving the number of tickets grouped by issuing agency

All of the above, except for the interactive map, can be achieved using
the [dc](https://dc-js.github.io/dc.js/) javascript library. It leverages
[d3](https://d3js.org) to produce reactive charts in the browser and supports
[crossfilter](http://crossfilter.github.io/crossfilter/) to allow users to
easily filter and explore the data. Once you
define the dimensions of the data, e.g., timestamp, zip code, day of week, etc.,
users can easily filter the charts along the dimension of their choosing.

I implemented the interactive map
using the [Leaflet](http://leafletjs.com)
javascript library. I first added the zip code boundaries of Philadelphia to
the map using the GeoJSON data available from
[OpenDataPhilly](https://www.opendataphilly.org/dataset/zip-codes). Next,
I set up an interactive density map (using hexagonal binning) using a
[Leaflet plugin](https://github.com/Asymmetrik/leaflet-d3).
The density map automatically shows the same data being plotted on the
dc.js charts. As the user applies different filters to the charts,
the density map updates simultaneously. We can go one step further
to increase the interactivity of the map and charts. Since zip code is one
of the data dimensions and the zip code boundaries are nicely delineated on
the map, I added some javascript magic to the map that automatically applies
zip code filtering of the data when the user clicks on specific zip
codes on the map. This allows users to very easily visualize trends in the data
for specific areas of Philly as they explore the map.

## Putting it all together

Learning the javascript tools was the focus of the project, and since
I'm an HTML + CSS novice, I opted to use the
[dashboard Bootstrap templates](https://keen.github.io/dashboards/) provided by Keen IO.
This allowed me to get the app up and running quickly using an aesthetically
pleasing and responsive design. And since I was already familiar with the
[Bootstrap framework](http://getbootstrap.com/2.3.2/),
I was able to tweak things easily along the way.
Finally, since I wanted to focus on monthly trends, I added a button to the
dashboard to load the proper data given the month and year requested by the
user.

Python is my language of choice, so I chose to deploy the visualization as
a (very simple) [Flask application](http://flask.pocoo.org/docs/0.12/quickstart/).
With just a few lines of code, the server was up and running, properly
delivering the monthly data set requested by the user.
Finally, I needed to host the app somewhere. The two obvious choices
were [Heroku](https://www.heroku.com) and
[PythonAnywhere](https://www.pythonanywhere.com), and after a little
research, I chose the latter. A few minutes of setup, and the app was up and
running at <http://nickhand.pythonanywhere.com>.

## Analyzing the data

The Philadelphia Parking Authority (PPA) is an infamous organization, known to
operate with ruthless efficiency. That efficiency is reflected clearly in
the data. There are over 100,000 tickets issued monthly, totaling a
staggering 5 to 6 million dollars in fines. The bulk of those
tickets are issued in Center City and its surrounding zip codes
Monday through Friday, when the frantic search for a valid parking space
must often competes with other time constraints, such as getting to work on time.
Lunch time hours (11 AM to 2 PM) appear to be the peak time to get a ticket in
these areas. Sundays are the easiest day to avoid being ticketed. The
ticketing distributions for Thursday, Friday, and Saturday are bimodal, with
the usual lunch time peak followed by a second, lesser peak around 9 PM,
which likely takes advantage of the weekend nightlife ramping up across
the city.

There are clear ticketing trends present in the data, and the PPA have very likely
optimized their enforcement patterns and hours to issue the most number of
tickets possible. That is likely why we see ticketing peaks at lunch time
during the work week and in the evenings during the weekend.
However, to draw further conclusions from these patterns, we would need to perform
a more careful statistical analysis. A complex number of variables,
such as population, traffic flow, number of registered cars, etc., contributes
to these trends, and they would need to be carefully accounted for.

The data visualization is particularly well-suited for detecting anomalies
in the data. These outliers are due to city-wide events that impact the usual
ticketing patterns in a meaningful way, and identifying them in the data
allows you to reverse engineer their cause. For example, there is a clear
deficit in the number of tickets issued from January 24 - 26, 2016, with a
rise in the number of snow emergency tickets. The cause was
[Winter Storm Jonas](https://en.wikipedia.org/wiki/January_2016_United_States_blizzard),
which dropped over [20 inches of snow on Philadelphia](http://www.philly.com/philly/news/local/20160124_Philadelphia_January_2016_blizzard_updates.html).
An even more striking outlier occurred from September 24 - 29, 2015, with nearly
no tickets being issued during that time. These dates correspond to the
[Pope's visit to Philly](http://www.philly.com/philly/news/pope/). With the
ticketing machine shutdown for roughly 5 days, the total amount issued in
fines was about 1 million dollars below average in September 2015.

And with that, I'll leave you to explore the data. Good luck avoiding those
parking tickets, and thanks for reading!
