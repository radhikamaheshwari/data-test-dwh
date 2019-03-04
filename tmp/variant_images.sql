create table if not exists tmp_variant_images AS
(SELECT
    v.id AS sku_id,
    collect_list(
        p.url
    ) AS urls
FROM `raw_variants` v
LEFT JOIN `raw_pictures` p ON v.id = p.external_id
GROUP BY 1)