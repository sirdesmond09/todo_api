from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = '__all__'
        

class ChangePasswordSerializer(serializers.Serializer):
    old_password  = serializers.CharField(max_length=200)
    new_password  = serializers.CharField(max_length=200)
    confirm_password  = serializers.CharField(max_length=200)
    
    
    def check_pass(self):
        """ checks if both passwords are the same """
        if self.validated_data['new_password'] != self.validated_data['confirm_password']:
            raise serializers.ValidationError({"error":"Please enter matching passwords"})
        return True
            
 


