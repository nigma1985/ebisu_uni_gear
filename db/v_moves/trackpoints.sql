SELECT
	id,
	CAST ( lat AS FLOAT8 ) AS lat,
	CAST ( lon AS FLOAT8 ) AS lon,
	CAST ( "time" AS TIMESTAMPTZ ) AS "time",
	CAST ( activities AS BIGINT ) AS activities
FROM public.trackpoints;
