# Importing an entire module.

import printing_functions as pf

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_designs, completed_models)
pf.show_completed_models(completed_models)

print("")

# Importing specific functions from a module.

from printing_functions import print_models as pm, show_completed_models as show_cm

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

pm(unprinted_designs, completed_models)
show_cm(completed_models)
