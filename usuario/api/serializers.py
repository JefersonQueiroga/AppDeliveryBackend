from rest_framework import serializers
from usuario.models import User, Endereco
from django.contrib.auth.models import Group
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model= Group
        fields = ('id','name',)

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    email = serializers.EmailField(max_length=255, min_length=3)
    password = serializers.CharField(max_length=70, min_length=6, write_only=True)
    username = serializers.CharField(max_length=255, min_length=3, read_only=True)
    groups = GroupSerializer(many=True, read_only=True)
    tokens = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ['id','email', 'password', 'username','tokens','groups',]

    def validate(self, attrs):
        email = attrs.get('email', '')
        password = attrs.get('password', '')
        filtered_user_by_email = User.objects.filter(email=email)
        user = auth.authenticate(email=email, password=password)

        if not user:
            raise AuthenticationFailed('Credenciais erradas, tente novamente.')

        return {
            'id': user.id,
            'email': user.email,
            'username': user.username,
            'tokens': user.tokens,
        }
        
    def get_tokens(self, obj):
        user = User.objects.get(email=obj['email'])

        return {
            'refresh': user.tokens()['refresh'],
            'access': user.tokens()['access']
        }

class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=6, write_only=True)

    default_error_messages = {
        'username': 'O nickname do usuário podem conter apenas letras (a-z) e números (0-9)'}

    class Meta:
        model = User
        fields = ['email', 'username','password','phone']

    def validate(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class EnderecoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Endereco
        fields= ('__all__')