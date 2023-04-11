from rest_framework.permissions import AllowAny
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Company, Vacancy, Resume


class StatisticsView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        companies_count = Company.objects.count()
        vacancies_count = Vacancy.objects.count()
        resumes_count = Resume.objects.count()

        response = {
            'companies': companies_count,
            'vacancies': vacancies_count,
            'resumes': resumes_count,
        }
        return Response(response)
