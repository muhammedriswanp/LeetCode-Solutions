select e.employee_id 
from Salaries as s
right join Employees as e 
on e.employee_id  = s.employee_id
where s.salary  is null
union all 
select s.employee_id 
from Salaries as s
left join Employees as e 
on e.employee_id  = s.employee_id
where e.name is null 
order by employee_id ;