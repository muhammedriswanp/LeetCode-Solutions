with all_friends as (
    select requester_id as id from requestaccepted
    union all
    select accepter_id as id from requestaccepted
),
friend_counts as (
    select id, count(*) as num
    from all_friends
    group by id
),
max_count as (
    select max(num) as max_num from friend_counts
)
select id, num
from friend_counts, max_count
where num = max_num;
-- 