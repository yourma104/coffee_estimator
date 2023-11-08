# views.py in the "ml_models" app

from django.shortcuts import render, redirect
import pandas as pd
from .forms import CoffeeForm
from .models import Coffee
import pickle
import numpy as np


def create_coffee(request):
    if request.method == 'POST':
        form = CoffeeForm(request.POST)
        if form.is_valid():
            coffee = form.save()

            region = coffee.region
            country_of_origin = coffee.country_of_origin
            company = coffee.company
            variety = coffee.variety
            processing_method = coffee.processing_method
            species = coffee.species

            # Retrieve data from the Coffee model
            data = Coffee.objects.all()

            # Create a pandas DataFrame from the retrieved data
            df = pd.DataFrame(data.values())

            object_columns = ['species', 'country_of_origin', 'company', 'region', 'variety', 'processing_method']

            for column in object_columns:
                df = pd.concat([df.drop(column, axis=1), pd.get_dummies(df[column], prefix=column)], axis=1)

            # Load the additional data from the CSV file
            file_path = 'ml_model/columns.csv'  # Assuming the CSV file is in the same folder as the views file

            # Check if the file exists before attempting to load it
           # Check if the file exists before attempting to load it
            additional_data = pd.read_csv(file_path)

            # Find the new columns that are in additional_data but not in df
            new_columns = set(additional_data.columns) - set(df.columns)

            # Create a DataFrame filled with False values for the new columns
            zero_data = {col: [False] * len(df) for col in new_columns}

            # Handle the 'region' column separately
            
            # Concatenate the original df with the new columns DataFrame
            new_df = pd.DataFrame(zero_data)
            df = pd.concat([df, new_df], axis=1)

            # Drop the 'region_{region}' column

            region_column = 'region'
            if f'region_{region}' not in additional_data.columns:
                df[f'{region_column}_Other'] = [True] * len(df)
                df.drop(columns=[f'{region_column}_{region}'], inplace=True)
            else:
                df[f'{region_column}_{region}'] = [True] * len(df)

            
            country_of_origin_column = 'country_of_origin'
            if f'country_of_origin_{country_of_origin}' not in additional_data.columns:
                df[f'{country_of_origin_column}_Other'] = [True] * len(df)
                df.drop(columns=[f'{country_of_origin_column}_{country_of_origin}'], inplace=True)
            else:
                df[f'{country_of_origin_column}_{country_of_origin}'] = [True] * len(df)

            
            variety_column = 'variety'
            if f'variety_{variety}' not in additional_data.columns:
                df[f'{variety_column}_Other'] = [True] * len(df)
                df.drop(columns=[f'{variety_column}_{variety}'], inplace=True)
            else:
                df[f'{variety_column}_{variety}'] = [True] * len(df)

            
            species_column = 'species'
            if f'species_{species}' not in additional_data.columns:
                df[f'{species_column}_Other'] = [True] * len(df)
                df.drop(columns=[f'{species_column}_{species}'], inplace=True)
            else:
                df[f'{species_column}_{species}'] = [True] * len(df)

            
            processing_method_column = 'processing_method'
            if f'processing_method_{processing_method}' not in additional_data.columns:
                df[f'{processing_method_column}_Other'] = [True] * len(df)
                df.drop(columns=[f'{processing_method_column}_{processing_method}'], inplace=True)
            else:
                df[f'{processing_method_column}_{processing_method}'] = [True] * len(df)

            company_column = 'company'
            if f'company_{company}' not in additional_data.columns:
                df[f'{company_column}_Other'] = [True] * len(df)
                df.drop(columns=[f'{company_column}_{company}'], inplace=True)
            else:
                df[f'{company_column}_{company}'] = [True] * len(df)



            correct_feature_order = additional_data.columns

            df = df[correct_feature_order]

            filename = 'ml_model/coffee_model_final2.pkl'


# Load the model from the pickle file
            with open(filename, 'rb') as file:
                loaded_model = pickle.load(file)

            predictions = loaded_model.predict(df)

            df_fc = pd.read_csv('ml_model/test_y25.csv') # Assuming the CSV file is in the same folder as the views file


            df_p = pd.DataFrame(data=predictions, columns=df_fc.columns)

            df_p= np.round(df_p, 2)
            
            aroma = df_p.at[0, 'aroma']
            flavor = df_p.at[0, 'flavor']
            aftertaste = df_p.at[0, 'aftertaste']
            body = df_p.at[0, 'body']
            sweetness = df_p.at[0, 'sweetness']

            context = {
            'coffee': coffee,  # if you still need the coffee object
            'aroma': aroma,
            'flavor': flavor,
            'aftertaste': aftertaste,
            'body': body,
            'sweetness': sweetness,
}
            coffee.delete()
# Instead of 'html_table', we are now passing the context dictionary
            return render(request, 'display.html', context)
            # Delete the coffee record from the database
    else:
        form = CoffeeForm()
    # If it's a GET request or a form submission with validation errors, don't delete the data
    return render(request, 'coffee_e.html', {'form': form})


def success_page(request):
    latest_coffee = Coffee.objects.latest('id')

    return render(request, 'display.html', {'coffee': latest_coffee})


def try_new_coffee(request):
    if request.method == 'POST':
        # Here, you can add any server-side logic that needs to happen 
        # before a user tries a new coffee. If you don't need to handle
        # anything, you can directly redirect to the coffee entry page.

        return redirect('create_coffee')

# views.py in your tutorial_app


def tutorial(request):
    return render(request, 'tutorial.html')








# views.py
from django.http import JsonResponse
from .models import SPECIES_CHOICES
from .models import PROCESSING_METHODS
from .countries import COUNTRIES
from .variety import COFFEE_VARIETIES
from .company import COFFEE_COMPANIES
from .region import REGION_CHOICES 

# Import other options lists as needed


