create table if not exists tmp_products AS
(SELECT
    p.id As productId,
    i.urls AS urls,
    c.categories AS categories
FROM `raw_products` p
LEFT JOIN `tmp_product_images` i ON p.id = i.productId
LEFT JOIN `tmp_product_categories` c ON p.id = c.productId)