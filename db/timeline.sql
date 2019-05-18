-- SELECT CURRENT_DATE + i
-- FROM generate_series(date '2012-06-29' - CURRENT_DATE,
--   date '2012-07-03' - CURRENT_DATE) i

SELECT i::date FROM generate_series('2012-06-29',
  '2012-07-03', '1 day'::interval) i
