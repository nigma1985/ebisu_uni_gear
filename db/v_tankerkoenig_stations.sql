DROP VIEW IF EXISTS v_tankerkoenig_stations CASCADE;

CREATE VIEW v_tankerkoenig_stations AS
(SELECT
	loca.station_location_id AS station_location_id,
	COUNT(DISTINCT res.tankerkoenig) AS n,
 	MAX(tk.utc_datetime) AS utc_datetime,
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
	loca.station_location_id,
	res.station_location,
 	tk."user"
);
