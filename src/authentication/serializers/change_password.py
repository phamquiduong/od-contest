from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

User = get_user_model()


class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True, validators=[validate_password])

    user: User | None = None

    def validate_current_password(self, current_password: str):
        if self.user and not self.user.check_password(current_password):
            raise serializers.ValidationError('Mật khẩu cũ không đúng.', code='incorrect_current_password')
        return current_password

    def validate(self, attrs):
        if attrs['current_password'] == attrs['new_password']:
            raise serializers.ValidationError({
                'new_password': serializers.ErrorDetail(
                    string='Mật khẩu mới không được trùng với mật khẩu hiện tại.',
                    code='new_password_same_as_current'
                )
            })
        return attrs

    def save(self):
        new_password = self.validated_data['new_password']

        if self.user:
            self.user.set_password(new_password)
            self.user.save()

        return self.user
