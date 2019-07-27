DROP VIEW IF EXISTS v_coordinates_moves_location CASCADE;

CREATE VIEW v_coordinates_moves_location AS
(SELECT
	dta.lat AS latitude,
	dta.lon AS longitude,
	MAX(dta.endtime) AS last_visit,
	dta."user" AS "user",
	CASE
		WHEN SUM(dta.duration) IS NOT NULL OR SUM(dta.duration) > 0
		THEN SUM(dta.duration)
		ELSE 1/(24*60*60)
		END * COUNT(dta.*) AS prio
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
