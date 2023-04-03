from django.middleware.common import CommonMiddleware
from django.http import HttpResponse

class BackButtonMiddleware(CommonMiddleware):
    def process_request(self, request):
        if request.META.get('HTTP_CACHE_CONTROL') == 'max-age=0':
            # здесь вы можете выполнить необходимые действия при нажатии на кнопку "назад"
            return HttpResponse('Вы вернулись назад!')
        return super().process_request(request)
