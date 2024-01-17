#!/bin/bash

# Check if the correct number of arguments is provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <database_name>"
    exit 1
fi

# Store the provided database name in a variable
database_name="$1"

# MySQL command to execute the query
mysql -u your_mysql_user -p -e "
  USE ${database_name};
  SELECT tv_genres.name, SUM(tv_shows.rating) AS rating_sum
  FROM tv_genres
  JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
  JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id
  GROUP BY tv_genres.name
  ORDER BY rating_sum DESC;
"

