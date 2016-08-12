from models import AiklagUser
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True
    )
    password2 = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True
    )

    class Meta:
        model = AiklagUser
        fields = ('email', 'password', 'password2', 'date_of_birth', 'first_name', 'last_name', 'gender',
                  'phone_number', 'location')
        read_only_fields = ['is_admin']
        write_only_fields = ('password', 'password2')

    def validate(self, data):
        """
        Checks to be sure that the received password and confirm_password
        fields are exactly the same
        """
        if data['password'] != data['password2']:
            raise serializers.ValidationError("Passwords do not match")
        return data

    def create(self, validated_data):
        return AiklagUser.objects.create_user(**validated_data)
