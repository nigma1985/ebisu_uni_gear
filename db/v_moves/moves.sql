SELECT
	id,
	"user",
	CAST ( date AS DATE ) AS date,
	CAST ( caloriesidle AS INTEGER ) AS caloriesidle,
	CAST ( activities AS BOOLEAN ) AS activities,
	CAST ( places AS BOOLEAN ) AS places,
	CAST ( summary AS BOOLEAN ) AS summary,
	CAST ( storyline AS BOOLEAN ) AS storyline,
	CAST ( lastupdate AS TIMESTAMP ) AS lastupdate
FROM public.moves;
