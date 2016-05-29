import ast
import os

class ExtractTc:
    def find_tests(self, file_name):
        '''parsing the scenario for the required testcases'''
        function_desc_name_dict = {}
        function_desc_name_list = []
        file_name = str(file_name) #the correct path should be provided
        with open(file_name) as f:
            source = f.read()
        tree = ast.parse(source)
        #print ast.dump(tree)
        for node in tree.body:
            if isinstance(node, ast.ClassDef):
                #print node.name
                for function_nodes in node.body:
                    if isinstance(function_nodes, ast.FunctionDef):
                        function_name, function_desc = function_nodes.name, function_nodes.body
                        if 'test' in function_name and 'xtest' not in function_name:
                            function_desc_name = None
                            for fxn_nodes in function_desc:
                                if isinstance(fxn_nodes, ast.Expr):
                                    for child in ast.iter_fields(fxn_nodes):
                                        try:
                                            function_desc_only = (child[1].s).split('|')[1]
                                            break
                                        except:
                                            pass
                            function_name_only = str(file_name)+':'+str(node.name)+'.'+str(function_name)
                            function_desc_name_list.append(function_name_only)
        function_desc_name_dict[file_name] = function_desc_name_list
        '''returns a dictionary'''
        print function_desc_name_dict
		
if __name__=="__main__":
    et = ExtractTc()
    files_list = os.listdir(".")
    for i in files_list:
        if 'test' in i:
            et.find_tests(i)