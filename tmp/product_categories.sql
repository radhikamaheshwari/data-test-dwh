create table if not exists tmp_product_categories as

(SELECT
    p.id As productId,
    array(
        collect_list(
            c.category_name
        )
    ) AS categories
FROM `raw_products` p
LEFT JOIN `raw_categories` c ON  p.category_id = c.id
GROUP BY 1)