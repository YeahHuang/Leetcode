#关于sql如何依靠q1.turn排序 然后一个个加进去 选一个最开始的 可以慢慢看
#1741ms
SELECT q1.person_name
FROM Queue q1 JOIN Queue q2 ON q1.turn >= q2.turn
GROUP BY q1.turn
HAVING SUM(q2.weight) <= 1000
ORDER BY SUM(q2.weight) DESC
LIMIT 1

#2192ms
SELECT q1.person_name
FROM Queue q1, Queue q2
WHERE q1.turn >= q2.turn
GROUP BY q1.turn
HAVING SUM(q2.weight) <= 1000
ORDER BY SUM(q2.weight) DESC
LIMIT 1

#1675ms
SELECT person_name FROM Queue as a
WHERE
(
    SELECT SUM(weight) FROM Queue as b
    WHERE b.turn<=a.turn
    ORDER By turn
)<=1000
ORDER BY a.turn DESC limit 1;