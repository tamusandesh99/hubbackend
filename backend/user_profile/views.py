from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserProfile
from .serializers import UserProfileSerializer


class GetUserProfileView(APIView):
    def get(self, request, format=None):
        try:
            user = self.request.user
            username = user.username
            print(user)
            user_profile = UserProfile.objects.get(user=user)
            user_profile = UserProfileSerializer(user_profile)

            return Response({'profile': user_profile.data, 'username': str(username)})
        except:
            return Response({'error': 'Something went wrong when retrieving profile'})


class UpdateUserProfileView(APIView):
    def put(self, request, format=None):
        try:
            user = self.request.user
            username = user.username

            data = self.request.data
            website_link = data['website_link']

            UserProfile.objects.filter(user=user).update(website_link=website_link)

            user_profile = UserProfile.objects.get(user=user)
            user_profile = UserProfileSerializer(user_profile)

            return Response({'profile': user_profile.data, 'username': str(username)})
        except:
            return Response({'error': 'Something went wrong when updating profile'})


class GetUserProfileAndWebsiteView(APIView):
    def get(self, request, format=None):
        try:
            user = self.request.user
            username = user.username

            user_profile = UserProfile.objects.filter(user=user).first()

            if user_profile is not None and user_profile.website_link:
                # If the user has a website link, include it in the response
                user_profile = UserProfileSerializer(user_profile)
                return Response({'profile': user_profile.data, 'username': str(username)})
            else:
                # If the user does not have a website link, return an empty string
                return Response({'username': str(username), 'website_link': ' '})

        except:
            return Response({'error': 'Something went wrong when retrieving profile'})