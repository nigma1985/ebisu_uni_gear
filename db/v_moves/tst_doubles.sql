-- this statement is meant to controll for doubles
-- this view should always be empty

SELECT * FROM (
	SELECT
		COUNT(id) as ids, date, "user" --, caloriesidle, lastupdate, summary, activities
		FROM public.moves
		GROUP BY date, "user") as query
	WHERE query.ids > 1
	ORDER BY query.date
	;
