DROP VIEW IF EXISTS v_coordinates_moves_trackpoints CASCADE;

CREATE VIEW v_coordinates_moves_trackpoints AS
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
		tp.lat,
		tp.lon,
		aa.endtime,
		aa.duration/(24*60*60) AS duration,
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
	LEFT JOIN v_activities AS aa ON aa.segments = sa.id
	LEFT JOIN v_trackpoints AS tp ON tp.activities = sa.id) AS dta
GROUP BY
	dta.lat, dta.lon, dta."user"
-- LIMIT 100
);
