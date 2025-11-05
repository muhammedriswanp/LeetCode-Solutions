WITH CategoryCounts AS (
    SELECT
        CASE
            WHEN income < 20000 THEN 'Low Salary'
            WHEN income <= 50000 THEN 'Average Salary'
            ELSE 'High Salary'
        END AS category,
        COUNT(account_id) AS accounts_count
    FROM
        Accounts
    GROUP BY
        category
),
MandatoryCategories AS (
    SELECT 'Low Salary' AS category
    UNION ALL
    SELECT 'Average Salary'
    UNION ALL
    SELECT 'High Salary'
)

SELECT
    M.category,
  
    COALESCE(C.accounts_count, 0) AS accounts_count
FROM
    MandatoryCategories M
LEFT JOIN
    CategoryCounts C ON M.category = C.category;