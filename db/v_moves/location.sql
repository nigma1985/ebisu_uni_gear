DROP VIEW IF EXISTS v_location CASCADE;

CREATE VIEW v_location AS
	(SELECT
		id,
		CAST ( lat AS FLOAT8 ) AS lat,
		CAST ( lon AS FLOAT8 ) AS lon
	FROM public.location
);
