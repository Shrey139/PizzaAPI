from rest_framework import routers
from .views import PizzaViewSet

router = routers.SimpleRouter()
router.register('', PizzaViewSet)
urlpatterns = router.urls