student table
student_id , marks , deviation
1,    20           70-20=50
2     30           70-30=40
3     40           70-40=30
4     70           0
5     90           20

avg= 140/5 =28


with cte()(
        select marks , rank() over (order by marks) as rnk from student;
)
select marks as second_max from cte where rnk=2
,cte2()(
    select (marks - second_max) as  deviation  from cte1
)
cte3()(
    select avg(deviation) from cte2
)

given an array having duplicates
subsets







find 2nd maximum marks
introduce 3rd col deviation
 deviation = abs (marks of student - 2nd maximum)
 average of  deviation