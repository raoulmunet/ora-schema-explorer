INSERT INTO dwh.customer_dim (customer_id, customer_name)
SELECT customer_id, customer_name
FROM customers;
