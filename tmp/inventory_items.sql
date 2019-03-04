create table if not exists tmp_inventory_items AS
(
SELECT
    sku_id,
    inventory_count
FROM 
    `raw_inventory_items`
    )
