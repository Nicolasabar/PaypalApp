import stripe
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from user.api.serializers import UserRegisterSerializer
from user.models import User
from wallet.models import Wallet

stripe.api_key = "sk_test_51Ps355LAcjaRrmTJWZaBA69KhzMGgqVZCIjSwOFRC7cVJEh92meUvIjx5xH0z7lr91hJhd3Ppd4XgtvvRoq1K7sp000VnwvGHI"


class RegisterView(APIView):
    def post(self, request):
        
        #Se crea la wallet asociada al usuario con saldo incial de 0
        wallet = Wallet(balance = 0)
        wallet.save()
        
        
        serializer = UserRegisterSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception = True):
            new_user = serializer.save()
            emailIUser = serializer.data['email']
            
            ## Uso de stripe pasarela de pago y registro del usuario email id
            user_stripe = stripe.Customer.create(email=emailIUser)
            id_user_stripe = user_stripe.id
            
            user = User.objects.get(pk=new_user.id)
            user.id_user_stripe = id_user_stripe
            user.wallet = wallet
                
            user.save()
            
            
            return Response(serializer.data, status = status.HTTP_200_OK)
        
        return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        
    