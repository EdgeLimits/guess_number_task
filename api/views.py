from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.cache import cache
from api.library.guess_from_cache import make_guess, get_summary
from api.serializers import GuessSerializer


class GuessView(APIView):
    permission_classes = []

    # POST
    def post(self, request):
        serializer = GuessSerializer(data=request.data)
        if serializer.is_valid():
            action = serializer.validated_data.get('action', '')
            if action in ['start', '<', '>']:
                data = make_guess(
                    cache=cache,
                    move=action,
                )
                return Response(
                    data=data,
                    status=status.HTTP_200_OK
                )

            elif action == '=':
                data = get_summary(cache=cache)
                return Response(
                    data=data,
                    status=status.HTTP_200_OK
                )

            else:
                return Response(
                    {"action": ["edge case errror on actions"]},
                    status=status.HTTP_400_BAD_REQUEST
                )
        
        else:
            # print(serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        
