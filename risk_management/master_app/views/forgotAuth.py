from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.core.mail import send_mail


class ForgotPasswordView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User with this email does not exist'}, status=400)
        
        # Generate token and save it in the database
        token_generator = PasswordResetTokenGenerator()
        uid = urlsafe_base64_encode(force_bytes(user.pk))
        token = token_generator.make_token(user)
        user.password_reset_token = token
        user.save()

        # Send email with password reset link
        reset_link = f"{request.scheme}://localhost:3000/#/Reset_Password/{token}"
        send_mail(
            'Password reset request',
            f'Please click on the following link to reset your password: {reset_link}',
            'from@example.com',
            [email],
            fail_silently=False,
        )

        return Response({'success': 'Plz check your email'}, status=200)
    
    
class ResetPasswordView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        password_reset_token = request.data.get('password_reset_token')
        print("======================================================")
        print(email)
        print(password)
        try:
            user = User.objects.get(password_reset_token=password_reset_token, email=email)
           
            user.password_reset_token = ""
            user.set_password(password)
            user.save()
        except User.DoesNotExist:
            return Response({'error': 'Some thing went wrong with this reset link'}, status=400)
        
        # Generate token and save it in the database
        # token_generator = PasswordResetTokenGenerator()
        # uid = urlsafe_base64_encode(force_bytes(user.pk))
        # token = token_generator.make_token(user)
        # user.save()
              

        return Response({'success': 'password updated sucessfully', 'data':user.email}, status=200)
    

