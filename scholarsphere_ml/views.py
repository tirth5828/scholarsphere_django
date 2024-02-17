# from django.shortcuts import render

# # Create your views here.
# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import DataModel

# def add_data_to_db(request):
#     if request.method == 'POST':
#         # Assuming data is sent via POST request
#         data = request.POST.get('data')
#         # Save data to the database
#         DataModel.objects.create(data=data)
#         return JsonResponse({'message': 'Data added successfully'})
#     else:
#         return JsonResponse({'error': 'Only POST requests are allowed'})
    
    
# from django.shortcuts import render
# from django.http import JsonResponse
# from .models import DataModel
# from .train_model import train_and_compare_models

# def train_model(request):
#     # Assuming this view is accessed via a manual trigger or scheduled task
#     data_count = DataModel.objects.count()
#     if data_count >= 50:
#         # Get data from the database
#         data = list(DataModel.objects.all().values_list('data', flat=True))
#         # Clear the database
#         DataModel.objects.all().delete()
#         # Train and compare models
#         best_model_accuracy = train_and_compare_models(data)
#         return JsonResponse({'message': f'Model trained and compared. Best model accuracy: {best_model_accuracy}'})
#     else:
#         return JsonResponse({'message': 'Not enough data to train the model yet'})