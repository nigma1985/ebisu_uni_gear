DROP VIEW IF EXISTS v_coordinates_moves_location CASCADE;

CREATE VIEW v_coordinates_moves_location AS
(SELECT
	dta.lat,
	dta.lon,
	MAX(dta.endtime) AS "timestamp",
	dta."user" ,
	SUM(dta.duration) AS duration,
	COUNT(dta.*) AS n
FROM (
	SELECT
		lc.lat,
		lc.lon,
		sa.endtime,
		(EXTRACT(EPOCH FROM sa.endtime - sa.starttime))/(24*60*60) AS duration,
		mb.user
	FROM v_moves AS mb
	LEFT JOIN (
		SELECT
			MAX(lastupdate) AS lastupdate,
			date,
			"user"
		FROM
			v_moves AS ma
		GROUP BY
			date,
			"user"
		) AS mc USING (lastupdate, "user", date)
	LEFT JOIN v_segments AS sa ON sa.moves = mb.id
	LEFT JOIN v_place AS pl ON pl.id = sa.place
	LEFT JOIN v_location AS lc ON lc.id = pl.location) AS dta
GROUP BY
	dta.lat, dta.lon, dta."user"
-- LIMIT 100
);
