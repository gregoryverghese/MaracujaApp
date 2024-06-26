import os
import pandas as pd
 
absolute_path = os.path.dirname(__file__)

#path = os.path.join(absolute_path, 'static/KCL-content/figures/Sample_bubbles')
#bubble_files = os.listdir(path)

#path = os.path.join(absolute_path, 'static/KCL-content/metadata/metadata.csv')
#metadata = pd.read_csv(path, delimiter='\t')

path = os.path.join(absolute_path, 'static/KCL-content/metadata.csv')
metadata = pd.read_csv(path, delimiter=',')

class figure:
    def __init__(self, file_name, figure_name, legend):
        self.file_name = file_name
        self.figure_name = figure_name
        self.legend = legend
    
    def __repr__(self):
        return self.file_name

"""
def initialise_bubble_overlay():
    fig_list = []
    for i in range(len(bubble_metadata)):
        row = bubble_metadata.iloc[i]
        new_fig = figure(row['file_name'], row['figure_name'], row['legend'])
        fig_list.append(new_fig)
    return fig_list

fig_list = initialise_bubble_overlay()
"""

# Create array of objects for each row of a dataframe
class Samples:
    def __init__(self, row):
        for i in range(len(row)):
            if str(row[i]) != 'nan':
                setattr(self, row.index[i], str(row[i]))
        self.id = row[0]

    def __repr__(self):
        return self.id

def initialise_samples():
    autoSampleList = []
    for i in range(len(metadata)):
        row = metadata.iloc[i]
        new_sample = Samples(row)
        autoSampleList.append(new_sample)
    return autoSampleList

autoSampleList = initialise_samples() 


filter_attributes = ['patient_id', 'pool', 'protocol', 'sequencing', 'sample_type']
sortby_attributes = ['N', 'shannons', 'simpsons', 'gutais']

### Testing ###
# sample = [ s for s in autoSampleList if s.id == 'KCL710-A_Pool7' ][0]
# print([ s for s in autoSampleList if s.id == 'KCL710-A_Pool7' ])
# print([ s for s in autoSampleList if s.id == 'KCL710-A_Pool7' ])



# print(dir(sample))
# print(sample.Negpval)
# print(sample.Negpval_bc55)

# # print(sample.DMSOpval)

# print(sample.CEFpval_bc55)

