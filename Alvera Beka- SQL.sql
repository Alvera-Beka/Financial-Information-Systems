UPDATE Expenses SET amount = 180.00 WHERE expense_id = 2;

SELECT * FROM Savings
-- delete a row from a table
DELETE FROM Savings WHERE saving_id = 2
SELECT * FROM Expenses
SELECT category, SUM(amount) as total_expenses
FROM Expenses 
GROUP BY category;
-- select everything andorder them in descending order 
SELECT * FROM Income
ORDER BY date_received DESC;
-- filter categories with total expenses above $500 
SELECT category, SUM(amount) as total_expense 
FROM Expenses 
GROUP BY category 
HAVING total_expense > 200;
DESCRIBE Savings
-- inner join - match income with savings on the same date 
SELECT i.income_source, i.amount as income_amount, s.amount as saved_amount, s.date_saved
FROM Income i 
INNER JOIN Savings s 
on i.date_received = s.date_saved;