-- Write your query below
SELECT name FROM customers 
Where id NOT IN (SELECT customer_id FROM Orders) ;