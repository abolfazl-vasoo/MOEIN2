from django.shortcuts import render

# Create your views here.
from django.views import View
from django.views.generic.base import TemplateView
from site_module.models import SiteSetting , Slider


# class HomeView(View):
#     def get(self, request):
#         context = {
#             'data': 'this is data'
#         }
#         return render(request, 'home_module/index_page.html', context)



class HomeView(TemplateView):
    template_name = 'home_module/index_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        sliders = Slider.objects.filter(is_active=True)
        context['sliders'] = sliders
        return context



def site_header_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
    context = {
        'site_setting': setting
    }
    return render(request, 'shared/site_header_component.html', context)
# def site_header_component(request):
#
#     setting : SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()
#
#     context = {
#         'site_seting': setting
#     }
#     return render(request, 'shared/site_header_component.html', context)
#
#
def site_footer_component(request):
    setting: SiteSetting = SiteSetting.objects.filter(is_main_setting=True).first()

    context = {
        'site_seting': setting
    }
    return render(request, 'shared/site_footer_component.html', context)
