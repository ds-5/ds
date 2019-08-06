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

# Top 10 클럽의 순위를 Bar chart로 표시한다.
import matplotlib.pyplot as plt

position = list( df_clubs10.index )
goals = []
for i in range( 10 ):
    goals.append( df_club10.goals[i])

# Y축은 Club name, X축은 클럽 소속 선수들의 총 득점 수
plt.barh( position, goals, align = 'center', alpha=1)
plt.yticks( position, df_clubs10.playing_club )
plt.xlabel( 'Goal score')
plt.title( 'Top 10 club in goal score')
