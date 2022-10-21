from rest_framework import serializers
from .models import Miner

class MinerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Miner
        fields = ('orderDate','facility','machineName','quantity','power','monthlyFee','miningPool','status')
