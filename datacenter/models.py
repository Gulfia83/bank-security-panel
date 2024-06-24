from django.db import models
from django.utils.timezone import localtime


class Passcard(models.Model):
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now=True)
    passcode = models.CharField(max_length=200, unique=True)
    owner_name = models.CharField(max_length=255)

    def __str__(self):
        if self.is_active:
            return self.owner_name
        return f'{self.owner_name} (inactive)'


class Visit(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    passcard = models.ForeignKey(Passcard, on_delete=models.CASCADE)
    entered_at = models.DateTimeField()
    leaved_at = models.DateTimeField(null=True)

    def __str__(self):
        return '{user} entered at {entered} {leaved}'.format(
            user=self.passcard.owner_name,
            entered=self.entered_at,
            leaved=(f'leaved at {self.leaved_at}'
                    if self.leaved_at else 'not leaved'))

    def get_duration(self):
        leaved_at_localtime = localtime(self.leaved_at)
        entered_at_localtime = localtime(self.entered_at)
        now = localtime()
        if self.leaved_at:
            duration = leaved_at_localtime - entered_at_localtime
        else:
            duration = now - entered_at_localtime

        return duration

    def format_duration(duration):
        time = duration.total_seconds()
        hours = int(time // 3600)
        minutes = int((time % 3600) // 60)
        
        return f'{hours} ч. {minutes} мин.'
    
    def is_long(self, minutes=60):
        if self.leaved_at:
            duration = self.leaved_at - self.entered_at
        else:
            duration = localtime() - localtime(self.entered_at)
        
        duration_in_minutes = duration.total_seconds() / 60
    
        return duration_in_minutes > minutes