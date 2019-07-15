DROP VIEW IF EXISTS v_station_values CASCADE;

CREATE VIEW v_station_values AS
(SELECT
	id,
	dist::FLOAT AS dist,
	CASE WHEN diesel = 'False' THEN NULL ELSE diesel::FLOAT END AS diesel,
	CASE WHEN e5 = 'False' THEN NULL ELSE e5::FLOAT END AS e5,
	CASE WHEN e10 = 'False' THEN NULL ELSE e10::FLOAT END AS e10,
	isopen::BOOLEAN AS isopen,
	status
FROM
	public.station_values
);
