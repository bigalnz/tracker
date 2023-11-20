"""
Embedded Python Blocks:

Each time this file is saved, GRC will instantiate the first class it finds
to get ports and parameters of your block. The arguments to __init__  will
be the parameters. All of them are required to have default values!
"""

import numpy as np
from gnuradio import gr
import pmt


class blk(gr.sync_block):  # other base classes are basic_block, decim_block, interp_block
    """Embedded Python Block example - a simple multiply const"""

    def __init__(self, threshold=1.0):  # only default arguments here
        """arguments to this function show up as parameters in GRC"""
        gr.sync_block.__init__(
            self,
            name='Tags',   # will show up in GRC
            in_sig=[np.float32],
            out_sig=[np.float32]
        )
        # if an attribute with the same name as a parameter is found,
        # a callback is registered (properties work, too).
        self.threshold = threshold
        self.timer = 0
        self.readyForTag = True
        self.previousValue1 = None
        self.previousValue2 = None

    def work(self, input_items, output_items):
        """example: multiply with constant"""
        
        print(f"length of input items {len(input_items[0])}")
        for index in range(len(input_items[0])):
        
            
            print(f"index : {index}")

            if index > 3 and index < 5:
                #print("inside loop *********************")
                #print(f"index : {index} input itmes index : {input_items[0][index]}")
                #print(f"index : {index} input itmes -1 : {input_items[0][index-1]}")
                #print(f"index : {index} input itmes -2: {input_items[0][index-2]}")
                if input_items[0][index-1] > input_items[0][index] and input_items[0][index-1] > input_items[0][index-2]:
                    print(f"peak at {input_items[0][index-1]}")
                    key = pmt.intern("detect")
                    value = pmt.from_float(np.round(float(input_items[0][index-1]),2))
                    writeIndex = self.nitems_written(0) + index-1
                    print(f"Index:{writeIndex}")
                    print(f"Value:{value}")
                        
                    self.add_item_tag(0, writeIndex, key, value )   
                
        output_items[0][:] = input_items[0]
        return len(output_items[0])
