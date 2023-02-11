from ..models import Measurement
from variables.logic.variables_logic import *
def get_measurements():
    measurement = Measurement.objects.all()
    return measurement

def get_measurement(meas_pk):
    measurement = Measurement.objects.get(pk=meas_pk)
    return measurement

def update_measurement(meas_pk, new_meas):
    measurement = get_measurement(meas_pk)
    measurement.variable = get_variable(new_meas["variable"])
    measurement.value = new_meas["value"]
    measurement.unit = new_meas["unit"]
    measurement.place = new_meas["place"]
    measurement.save()
    return measurement

def create_measurement(meas):
    measurement = Measurement(variable=get_variable(meas["variable"]), value=meas["value"], unit=meas["unit"], place=meas["place"])
    measurement.save()
    return measurement

def delete_measurement(meas_pk):
    measurement = get_measurement(meas_pk)
    measurement.delete()
    return measurement
