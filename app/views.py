from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import LogSerializer
from .handlers import get_event_handler

@api_view(['GET', 'POST'])
def create_log(request): 
    if request.method == 'POST':
        serialized_item = LogSerializer(data=request.data)
        serialized_item.is_valid(raise_exception=True)
        
        event_handler = get_event_handler()
        event_handler.handle_request(request)
        
        return Response(serialized_item.data, status=status.HTTP_201_CREATED) 
    
