SELECT
	id,
	CAST ( lat AS FLOAT8 ) AS lat,
	CAST ( lon AS FLOAT8 ) AS lon
FROM public.location;
