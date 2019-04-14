SELECT
	id,
	"group",
	activity,
	CAST ( duration AS FLOAT) AS duration,
	CAST ( steps AS FLOAT) AS steps,
	CAST ( distance AS FLOAT) AS distance,
	CAST ( calories AS FLOAT) AS calories,
	CAST ( moves AS BIGINT) AS moves
FROM public.summary;
