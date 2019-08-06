# 각 클럽별 출전 선수들의 총 득점 수 (Searching Top 10 Club)
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

# Top 10 Club 의 총 득점수를 차트로 표현한다.
import matplotlib.pyplot as plt

# X축은 클럽 순위(1~10), Y축은 클럽별 득점 수
position = list( df_clubs10.index )
plt.bar( position, df_club10.goals, align = 'center')
plt.xticks( position, df_clubs10.club_name )
plt.ylabel( 'Goals' )
plt.title( 'Top 10 club in goal')
