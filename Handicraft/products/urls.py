from rest_framework.routers import DefaultRouter
from products.views import *


router = DefaultRouter()
router.register(r'products', ProductViewset)
router.register(r'other_products', OtherProductViewset)   
urlpatterns = router.urls