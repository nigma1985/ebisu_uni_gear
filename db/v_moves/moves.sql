SELECT moves.id,
   moves.lastupdate::timestamp without time zone AS lastupdate,
   moves.date::date AS date,
   moves.caloriesidle::integer AS caloriesidle,
   moves."user",
   moves.activities::boolean AS activities,
   moves.places::boolean AS places,
   moves.storyline::boolean AS storyline,
   moves.summary::boolean AS summary
  FROM moves;
