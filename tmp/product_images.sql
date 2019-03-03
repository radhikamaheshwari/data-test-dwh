SELECT
    pr.id As productId,
    ARRAY_AGG(
        p.url
    ) AS urls
FROM `raw_products` pr
LEFT JOIN `raw_pictures` p ON (pr.id, 'product') = (p.external_id, p.type)
GROUP BY 1