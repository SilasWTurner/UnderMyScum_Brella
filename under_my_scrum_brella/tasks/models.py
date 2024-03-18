###########################################################################
#   Author: Luke Clarke
#   Contributors: Ollie Barnes
#
#   The author has written all code in this file unless stated otherwise.
###########################################################################

from django.db import models
from users.models import Group
from users.models import User

class Task(models.Model):
    TaskName = models.CharField(max_length=200)
    Description = models.CharField(max_length=400)
    DifficultyLevel = models.CharField(max_length=10)
    CoinReward = models.IntegerField(default=0)
    XpReward = models.IntegerField(default=0)

    def __str__(self):
        return self.TaskName


################################################################
#   This model connects the User model to the Task model,
#   allowing admins to assign tasks to individual users
#
#   Author: Ollie Barnes
################################################################
class UserTask(models.Model):
    completion_status = models.IntegerField(default=0)
    task_id = models.ForeignKey(Task, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ['user_id', 'task_id']


################################################################
#   This model connects the Group model to the Task model,
#   allowing admins to assign tasks to a group of users
#
#   Author: Ollie Barnes
################################################################
class GroupTask(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    
    class Meta:
        unique_together = ['group', 'task']