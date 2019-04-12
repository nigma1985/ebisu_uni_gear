SELECT place.id,
   place.place_id::bigint AS place_id,
   place.type,
   place.name,
   place.facebookplaceid,
   place.foursquareid,
   place.location::integer AS location
  FROM place;
