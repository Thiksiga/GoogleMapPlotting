# import gmplot package
import gmplot
import pandas as pd

file_name='2023-04-02'

# Load the CSV data into a pandas DataFrame
df = pd.read_csv('C:\AI4covid\Trajectory plotting\Datas'+ f'\data_{file_name}.csv')

# Extract the 'latitude'&'longitude' columns
latitude_list= df['Latitude']
longitude_list = df['Longitude']

#Map centorized to srilanka
gmap3 = gmplot.GoogleMapPlotter(7.8731, 80.7718, 22)

# scatter method of map object 
# scatter points on the google map
gmap3.scatter(latitude_list, longitude_list, '#000000',
              size=5, marker=False)

# Plot method Draw a line in
# between given coordinates
# gmap3.plot(latitude_list, longitude_list,
#            'cornflowerblue', edge_width=2.5)

# filename = 'C:\AI4covid\Trajectory plotting\plots'+ f'\plot_{file_name}.html'

# gmap3.draw("C:\AI4covid\Trajectory plotting\plots\map1.html")

gmap3.draw('C:\AI4covid\Trajectory plotting\plots'+ f'\plot_{file_name}.html')