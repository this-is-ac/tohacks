from django.shortcuts import render
import pgeocode

nomi = pgeocode.Nominatim('ca')
import pickle
import pandas as pd
from .models import Person


# Create your views here.
def index(request):
    if request.method == "POST":
        email = request.POST['u']
        pincode = request.POST['p']
        cords = nomi.query_postal_code(pincode)
        lat = cords["latitude"]
        lon = cords["longitude"]
        P = Person.objects.create(email=email, pincode=pincode)
        P.save()
        df = pd.read_csv("ToHacks_Dataset.csv")
        df = df.drop_duplicates()
        df = df.fillna(0)
        pkl_filename = "toihacks2/pickle_rfcmodel.pkl"

        with open(pkl_filename, 'rb') as file:
            model = pickle.load(file)

        Closest = df.iloc[(df['Latitude'] - lat + df['Longitude'] - lon).abs().argsort()[:10]]
        Mean_Values = Closest.mean()
        Inputs_to_model = Mean_Values[2:8]

        Prediction = model.predict([Inputs_to_model])
        print("Model Prediction ", Prediction)
        # print(Closest)

        if (Prediction == 0):
            stringn = "Currently no danger of floods"
        else:
            stringn = "Flood Warning . Be safe and get to high ground"

        string1 = " Location :" + str(Closest.iloc[0]['Latitude']) + ' and ' + str(
            round((Closest.iloc[0]['Longitude']), 4))
        string2 = "Precipitation Value of :" + str(Closest.iloc[0]['Precipitation1'])
        string3 = "Closest Dam :" + str(Closest.iloc[0]['Dams']) + "Kms"

        response = {'pred1': string1, 'prednow': stringn, 'pred2': string2, 'pred3': string3}
        return render(request, 'dashboard.html', response)
    else:
        return render(request, 'landing.html')
