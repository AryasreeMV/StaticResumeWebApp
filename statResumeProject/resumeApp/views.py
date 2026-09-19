from django.shortcuts import render

# Create your views here.


def viewResume(request):
    res_data = {
    "name": "ABHINAV K",
    "age": 30,
    "gender": "Male",
    "email": "abhinavk@gmail.com",
    "phone": "+91 7034047363",
    "location": "Kochi, Kerala, India",

    "skills": [
        "Python",
        "Django",
        "HTML",
        "CSS",
        "SQL"
    ],

    "experience": {
        "position": "Django Developer",
        "company": "ABC IT Solutions",
        "duration": "2021 - 2026"
    },

    "education": {
        "Degree": "Master of Computer Applications",
        "College": "ABC College",
        "Year": "2021"
    },

}
    return render(request, 'resume.html',{"resume": res_data})