create table if not exists tmp_item_purchase_prices AS
(SELECT
    l.sku_id AS sku_id,
    i.batch_id,
            collect_list(i.purchase_price
        ) AS purchase_prices
FROM
    `raw_purchase_line_items` l
    INNER JOIN `raw_purchase_items` i ON l.batch_purchase_id = i.batch_id
GROUP BY 1, 2)