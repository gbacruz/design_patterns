'''
    Goal
        Create a pice of code that can create a html elements,
        for example: 
            <ul>
                <li>text 1 </li>
                <li>text 2 </li>
            </ul>
'''


param_structure = ['element','contain',['childs']]

class Builder:
    
    def __init__(self, params):
        self.params = params 
        self.element = params[0]
        self.contain = params[1]
        self.childs = params[-1]
        self.node_childs = []
    def single_element(self, element,contain):
        builder = f' <{element}>\n{contain}\n</{element}> \n'
        return builder

    def have_childs(self, childs):
        if len(childs)==0:
            return None
        else:
            child_element = childs[0][0]
            child_contain = childs[0][1]
            build_child = self.single_element(child_element, child_contain)            
            self.node_childs.append(build_child)
            self.have_childs(childs[1:])
        return ''.join(self.node_childs)

        print(contain)
        return contain

    def __str__(self):
        return ' I am here'

    def build_it(self):
        if type(self.childs)==list:
            contain = [self.contain]
            contain.append(self.have_childs(self.childs))
            response = self.single_element(html_builder.params[0], ''.join(contain))
        else:
            response = self.single_element(html_builder.params[0], html_builder.params[1])
        print(response)            


item = ['a','link to']
item2 = ['a','other link to']
html_element = ['p','my pyton code',[item, item2]]

html_builder = Builder(html_element)
html_builder.build_it()