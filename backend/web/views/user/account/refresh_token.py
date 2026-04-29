from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken


class RefreshTokenView(APIView):
    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.COOKIES.get('refresh_token')
            if not refresh_token:
                return Response({
                    'result':'refres_token 不存在'
                },status=401)
            refresh = RefreshToken(refresh_token)#自动检测是否在有效期如果过期报异常
            if settings.SIMPLE_JWT['ROTATE_REFRESH_TOKENS']:#同时刷新refresh和access
                refresh.set_jti()
                response = Response({
                    'result':'access',
                    'access': str(refresh.access_token),
                })
                response.set_cookie(
                    key='refresh_token',
                    value=str(refresh),
                    httponly=True,
                    samesite='Lax',
                    secure=True,
                    max_age=84600 * 7  # 默认七天有效
                )
                return response
            return Response({
                'result':'success',
                'access':str(refresh.access_token),
            })
        except:
            return Response({
                'result':'refresh_token 过期，请重新登录',
            },status = 401)