import pandas as pd
b_math = {'Student': ['Ice Bear', 'Panda', 'Grizzly'], 'Math': [80,95,79]}
bdf_math = pd.DataFrame(b_math, columns = ['Student', 'Math'])
b_elecs = {'Student': ['Ice Bear', 'Panda', 'Grizzly'], 'Electronics': [85,81,83]}
bdf_elecs = pd.DataFrame(b_elecs, columns = ['Student', 'Electronics'])
b_GEAS = {'Student': ['Ice Bear', 'Panda', 'Grizzly'], 'GEAS': [90,79,93]}
bdf_GEAS = pd.DataFrame(b_GEAS, columns = ['Student', 'GEAS'])
b_ESAT = {'Student': ['Ice Bear', 'Panda', 'Grizzly'], 'ESAT': [93,89,88]}
bdf_ESAT = pd.DataFrame(b_ESAT, columns = ['Student', 'ESAT'])
bdf_math_elecs = pd.merge(bdf_math, bdf_elecs, on= 'Student')
bdf_math_elecs_GEAS = pd.merge(bdf_math_elecs, bdf_GEAS, on='Student')
all_subj = pd.merge(bdf_math_elecs_GEAS, bdf_ESAT, on='Student')
wide_to_long = pd.melt(all_subj, id_vars = 'Student', value_vars = ['Math', 'Electronics', 'GEAS', 'ESAT']) 
wide_to_long.rename(columns = {'variable':'Subject','value':'Grades'}, inplace = True)