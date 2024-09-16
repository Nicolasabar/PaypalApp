from rest_framework import serializers
from user.models import User 

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # datos que se van a manejar para la creacion del usuario
        fields = ['id', 'email', 'username', 'password']
        
        
    def create(self, validate_data):
        password = validate_data.pop('password', None)
        instance = self.Meta.model(**validate_data)
            
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance