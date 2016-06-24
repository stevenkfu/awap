from django.db.models.signals import pre_save
from django.dispatch import receiver

from web.models import Team


@receiver(pre_save, sender=Team)
def update_total_score(sender, instance, **kwargs):
    instance.total_score = (instance.score_1
                          + instance.score_2
                          + instance.score_3
                          + instance.score_4
                          + instance.score_5
                          + instance.score_6
                          + instance.score_7
                          + instance.score_8
                          + instance.score_9
                          + instance.score_10)
