
from sqlalchemy import create_engine
import matplotlib.pyplot as plt
import numpy as np

engine = create_engine('mysql+pymysql://ds2rdb:ds2ds2@localhost:3306/euro_match',
                      encoding='utf-8')
con = engine.connect()
con.execution_options(autocommit=True)

result = con.execute('select playing_club, count(*) as mvp from games as g right join players as p on g.plr_of_match = p.player_id group by p.playing_club order by mvp desc;')
playing_club = []
mvp_count = []
view_cnt = 5
# for data in result:
#     playing_club.append(data['playing_club'])
#     mvp_count.append(data['mvp'])
# ind = np.arange(view_cnt)
# p1 = plt.bar(ind, mvp_count[:view_cnt], width=0.5)
# plt.ylabel('Player Of Match')
# plt.xlabel('Club Team')
# plt.xticks(ind, playing_club[:view_cnt])
# plt.title('Club with Player Of Match')
# plt.show()