from .models import CompanyInfo
# This function gets current company name from CompanyInfo model to all pages.
def company_name(request):
    try:
        company = CompanyInfo.objects.all()
        if len(company) > 0:
            company = company[0]
            print(company.company_id)
    except company.DoesNotExist:
        company = None

    return {
        'company_name': company.company_name if company else 'Įmonės pavadinimas',
    }