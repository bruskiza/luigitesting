SELECT net as network,
count(*) as number_of_event
from earthquakes
group by net
