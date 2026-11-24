# Write your MySQL query statement below
select c.unique_id,e.name from Employees as e left join EmployeeUNI as c ON e.id = c.id