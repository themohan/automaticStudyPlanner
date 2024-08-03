from rest_framework.response import Response
from rest_framework.decorators import api_view
from serializers import StudentInfoSerializer


@api_view(['POST'])
def create_study_form(request):
    item = request.data
    item = StudentInfoSerializer(data=item)
    if item.is_valid():
        item.save()
    schedule = generate_table(item)
    return Response(schedule)

def generate_table(item):
    pass


# @api_view(['POST'])
# def update_progress(request):
#     data = request.data
