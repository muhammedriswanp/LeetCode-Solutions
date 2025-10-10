SELECT employee_id
FROM Employees
where salary < 30000 
and manager_id is not null and manager_id not in (select employee_id from employees )
ORDER BY employee_id;