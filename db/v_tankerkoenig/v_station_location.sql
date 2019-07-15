DROP VIEW IF EXISTS v_station_location CASCADE;

CREATE VIEW v_station_location AS
(SELECT
	id,
	station_location_id,
	name,
	brand,
	street,
	place,
	lat::FLOAT8 lat,
	lng::FLOAT8 lng,
	postcode,
	housenumber,
	wholeday::BOOLEAN AS wholeday
	FROM public.station_location
);
