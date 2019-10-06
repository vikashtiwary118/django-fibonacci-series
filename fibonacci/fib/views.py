import time
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect

from .models import FibonacciResults


def fib_cal(number):
    if number < 2:
        return 1
    else:
        number_sequence_1 = 1
        number_sequence_2 = 1
        for num in range(2, number):
            temp = number_sequence_1 + number_sequence_2
            number_sequence_1 = number_sequence_2
            number_sequence_2 = temp
        return number_sequence_2


def fibonacci(request):
    num = 0
    result = 0
    execution_time = 0

    if request.GET.get('number'):
        start_time = time.time()
        number = request.GET.get('number')
        num = int(number)
        result = fib_cal(num)
        end_time = time.time() - start_time
        execution_time = str(end_time)[0:4]

        obj = FibonacciResults.objects.create(
            number=num, result=result, time_taken=execution_time)
        obj.save()

    return render(request,'fib/index.html',{'number': num,'result': result,'time_taken': execution_time})

   