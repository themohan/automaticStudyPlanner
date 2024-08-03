from rest_framework.response import Response
from rest_framework.decorators import api_view
from serializers import StudentInfoSerializer, TimeTableGeneratedSerializer


@api_view(['POST'])
def create_study_form(request):
    item = request.data
    item = StudentInfoSerializer(data=item)
    if item.is_valid():
        item.save()
    schedule = generate_table(item)
    return Response(schedule, 200)

def generate_table(item):
    # json_data = get_rows_timetable_data(item)
    json_data = {}
    new_data = TimeTableGeneratedSerializer(data=json_data)
    if new_data.is_valid():
        new_data.save()
    return TimeTableGeneratedSerializer(new_data).data
