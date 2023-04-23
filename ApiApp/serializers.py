from rest_framework import serializers

from MoviesApp.models import Critic


class criticSerializers(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source = 'author.id')

    class Meta:
        model = Critic
        fields = '__all__'
