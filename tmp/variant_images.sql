SELECT
    v.id AS sku_id,
    ARRAY_AGG(
        p.url
    ) AS urls
FROM `raw_variants` v
LEFT JOIN `raw_pictures` p ON (v.id, 'variant') = (p.external_id, p.type)
GROUP BY 1