from django.urls import path
from . import views

app_name = "vendeo_managememnt"
urlpatterns = [
    path("vendor", views.VendorAPIView.as_view(), name="vendor"),
    path(
        "vendor/<int:pk>/", views.VendorAPIView.as_view(), name="vendor-update"
    ),
    path(
        "vendor/<int:pk>/performance",
        views.vendor_performance,
        name="vendor-performance",
    ),
    path(
        "purchase_orders/",
        views.PurchasedOrderAPIView.as_view(),
        name="purchase",
    ),
    path(
        "purchase_orders/<int:pk>/acknowledge",
        views.order_acknowledge,
        name="purchase-ack",
    ),
    path(
        "purchase_orders/<int:pk>/",
        views.PurchasedOrderAPIView.as_view(),
        name="purchase_orders-update",
    ),
    path(
        "purchase_orders/<int:pk>/acknowledge",
        views.order_acknowledge,
        name="purchase-ack",
    ),
]
