#import os
import driftmlp
import os
file = os.environ['DRIFTFILE']
day_cut_off=5
silent = False
import pickle
drift_kwargs = {'variables':['position','drogue', 'datetime'], 'drop_na':False, 'drogue':True}
fnames = {True:'drg', False:'nodrg', None:'both'}
for drogue in [True, False, None]:
    drift_kwargs['drogue']=drogue
    network = driftmlp.file_to_network(file, drift_kwargs, day_cut_off=5)
    driftmlp.helpers.remove_undesired(network)
    fname = f"transition_{fnames[drogue]}"
    network['discretizer'] = None

    # .GraphML format coverts numerics to floats
    network.vs['name'] = [str(i) for i in network.vs['name']]
    network.write_graphml(fname+'.GraphML')
