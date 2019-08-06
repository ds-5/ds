# 각 클럽 별 소속 선수들의 총 득점 수 (Searching Top 10 Club)
df_clubs = sql.read_sql_query("""
    select playing_club, count(*)
    from players p
    right join goals g
    on p.player_id = g.player_id
    group by playing_club
    order by count(*) DESC    
    """, con)

# 전체 클럽 중에서 Top 10 클럽을 추출한다.
df_clubs10 = df_clubgoals.head(10)

# Column 이름을 수정한다.
df_clubs10.rename( columns = { "playing_club":"club_name", "count(*)":"goals" })

