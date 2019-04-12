SELECT
	COUNT(id) AS id,
	MAX(lastupdate) AS lastupdate,
	MIN(date) AS date,
	COUNT(DISTINCT DATE) AS cnt_dates,
	-- caloriesidle,
	"user",
	COUNT(activities) AS activities,
	COUNT(places) AS places,
	COUNT(storyline) AS storyline,
	COUNT(summary) AS summary
FROM public.v_moves
GROUP BY "user"
;
