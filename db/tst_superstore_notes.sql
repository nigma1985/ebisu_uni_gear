CREATE TABLE "SuperStore";

ALTER TABLE "SuperStore"
	ADD COLUMN rowID TEXT,
	ADD COLUMN orderID TEXT,
	ADD COLUMN orderDate TEXT,
	ADD COLUMN shipDate TEXT,
	ADD COLUMN shipMode TEXT,
	ADD COLUMN customerID TEXT,
	ADD COLUMN customerName TEXT,
	ADD COLUMN segment TEXT,
	ADD COLUMN city TEXT,
	ADD COLUMN "state" TEXT,
	ADD COLUMN country TEXT,
	ADD COLUMN po TEXT,
	ADD COLUMN market TEXT,
	ADD COLUMN region TEXT,
	ADD COLUMN productID TEXT,
	ADD COLUMN category TEXT,
	ADD COLUMN subCategory TEXT,
	ADD COLUMN productName TEXT,
	ADD COLUMN sales TEXT,
	ADD COLUMN quantity TEXT,
	ADD COLUMN discount TEXT,
	ADD COLUMN profit TEXT,
	ADD COLUMN shippingCost TEXT,
	ADD COLUMN orderPriority TEXT
;

CREATE OR REPLACE VIEW public.v_superstore AS
 SELECT "SuperStore".rowid::integer AS rowid,
    "SuperStore".orderid,
    "SuperStore".orderdate::date AS orderdate,
    "SuperStore".shipdate::date AS shipdate,
    "SuperStore".shipmode,
    "SuperStore".customerid,
    "SuperStore".customername,
    "SuperStore".segment,
    "SuperStore".city,
    "SuperStore".state,
    "SuperStore".country,
        CASE
            WHEN "SuperStore".po = ''::text THEN NULL::integer
            ELSE "SuperStore".po::integer
        END AS po,
    "SuperStore".market,
    "SuperStore".region,
    "SuperStore".productid,
    "SuperStore".category,
    "SuperStore".subcategory,
    btrim("SuperStore".productname, '"'::text) AS productname,
    "SuperStore".sales::real AS sales,
    "SuperStore".quantity::integer AS quantity,
    "SuperStore".discount::real AS discount,
    "SuperStore".profit::real AS profit,
    "SuperStore".shippingcost::real AS shippingcost,
    "SuperStore".orderpriority
   FROM "SuperStore";
