from login.models import CreateLogin
from django.http import HttpResponse

# Create your views here.
def create_user(request):
  first_name=request.GET['firstName']
  last_name=request.GET['lastName']
  address=request.GET['Address']
  Gender=request.GET['gender']
  State=request.GET['state']
  City=request.GET['city']
  Dob=request.GET['Dob']
  Pincode=request.GET['pinCode']
  CourseId=request.GET['courseId']
  Course=request.GET['course']
  Email=request.GET['Email']
 
  
  login_obj = CreateLogin(
    first_name=first_name,
    last_name=last_name, 
    address=address,
    Gender=Gender,
    State=State,
    City=City,
    Dob=Dob,
    Pincode=Pincode,
    CourseId=CourseId,
    Course=Course,
    Email=Email
  )
  login_obj.save()
      
  return HttpResponse('Sucessfull !!')
