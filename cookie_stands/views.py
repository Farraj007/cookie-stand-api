from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import CookieStand
from .permissions import IsOwnerOrReadOnly
from .serializers import CookieSerializer

@csrf_protect
class CookieStandList(ListCreateAPIView):
    queryset = CookieStand.objects.all()
    serializer_class = CookieSerializer

@csrf_protect
class CookieStandDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = CookieStand.objects.all()
    serializer_class = CookieSerializer
