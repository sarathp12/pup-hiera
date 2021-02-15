import sys
import ruamel.yaml
from ruamel.yaml.scalarstring import SingleQuotedScalarString, DoubleQuotedScalarString

yaml = ruamel.yaml.YAML(typ='rt')
yaml.preserve_quotes = True
yaml.default_flow_style = False
yaml.allow_unicode = False
yaml.Loader = ruamel.yaml.RoundTripLoader
yaml.width = 800    

#cur_yaml = yaml.load("/Users/parthap/python-exercises/tmp/pup-hiera/example.yaml")
#cur_yaml['org_types::keys']['tommy']['auth_keys'].append('ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAIEA0KJDLOiiXj9XdMxiCT9KvaKfuxFQi+CIiklaN5hHsNgYOu7TijqyONEu5fONLoAo/cshLa+KuargyTrtizwcP4TPcTXZhhJrM0GUDJragw7SMVIs/5xJBGAyHKJ1YUMGO7+nJTmsCLx6PFOlQYveuriiVVCCZerGCLH+UtSXK3z+l7hx9NiDg3/ylOLc3f3SLxrJKn0gMTgK7BHJFXo4PguuPjWZLVdUDX+XKiqtT2n4IsYs6N9qVFG3zUgNlEjZM47NK/ytAC0max98pK+QNzsuaQOo/IShJ1TOw5wwScflPArVJ2AyROqAe7cfQg7q12I9olASFd3U5NazfZCTYAvWA1kz9UZEWLJ1Br1XOkPqOleMM8KCp/PXzz8H0kISkMIji0/QuiZOPEBsKlszXjlALcXR8Mg1uiZVWy48i9JheyXyj1ToCj6cPScpgFHp3DAGSlKKbE1EFaVfeeyGAnHESlnDDg3Gq5xSsB9Okqm3V5t8GpFaJbV68BxQ4BK6HJ21A3CinV4LdV3hR/OBUbDG2EcI+ZKRDjlpJuu4YU= psp@psp-mac')
#yaml.dump(cur_yaml, sys.stdout)
#yaml.indent(mapping=4, sequence=4, offset=2)
#
copy_level_str = "ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAIEA0KJDLOiiXj9XdMxiCT9KvaKfuxFQi+CIiklaN5hHsNgYOu7TijqyONEu5fONLoAo/cshLa+KuargyTrtizwcP4TPcTXZhhJrM0GUDJragw7SMVIs/5xJBGAyHKJ1YUMGO7+nJTmsCLx6PFOlQYveuriiVVCCZerGCLH+UtSXK3z+l7hx9NiDg3/ylOLc3f3SLxrJKn0gMTgK7BHJFXo4PguuPjWZLVdUDX+XKiqtT2n4IsYs6N9qVFG3zUgNlEjZM47NK/ytAC0max98pK+QNzsuaQOo/IShJ1TOw5wwScflPArVJ2AyROqAe7cfQg7q12I9olASFd3U5NazfZCTYAvWA1kz9UZEWLJ1Br1XOkPqOleMM8KCp/PXzz8H0kISkMIji0/QuiZOPEBsKlszXjlALcXR8Mg1uiZVWy48i9JheyXyj1ToCj6cPScpgFHp3DAGSlKKbE1EFaVfeeyGAnHESlnDDg3Gq5xSsB9Okqm3V5t8GpFaJbV68BxQ4BK6HJ21A3CinV4LdV3hR/OBUbDG2EcI+ZKRDjlpJuu4YU= psp@psp-mac"
copy_str = "'"+copy_level_str+"'"

#new_copy_level_str = SingleQuotedScalarString('ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAIEA0KJDLOiiXj9XdMxiCT9KvaKfuxFQi+CIiklaN5hHsNgYOu7TijqyONEu5fONLoAo/cshLa+KuargyTrtizwcP4TPcTXZhhJrM0GUDJragw7SMVIs/5xJBGAyHKJ1YUMGO7+nJTmsCLx6PFOlQYveuriiVVCCZerGCLH+UtSXK3z+l7hx9NiDg3/ylOLc3f3SLxrJKn0gMTgK7BHJFXo4PguuPjWZLVdUDX+XKiqtT2n4IsYs6N9qVFG3zUgNlEjZM47NK/ytAC0max98pK+QNzsuaQOo/IShJ1TOw5wwScflPArVJ2AyROqAe7cfQg7q12I9olASFd3U5NazfZCTYAvWA1kz9UZEWLJ1Br1XOkPqOleMM8KCp/PXzz8H0kISkMIji0/QuiZOPEBsKlszXjlALcXR8Mg1uiZVWy48i9JheyXyj1ToCj6cPScpgFHp3DAGSlKKbE1EFaVfeeyGAnHESlnDDg3Gq5xSsB9Okqm3V5t8GpFaJbV68BxQ4BK6HJ21A3CinV4LdV3hR/OBUbDG2EcI+ZKRDjlpJuu4YU= psp@psp-mac')

#yaml.explicit_start = True
#yaml.explicit_end = False
#yaml.default_flow_style = False
#yaml.dash_inwards = True
#yaml.quotes_preserved =True
#yaml.parsing_mode = 'rt'

with open("/Users/parthap/python-exercises/tmp/pup-hiera/example.yaml", 'r') as f:
    res = yaml.load(f)
    print(res)
    res['org_types::keys']['tommy']['auth_keys'].append(SingleQuotedScalarString('ssh-rsa AAAAB3NzaC1yc2EAAAABIwAAAIEA0KJDLOiiXj9XdMxiCT9KvaKfuxFQi+CIiklaN5hHsNgYOu7TijqyONEu5fONLoAo/cshLa+KuargyTrtizwcP4TPcTXZhhJrM0GUDJragw7SMVIs/5xJBGAyHKJ1YUMGO7+nJTmsCLx6PFOlQYveuriiVVCCZerGCLH+UtSXK3z+l7hx9NiDg3/ylOLc3f3SLxrJKn0gMTgK7BHJFXo4PguuPjWZLVdUDX+XKiqtT2n4IsYs6N9qVFG3zUgNlEjZM47NK/ytAC0max98pK+QNzsuaQOo/IShJ1TOw5wwScflPArVJ2AyROqAe7cfQg7q12I9olASFd3U5NazfZCTYAvWA1kz9UZEWLJ1Br1XOkPqOleMM8KCp/PXzz8H0kISkMIji0/QuiZOPEBsKlszXjlALcXR8Mg1uiZVWy48i9JheyXyj1ToCj6cPScpgFHp3DAGSlKKbE1EFaVfeeyGAnHESlnDDg3Gq5xSsB9Okqm3V5t8GpFaJbV68BxQ4BK6HJ21A3CinV4LdV3hR/OBUbDG2EcI+ZKRDjlpJuu4YU= psp@psp-mac'))
    print(res['org_types::keys']['tommy']['auth_keys'])

with open('/Users/parthap/python-exercises/tmp/pup-hiera/example.yaml', 'w') as f:
    #yaml.default_style = "'"
    yaml.dump(res, stream=f)
    
#stream=f, default_flow_style=False, sort_keys=False)