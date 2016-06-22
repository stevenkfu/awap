import django_tables2 as tables
from web.models import Team

class TeamScoreboard(tables.Table):

    name = tables.Column(verbose_name='Team Name')
    score_1 = tables.Column(verbose_name='Round 1')
    score_2 = tables.Column(verbose_name='Round 2')
    score_3 = tables.Column(verbose_name='Round 3')
    score_4 = tables.Column(verbose_name='Round 4')
    score_5 = tables.Column(verbose_name='Round 5')
    score_6 = tables.Column(verbose_name='Round 6')
    score_7 = tables.Column(verbose_name='Round 7')
    score_8 = tables.Column(verbose_name='Round 8')
    score_9 = tables.Column(verbose_name='Round 9')
    score_10 = tables.Column(verbose_name='Round 10')


    class Meta:
        model = Team
        fields = ['name', 'score_1', 'score_2', 'score_3', 'score_4', 'score_5', 'score_6', 'score_7', 'score_8', 'score_9', 'score_10']
        attrs = {'class': 'table table-bordered table-hover table-centered'}
