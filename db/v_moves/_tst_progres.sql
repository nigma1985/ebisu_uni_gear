-- this statement is meant to controll for doubles and progress during import

SELECT
	"user",
	COUNT(id) AS cnt_id,
	-- MAX(lastupdate) AS lastupdate,
	-- MIN(date) AS date,
	COUNT(DISTINCT date) AS cnt_dates,
	-- caloriesidle,
	ROUND((100.0 * COUNT(activities)) / COUNT(DISTINCT date),1) AS prc_activities,
	ROUND((100.0 * COUNT(places)) / COUNT(DISTINCT date),1) AS prc_places,
	ROUND((100.0 * COUNT(storyline)) / COUNT(DISTINCT date),1) AS prc_storyline,
	ROUND((100.0 * COUNT(summary)) / COUNT(DISTINCT date),1) AS prc_summary,
	ROUND((100.0 * COUNT(id)) / COUNT(DISTINCT date),1) AS prc_all
FROM public.moves
GROUP BY "user"
;
