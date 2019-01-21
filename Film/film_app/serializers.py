from rest_framework import serializers
from .models import Movie

#FilmId FilmName Genre Studio Director Producer LeadActor

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("FilmId", "FilmName", "Genre", "Studio", "Director", "Producer", "LeadActor")

    def update(self, instance, validated_data):
        if(instance.FilmId!=validated_data.get("FilmId", instance.FilmId)):
            instance.delete()
        instance.FilmId = validated_data.get("FilmId", instance.FilmId)
        instance.FilmName = validated_data.get("FilmName", instance.FilmName)
        instance.Genre = validated_data.get("Genre", instance.Genre)
        instance.Studio = validated_data.get("Studio", instance.Studio)
        instance.Director = validated_data.get("Director", instance.Director)
        instance.Producer = validated_data.get("Producer", instance.Producer)
        instance.LeadActor = validated_data.get("LeadActor", instance.LeadActor)
        instance.save()
        return instance