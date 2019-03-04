create table if not exists tmp_variants AS
(SELECT
    f.productId,
    v.id AS skuId,
    p.purchase_prices AS purchasePrices,
    i.urls AS urls,
    inv.inventory_count AS inventoryCount
FROM `raw_variants` v
LEFT JOIN `tmp_products` f on v.id=f.productId
LEFT JOIN `tmp_item_purchase_prices` p on v.id=p.sku_id
LEFT JOIN `tmp_variant_images` i on p.sku_id=i.sku_id
LEFT JOIN `tmp_inventory_items` inv on p.sku_id=inv.sku_id
)