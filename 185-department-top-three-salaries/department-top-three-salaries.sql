select d.name as department, e.name as employee, e.salary as salary
from employee as e
join department as d on e.departmentid = d.id
where (
    select count(distinct e2.salary)
    from employee as e2
    where e2.departmentid = e.departmentid
      and e2.salary > e.salary
) < 3
order by d.name, e.salary desc;
