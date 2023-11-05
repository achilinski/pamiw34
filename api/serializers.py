from rest_framework import serializers
from .models import Book
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_author(self, value):
        if any(char.isdigit() for char in value):
            raise serializers.ValidationError("Author name must be a string and cannot contain numbers.")
        return value

    def validate_date_of_publishing(self, value):
        if not isinstance(value, date):
            raise serializers.ValidationError("The date of publishing must be a valid date.")

        if value > date.today():
            raise serializers.ValidationError("The date of publishing cannot be in the future.")
        return value


