"""
API for student performance machine learning model.
Model format must be as follows:
['age',
 'Medu',
 'Fedu',
 'traveltime',
 'studytime',
 'failures',
 'famrel',
 'freetime',
 'goout',
 'Dalc',
 'Walc',
 'health',
 'absences',
 'school_MS',
 'sex_M',
 'address_U',
 'famsize_LE3',
 'Pstatus_T',
 'Mjob_health',
 'Mjob_other',
 'Mjob_services',
 'Mjob_teacher',
 'Fjob_health',
 'Fjob_other',
 'Fjob_services',
 'Fjob_teacher',
 'reason_home',
 'reason_other',
 'reason_reputation',
 'guardian_mother',
 'guardian_other',
 'schoolsup_yes',
 'famsup_yes',
 'paid_yes',
 'activities_yes',
 'nursery_yes',
 'higher_yes',
 'internet_yes',
 'romantic_yes']
"""

import pandas as pd
from flask import Flask, request, jsonify
import joblib
from sklearn.ensemble import RandomForestRegressor

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    feat_data = request.json
    df = pd.DataFrame(feat_data)
    df = df.reindex(columns=col_names)
    prediction = list(model.predict(df))

    return jsonify({"prediction": str(prediction)})

if __name__ == "__main__":
    model = joblib.load("C://Users/honer/Downloads/StudentPerformanceML/final_student_model.pkl")
    col_names = joblib.load("C://Users/honer/Downloads/StudentPerformanceML/student_column_names.pkl")



    app.run(debug=True)