from models import AiklagUser
from rest_framework import serializers


class ClientSerializer(serializers.ModelSerializer):
    PASS_MIN_LENGTH = 8
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True,
        min_length=PASS_MIN_LENGTH,
        error_messages={
            "min_length": "Password too short. Password must be min %s characters" % PASS_MIN_LENGTH,
        },
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

    def update(self, instance, validated_data):
        if 'password' not in validated_data or 'password2' not in validated_data:
            raise serializers.ValidationError("Please provide password")
        elif validated_data['password'] != validated_data['password2']:
            raise serializers.ValidationError("Your passwords do not match")
        if not instance.check_password(validated_data['password']):
            raise serializers.ValidationError("Invalid password")
        instance.email = validated_data.get('email', instance.email)
        instance.date_of_birth = validated_data.get('date_of_birth', instance.date_of_birth)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.gender = validated_data.get('gender', instance.gender)
        instance.phone_number = validated_data.get('phone_number', instance.phone_number)
        instance.location = validated_data.get('location', instance.location)
        instance.save()
        return instance



