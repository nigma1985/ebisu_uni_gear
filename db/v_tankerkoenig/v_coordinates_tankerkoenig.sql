DROP VIEW IF EXISTS v_coordinates_tankerkoenig CASCADE;

CREATE VIEW v_coordinates_tankerkoenig AS
(SELECT
	loca.lat AS lat,
	loca.lng AS lng,
	COUNT(DISTINCT res.tankerkoenig) AS n,
 	MAX(tk.utc_datetime) AS utc_datetime,
 	tk."user" AS "user",
	'tankerkoenig' AS "source"
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
