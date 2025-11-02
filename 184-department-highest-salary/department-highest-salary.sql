
SELECT
    D.name AS Department,
    E.name AS Employee,
    E.salary
FROM
    Employee E
INNER JOIN
    Department D ON E.departmentId = D.id
WHERE
    E.salary = (
        SELECT
            MAX(salary)
        FROM
            Employee
        WHERE
            departmentId = E.departmentId
    );
