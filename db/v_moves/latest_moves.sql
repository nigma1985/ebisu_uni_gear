-- first step towards standard view

SELECT a.id
FROM public.v_moves AS a
LEFT JOIN
	(SELECT
		"user" AS "user", date AS date, MAX(lastupdate) AS lastupdate
	FROM public.v_moves
	GROUP BY "user", date) AS b ON a.date = b.date AND a."user" = b."user"
WHERE	a.lastupdate = b.lastupdate
;
