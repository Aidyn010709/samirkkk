from rest_framework import serializers
from django.contrib.auth import get_user_model

from applications.account.utils import send_activation_code, send_forgot_password_code

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'surname', 'phone_number', 'date_of_birth', 'is_owner']


class OwnerApartmentProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'name', 'surname', 'phone_number', 'date_of_birth', 'is_owner', 'where_studied', 'profession', 'interesting_fact', 'hobbies',
                  'languages_spoken', 'location', 'description']


class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(required=True, min_length=6, write_only=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'password2')

    def validate(self, attrs):
        p1 = attrs.get('password')
        p2 = attrs.pop('password2')

        if p1 != p2:
            raise serializers.ValidationError('Пароли не совпадают')
        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        send_activation_code(user.email, user.activation_code)
        return user


class RegisterOwnerApartmentSerializer(serializers.ModelSerializer):
    where_studied = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)
    profession = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)
    interesting_fact = serializers.CharField(allow_blank=True, allow_null=True)
    hobbies = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)
    languages_spoken = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)
    location = serializers.CharField(max_length=100, allow_blank=True, allow_null=True)
    description = serializers.CharField(allow_blank=True, allow_null=True)

    class Meta:
        model = User
        fields = ('where_studied', 'profession', 'interesting_fact', 'hobbies',
                  'languages_spoken', 'location', 'description')




class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, min_length=6)
    new_password_confirm = serializers.CharField(required=True, min_length=6)

    def validate_old_password(self, password):
        request = self.context.get('request')
        user = request.user
        print(user)
        if not user.check_password(password):
            raise serializers.ValidationError('Неверный пароль!')
        return password

    def validate(self, attrs):
        p1 = attrs.get('new_password')
        p2 = attrs.get('new_password_confirm')

        if p1 != p2:
            raise serializers.ValidationError('Пароли не совпадают')
        return attrs

    def set_new_password(self):
        request = self.context.get('request')
        user = request.user
        password = self.validated_data.get('new_password')
        user.set_password(password)
        user.save(update_fields=['password'])


class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate_email(self, email):
        if not User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Пользователь с такой почтой не найден!')
        return email

    def send_code(self):
        email = self.validated_data.get('email')
        user = User.objects.get(email=email)
        user.create_activation_code()
        user.save()
        send_forgot_password_code(user.email, user.activation_code)


class ForgotPasswordConfirmSerializer(serializers.Serializer):
    code = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, min_length=6)
    new_password_confirm = serializers.CharField(required=True, min_length=6)

    @staticmethod
    def validate_code(code):
        if not User.objects.filter(activation_code=code).exists():
            raise serializers.ValidationError('Неверный код!')
        return code

    def validate(self, attrs):
        p1 = attrs.get('new_password')
        p2 = attrs.get('new_password_confirm')

        if p1 != p2:
            raise serializers.ValidationError('Пароли не совпадают')
        return attrs

    def set_new_password(self):
        code = self.validated_data.get('code')
        password = self.validated_data.get('new_password')
        user = User.objects.get(activation_code=code)
        user.set_password(password)
        user.activation_code = ''
        user.save(update_fields=['password', 'activation_code'])



