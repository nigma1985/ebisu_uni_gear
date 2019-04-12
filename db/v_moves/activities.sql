SELECT activities.id,
   activities.endtime::timestamp with time zone AS endtime,
   activities.starttime::timestamp with time zone AS starttime,
   activities.duration::double precision AS duration,
   activities.activity,
   activities."group",
   activities.manual::boolean AS manual,
   activities.distance::double precision AS distance,
   activities.calories::integer AS calories,
   activities.steps::integer AS steps,
   activities.segments::integer AS segments
  FROM activities;
