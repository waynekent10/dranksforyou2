
from rest_framework.decorators import api_view
from rest_framework.response import Response
from dranksforyou2api.models.user import User


@api_view(['POST'])
def check_user(request):
    '''Checks to see if user exists

    Method arguments:
      request -- The full HTTP request object
    '''
    uid = request.data['uid']

    # Use the built-in authenticate method to verify
    # authenticate returns the user object or None if no user is found
    user = User.objects.filter(uid=uid).first()

    # If authentication was successful, respond with their token
    if user is not None:
        data = {
            'id': user.id,
            'name': '',
            'uid': user.uid,
        }
        return Response(data)
    else:
        # Bad login details were provided. So we can't log the user in.
        data = { 'valid': False }
        return Response(data)


@api_view(['POST'])
def register_user(request):
    '''Handles the creation of a new rare_user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    user = User.objects.create(
        uid=request.data['uid'],
        name=request.data['name'],
        username=request.data['username'],
        email=request.data['email'],
    )

    # Return the user info to the client
    data = {
        'id': user.id,
        'uid': user.uid,
        'name': user.name,
        'username': user.username,
        'email': user.email,
    }
    return Response(data)
