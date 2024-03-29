'----Run the below Command----'
#pip install prophet
#pip install scipy

#loading of the libararies
import pickle
import operation as op
import pandas as pd
from datetime import datetime
import numpy as np
from scipy import stats,special

test=pd.DataFrame()
def choice(option,start_date,days,select):
    start1=datetime.strptime(start_date,"%Y-%m-%d")
    test['ds']=pd.date_range(start=start1,periods=days,freq='D')
    if option =='overall':
        model=pickle.load(open('model_overall.pkl','rb'))
        forecast_data=(model.predict(test))
        forecast_orig=np.exp(forecast_data['yhat'])
        forecast_orig_upp=np.exp(forecast_data['yhat_upper'])
        forecast_orig_low=np.exp(forecast_data['yhat_lower'])
        if (select == 'lower'):
            return op.operation(forecast_orig_low)
        elif (select == 'upper'):
            return op.operation(forecast_orig_upp)
        else:
            return op.operation(forecast_orig)
    elif option == 'BC':
        model=pickle.load(open('model_BC_2.pkl','rb'))
        forecast_data=(model.predict(test))
        forecast_orig=special.inv_boxcox((forecast_data['yhat']),-0.0417)
        forecast_orig_low=special.inv_boxcox((forecast_data['yhat_lower']),-0.0417)
        forecast_orig_upp=special.inv_boxcox((forecast_data['yhat_upper']),-0.0417)
        if (select == 'lower'):
            return op.operation(forecast_orig_low)
        elif (select == 'upper'):
            return op.operation(forecast_orig_upp)
        else:
            return op.operation(forecast_orig)
    elif option == 'HM':
        model=pickle.load(open('model_HM_2.pkl','rb')) 
        forecast_data=(model.predict(test))
        forecast_orig=special.inv_boxcox((forecast_data['yhat']),0.006)
        forecast_orig_low=special.inv_boxcox((forecast_data['yhat_lower']),0.006)
        forecast_orig_upp=special.inv_boxcox((forecast_data['yhat_upper']),0.006)
        if (select == 'lower'):
            return op.operation(forecast_orig_low)
        elif (select == 'upper'):
            return op.operation(forecast_orig_upp)
        else:
            return op.operation(forecast_orig)
    elif option == 'SE':
        model=pickle.load(open('model_SE_2.pkl','rb')) 
        forecast_data=(model.predict(test))
        forecast_orig=special.inv_boxcox((forecast_data['yhat']),-0.0315)
        forecast_orig_low=special.inv_boxcox((forecast_data['yhat_lower']),-0.0315)
        forecast_orig_upp=special.inv_boxcox((forecast_data['yhat_upper']),-0.0315)
        if (select == 'lower'):
            return op.operation(forecast_orig_low)
        elif (select == 'upper'):
            return op.operation(forecast_orig_upp)
        else:
            return op.operation(forecast_orig)
    elif option == 'PL':
        model=pickle.load(open('model_PL.pkl','rb'))
        forecast_data=(model.predict(test))
        forecast_orig=np.exp(forecast_data['yhat'])
        forecast_orig_low=np.exp(forecast_data['yhat_lower'])
        forecast_orig_upp=np.exp(forecast_data['yhat_upper'])
        if (select == 'lower'):
            return op.operation(forecast_orig_low)
        elif (select == 'upper'):
            return op.operation(forecast_orig_upp)
        else:
            return op.operation(forecast_orig)
    elif option == 'CP':
        model=pickle.load(open('model_CP.pkl','rb'))
        forecast_data=(model.predict(test))
        forecast_orig=np.exp(forecast_data['yhat'])
        forecast_orig_low=np.exp(forecast_data['yhat_lower'])
        forecast_orig_upp=np.exp(forecast_data['yhat_upper'])
        if (select == 'lower'):
            return op.operation(forecast_orig_low)
        elif (select == 'upper'):
            return op.operation(forecast_orig_upp)
        else:
            return op.operation(forecast_orig)
    else:
        print('Invalid Input')
    

 # example usuage   
print(choice('BC','2024-03-16',5,'lower'))


