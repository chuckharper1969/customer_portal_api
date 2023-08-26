from django.db import models

class SyslogInput(models.Model):
    created_at = models.DateTimeField(auto_now=True)
    input_id = models.CharField(max_length=32)
    udp_port = models.CharField(max_length=8)
    tcp_port = models.CharField(max_length=8)
    message = models.CharField(max_length=128, default="Waiting to be onboarded")
    status = models.IntegerField(default=0)
    owner = models.ForeignKey('auth.user', related_name='syslog_inputs', on_delete=models.CASCADE)

    class Meta:
        ordering = ['created_at']
