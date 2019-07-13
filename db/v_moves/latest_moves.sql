-- first step towards standard view

SELECT ma.id
FROM public.v_moves AS ma
LEFT JOIN
	(SELECT
		"user" AS "user", date AS date, MAX(lastupdate) AS lastupdate
	FROM public.v_moves
	GROUP BY "user", date) AS mb ON ma.date = mb.date AND ma."user" = mb."user"
WHERE	ma.lastupdate = mb.lastupdate
;


------------------

SELECT vact.*
FROM v_activities AS vact
LEFT JOIN v_segments AS vseg ON vseg.id = vact.segments
LEFT JOIN v_moves AS vmov ON vmov.id = vseg.moves
WHERE act.segments IN (
	SELECT seg.id
	FROM v_segments AS seg
	WHERE seg.moves IN (
		SELECT movb.id
		FROM v_moves AS mova
		JOIN v_moves AS movb ON (mova."user" = movb."user") AND (mova.date = movb.date)
		GROUP BY mova."user", mova.date
		)
);






-----------------------

WITH tab AS (
SELECT
	m.id AS moves_id,
	m.lastupdate::TIMESTAMP AS moves_lastupdate,
	m.user AS "user",
	s.id AS segments_id,
	s.lastupdate::TIMESTAMP AS segments_lastupdate,
	a.*
FROM
	moves AS m
LEFT JOIN
	segments AS s ON (s.moves::integer = m.id)
LEFT JOIN
	activities AS a ON (a.segments::integer = s.id)
-- ORDER BY
	-- m.id ASC
)

SELECT
	*
FROM
	tab
WHERE
	tab.id IS NOT NULL
LIMIT
	100
;
