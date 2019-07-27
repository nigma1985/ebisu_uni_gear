DROP VIEW IF EXISTS v_coordinates_tankerkoenig CASCADE;

CREATE VIEW v_coordinates_tankerkoenig AS
(SELECT
	loca.lat AS latitude,
	loca.lng AS longitude,
	COUNT(DISTINCT res.tankerkoenig) AS prio,
 	MAX(tk.utc_datetime) AS last_visit,
 	tk."user" AS "user"
FROM
	public.results AS res
LEFT JOIN
	public.v_station_location AS loca ON res.station_location::INTEGER = loca.id
LEFT JOIN
	public.v_tankerkoenig AS tk ON res.tankerkoenig::INTEGER = tk.id
WHERE
	loca.lat IS NOT NULL AND loca.lng IS NOT NULL
GROUP BY
	loca.lat,
	loca.lng,
	res.station_location,
 	tk."user"
);
