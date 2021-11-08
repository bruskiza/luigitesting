SELECT 
    magSource as "Magnitude Source",
    count(*) as number_of_event
from earthquakes
group by magSource
