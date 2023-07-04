from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from authentication.serializers.user import RegistrationSerializer
from authentication.models import user


class Registration(generics.CreateAPIView):
    serializer_class = RegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        account = serializer.save()
        data = {
            'response': 'Registration Successful',
            'user_name': account.username,
            'email': account.email
        }
        try:
            token = Token.objects.get(user=account).key
            data['token'] = token
        except Token.DoesNotExist:
            data['token'] = None

        return Response(data, status=status.HTTP_201_CREATED)


class LogOut(generics.CreateAPIView):

    def create(self, request, *args, **kwargs):
        if request.method == 'POST':
            request.user.auth_token.delete()
            return Response('Logout successful', status=status.HTTP_200_OK)
