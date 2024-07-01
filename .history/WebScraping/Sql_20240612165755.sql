


SELECT e.mgr, COUNT(*) as emp_count
FROM EMP e
GROUP BY e.mgr
ORDER BY emp_count DESC
LIMIT 1;


SELECT COUNT(*)
FROM EMP
where comm IS NOT NULL
