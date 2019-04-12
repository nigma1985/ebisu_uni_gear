SELECT location.id,
   location.lat::double precision AS lat,
   location.lon::double precision AS lon
  FROM location;
