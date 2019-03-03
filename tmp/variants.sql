SELECT
    f.product_id AS productId
    v.id AS skuId,
    p.purchase_prices AS purchasePrices,
    i.urls AS urls,
    inv.inventory_count AS inventoryCount
FROM `raw_variants` v
LEFT JOIN `tmp_item_purchase_prices` p
LEFT JOIN `tmp_variant_images` i
LEFT JOIN `tmp_inventory_items` inv