# 301 OK maybe
class Optimizer_Template:
    def __init__(self) -> None:
        """
        function的說明
        """
        raise Exception("using template class")
    
    def optimize(self) -> None:
        """
        start optimizing component
        """
        raise Exception("not implemented")

import os

class Netadapt:
    def __init__(self)-> None:
        self.netadapt_path = 'netadapt'
    
    def optimize(self,model_path, model_arch, dataset_path, input_shape: tuple, resource, budget_ratio, working_folder="", latency_lut=""):
        input_shape = str(input_shape).replace('(',"").replace(')',"").replace(','," ")
        if working_folder=="":
            working_folder=model_path+"/alexnet/prune-by-mac"
        if resource == 'latency':
            if latency_lut=="":
                raise Exception("latency lookup table is not specified")
            os.system(f"CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6 python master.py \"{working_folder}\" {input_shape} -im {model_path} -gp 0 -mi 30 -bur {budget_ratio} -rt LATENCY  -irr 0.025 -rd 0.96 -lr 0.001 -st 500 -lt {latency_lut} -dp {dataset_path} --arch {model_arch}")
        elif resource == 'mac':
            os.system(f"CUDA_VISIBLE_DEVICES=0,1,2,3,4,5,6 python master.py \"{working_folder}\" {input_shape} -im {model_path} -gp 0 -mi 30 -bur {budget_ratio} -rt FLOPS  -irr 0.025 -rd 0.96 -lr 0.001 -st 500 -dp {dataset_path} --arch {model_arch}")
        else:
            print("resource not supported")
            raise Exception("resource not supported")
