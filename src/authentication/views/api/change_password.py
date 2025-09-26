from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from authentication.serializers.change_password import ChangePasswordSerializer


class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data)
        serializer.user = request.user

        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response({'detail': 'Cập nhật mật khẩu thành công'}, status=status.HTTP_200_OK)
