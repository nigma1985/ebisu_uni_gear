SELECT
-- 	mb.id,
-- 	mb.date,
	aa.id,
	aa.activity,
	aa.group,
	aa.segments,
	aa.manual,
	aa.starttime,
	aa.endtime,
	aa.duration,
	aa.steps,
	aa.distance,
	aa.calories,
	mb.lastupdate,
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
;
