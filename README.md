# Restaurant
Full stack project about restaurant booking system
    path('', views.index, name='index'),
    #path('users/',UserView.as_view()),
    path('menu/', views.MenuItemView.as_view(), name='menu-list-create'),
    path('menu/<int:pk>/', views.SingleMenuItemView.as_view(), name='menu-detail'),
    path('admin/', admin.site.urls),
    path('restaurant/', include('littlelemon.urls')), 
    path('restaurant/api/', include(router.urls)),#add tables and users after restaurant/api to see the users and bookings lists
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('api-token-auth/', obtain_auth_token),
