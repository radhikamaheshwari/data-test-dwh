create table if not exists final_products as
(
SELECT
    productId,
    categories,
    images,
    collect_list(
        variant
    ) AS variants
FROM
    (
    SELECT
        p.productId,
        p.categories,
        p.urls AS images,
        struct(
            v.skuId,
            v.purchasePrices,
            v.urls,
            v.inventoryCount
        ) AS variant
    FROM `tmp_products` AS p
    LEFT JOIN `tmp_variants` v ON p.productId = v.skuId
)
GROUP BY 1, 2, 3)