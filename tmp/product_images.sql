create table if not exists tmp_product_images AS
(SELECT
    pr.id As productId,
    collect_list(
        p.url
    ) AS urls
FROM `raw_products` pr
LEFT JOIN `raw_pictures` p ON pr.id = p.external_id
GROUP BY 1)